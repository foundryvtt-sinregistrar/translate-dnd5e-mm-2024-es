(async () => {
    const PACK_ID = "dnd-monster-manual.tables";
    const OUTPUT_FILE = "dnd-monster-manual.tables.en-source.json";

    const pack = game.packs.get(PACK_ID);

    if (!pack) {
        ui.notifications.error(`No se encontró el compendium: ${PACK_ID}`);
        console.error(`No se encontró el compendium: ${PACK_ID}`);
        return;
    }

    const toPlainObject = (value) => {
        if (!value) return value;
        if (typeof value.toObject === "function") return value.toObject();
        return value;
    };

    const normalizeCollection = (collection) => {
        if (!collection) return [];
        if (Array.isArray(collection)) return collection;
        if (Array.isArray(collection.contents)) return collection.contents;
        if (typeof collection[Symbol.iterator] === "function") return Array.from(collection);
        if (typeof collection === "object") return Object.values(collection);
        return [];
    };

    const getResultText = (resultObj) => {
        if (typeof resultObj?.text === "string") return resultObj.text;
        if (typeof resultObj?.description === "string") return resultObj.description;
        return undefined;
    };

    const getRangeStart = (resultObj) => {
        if (Array.isArray(resultObj?.range) && Number.isFinite(resultObj.range[0])) return resultObj.range[0];
        if (Number.isFinite(resultObj?.range?.[0])) return resultObj.range[0];
        if (Number.isFinite(resultObj?.sort)) return resultObj.sort;
        return 0;
    };

    const getRangeEnd = (resultObj) => {
        if (Array.isArray(resultObj?.range) && Number.isFinite(resultObj.range[1])) return resultObj.range[1];
        if (Number.isFinite(resultObj?.range?.[1])) return resultObj.range[1];
        return getRangeStart(resultObj);
    };

    const docs = await pack.getDocuments();

    const out = {
        label: "Tablas de tiradas",
        mapping: {
            results: {
                path: "results",
                converter: "mm2024RollTableResultsById"
            }
        },
        folders: {},
        entries: {}
    };

    let tableCount = 0;
    let resultCount = 0;
    let textResultCount = 0;

    const sortedTables = docs
        .map(doc => toPlainObject(doc))
        .sort((a, b) => {
            const an = a?.name ?? "";
            const bn = b?.name ?? "";
            return an.localeCompare(bn, "en", { sensitivity: "base" });
        });

    for (const table of sortedTables) {
        const tableId = table?._id ?? table?.id;
        if (!tableId) continue;

        const patch = {};

        if (typeof table.name === "string") {
            patch.name = table.name;
        }

        const rawResults = normalizeCollection(table.results);
        const sortedResults = rawResults
            .map(result => toPlainObject(result))
            .sort((a, b) => {
                const as = getRangeStart(a);
                const bs = getRangeStart(b);
                if (as !== bs) return as - bs;

                const ae = getRangeEnd(a);
                const be = getRangeEnd(b);
                if (ae !== be) return ae - be;

                const at = a?.text ?? "";
                const bt = b?.text ?? "";
                return at.localeCompare(bt, "en", { sensitivity: "base" });
            });

        const resultPatches = {};

        for (const result of sortedResults) {
            const resultId = result?._id ?? result?.id;
            if (!resultId) continue;

            const resultPatch = {};
            const text = getResultText(result);

            if (typeof text === "string" && text.trim() !== "") {
                resultPatch.text = text;
                textResultCount++;
            }

            if (Object.keys(resultPatch).length > 0) {
                resultPatches[resultId] = resultPatch;
                resultCount++;
            }
        }

        if (Object.keys(resultPatches).length > 0) {
            patch.results = resultPatches;
        }

        out.entries[tableId] = patch;
        tableCount++;
    }

    console.log(`[MM2024 tables export] Tables: ${tableCount}`);
    console.log(`[MM2024 tables export] Results: ${resultCount}`);
    console.log(`[MM2024 tables export] Results with text: ${textResultCount}`);
    console.log(out);

    const json = JSON.stringify(out, null, 2);

    const save =
        globalThis.saveDataToFile ??
        foundry.utils.saveDataToFile;

    save(json, "application/json", OUTPUT_FILE);

    ui.notifications.info(`Exportado ${OUTPUT_FILE}`);
})();

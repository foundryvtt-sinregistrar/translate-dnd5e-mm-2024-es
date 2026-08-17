(async () => {
    const PACK_ID = "dnd-monster-manual.content";
    const OUTPUT_FILE = "dnd-monster-manual.content.en-source.json";

    const pack = game.packs.get(PACK_ID);

    if (!pack) {
        ui.notifications.error(`No se encontró el compendium: ${PACK_ID}`);
        console.error(`No se encontró el compendium: ${PACK_ID}`);
        return;
    }

    const getProperty = foundry.utils.getProperty;

    const getPageText = (pageObj) => {
        if (typeof pageObj?.text === "string") return pageObj.text;
        if (typeof pageObj?.text?.content === "string") return pageObj.text.content;
        if (typeof getProperty(pageObj, "system.text.content") === "string") {
            return getProperty(pageObj, "system.text.content");
        }
        return undefined;
    };

    const getDescription = (pageObj) => {
        if (typeof pageObj?.description === "string") return pageObj.description;
        if (typeof pageObj?.description?.value === "string") return pageObj.description.value;
        if (typeof getProperty(pageObj, "system.description.value") === "string") {
            return getProperty(pageObj, "system.description.value");
        }
        return undefined;
    };

    const docs = await pack.getDocuments();

    const out = {
        label: "Manual de Monstruos",
        mapping: {
            title: "flags.dnd5e.title",
            pages: {
                path: "pages",
                converter: "mm2024JournalPagesById"
            }
        },
        folders: {},
        entries: {}
    };

    let entryCount = 0;
    let pageCount = 0;
    let textPageCount = 0;
    let titleCount = 0;

    const sortedDocs = docs
        .map(doc => doc.toObject())
        .sort((a, b) => {
            const an = a.name ?? "";
            const bn = b.name ?? "";
            return an.localeCompare(bn, "en", { sensitivity: "base" });
        });

    for (const entry of sortedDocs) {
        const entryId = entry._id ?? entry.id;
        if (!entryId) continue;

        const patch = {};

        if (typeof entry.name === "string") {
            patch.name = entry.name;
        }

        const entryTitle = getProperty(entry, "flags.dnd5e.title");
        if (typeof entryTitle === "string") {
            patch.title = entryTitle;
            titleCount++;
        }

        const pages = Array.isArray(entry.pages)
            ? entry.pages
            : Array.isArray(entry.pages?.contents)
                ? entry.pages.contents
                : [];

        const pagePatches = {};

        const sortedPages = pages
            .map(p => typeof p.toObject === "function" ? p.toObject() : p)
            .sort((a, b) => {
                const as = Number.isFinite(a.sort) ? a.sort : 0;
                const bs = Number.isFinite(b.sort) ? b.sort : 0;
                return as - bs;
            });

        for (const page of sortedPages) {
            const pageId = page._id ?? page.id;
            if (!pageId) continue;

            const pagePatch = {};

            if (typeof page.name === "string") {
                pagePatch.name = page.name;
            }

            const pageTitle = getProperty(page, "flags.dnd5e.title");
            if (typeof pageTitle === "string") {
                pagePatch.title = pageTitle;
            }

            const text = getPageText(page);
            if (typeof text === "string" && text.trim() !== "") {
                pagePatch.text = {
                    content: text
                };
                textPageCount++;
            }

            const description = getDescription(page);
            if (typeof description === "string" && description.trim() !== "") {
                pagePatch.description = {
                    value: description
                };
            }

            if (Object.keys(pagePatch).length > 0) {
                pagePatches[pageId] = pagePatch;
                pageCount++;
            }
        }

        if (Object.keys(pagePatches).length > 0) {
            patch.pages = pagePatches;
        }

        out.entries[entryId] = patch;
        entryCount++;
    }

    console.log(`[MM2024 content export] Entries: ${entryCount}`);
    console.log(`[MM2024 content export] Pages: ${pageCount}`);
    console.log(`[MM2024 content export] Pages with text: ${textPageCount}`);
    console.log(`[MM2024 content export] Entry titles: ${titleCount}`);
    console.log(out);

    const json = JSON.stringify(out, null, 2);

    const save =
        globalThis.saveDataToFile ??
        foundry.utils.saveDataToFile;

    save(json, "application/json", OUTPUT_FILE);

    ui.notifications.info(`Exportado ${OUTPUT_FILE}`);
})();
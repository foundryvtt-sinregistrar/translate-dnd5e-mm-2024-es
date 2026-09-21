/** Translate by stable result ID, adapting legacy text to Foundry 14 fields. */
export function mm2024RollTableResultsById(source, translation) {
    if (!source || !translation || typeof translation !== "object") return source;

    const clone = (value) => globalThis.foundry?.utils?.deepClone?.(value) ?? structuredClone(value);
    const translate = (result, key) => {
        const out = typeof result?.toObject === "function" ? result.toObject() : clone(result);
        const id = out?._id ?? out?.id ?? key;
        const patch = translation[id];
        if (!out || !patch || typeof patch !== "object") return out;

        // Preserve IDs, ranges, weights and document references from the source.
        if (typeof patch.text === "string") {
            if ("name" in out || "description" in out) {
                const rich = /<\/?[a-z][\s\S]*?>/i.test(patch.text)
                    || patch.text.includes("[[") || /@\w+\[|&(?:amp;)?Reference\[/.test(patch.text);
                out.name = rich ? "" : patch.text;
                out.description = rich ? patch.text : "";
                delete out.text;
            } else {
                out.text = patch.text;
            }
        }
        // Also accept translations already using the current schema.
        for (const field of ["name", "description"]) {
            if (typeof patch[field] === "string") out[field] = patch[field];
        }
        return out;
    };

    if (Array.isArray(source)) return source.map(result => translate(result));
    if (Array.isArray(source.contents)) return source.contents.map(result => translate(result));
    if (typeof source[Symbol.iterator] === "function") return Array.from(source, result => translate(result));
    return Object.fromEntries(Object.entries(source).map(([id, result]) => [id, translate(result, id)]));
}

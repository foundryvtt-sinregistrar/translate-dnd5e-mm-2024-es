import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { mm2024RollTableResultsById as translate } from "../scripts/converters/mm2024-rollTableResultsById.js";
import { ConverterRegistry } from "../../babele/script/converter/converter-registry.js";
import { FieldMapping } from "../../babele/script/mapping/field-mapping.js";

const row = () => ({ _id: "one", name: "Original", description: "Original description",
    range: [1, 2], weight: 2, type: "document", documentUuid: "Compendium.example.actors.Actor.one" });

test("Foundry 14 translates legacy text without changing mechanics or source data", () => {
    const source = [row(), { ...row(), _id: "other" }];
    const before = structuredClone(source);
    const result = translate(source, { one: { text: "Traducido", range: [99, 99], weight: 0 } });
    assert.deepEqual(result[0], { ...row(), name: "Traducido", description: "" });
    assert.deepEqual(result[1], before[1]);
    assert.deepEqual(source, before);
});

for (const text of ["<p>Texto</p>", "Tira [[1d6]]", "@UUID[Compendium.example.actors.Actor.one]",
    "&Reference[prone]", "&amp;Reference[prone]", "@Embed[example]"]) {
    test(`rich result uses description: ${text}`, () => {
        const [result] = translate([row()], { one: { text } });
        assert.equal(result.name, "");
        assert.equal(result.description, text);
        assert.equal("text" in result, false);
    });
}

test("supports legacy results, current patches, collections and keyed results", () => {
    assert.equal(translate([{ _id: "one", text: "Original" }], { one: { text: "Traducido" } })[0].text, "Traducido");
    for (const source of [[row()], { contents: [{ toObject: row }] }, new Set([row()])]) {
        assert.deepEqual(translate(source, { one: { name: "Nombre", description: "Detalle" } }),
            [{ ...row(), name: "Nombre", description: "Detalle" }]);
    }
    assert.equal(translate({ one: { name: "Original" } }, { one: { text: "Traducido" } }).one.name, "Traducido");
});

test("all shipped table translations reach a visible Foundry 14 field", () => {
    const pack = JSON.parse(readFileSync(new URL("../compendium/dnd-monster-manual.tables.json", import.meta.url)));
    const registry = new ConverterRegistry({ mm2024RollTableResultsById: translate });
    const mapping = new FieldMapping("results", pack.mapping.results, registry);
    let count = 0;
    for (const entry of Object.values(pack.entries)) {
        for (const [id, patch] of Object.entries(entry.results ?? {})) {
            const { results: [result] } = mapping.map({ results: [{ ...row(), _id: id }] }, entry, { globalPacks: new Map(), localPacks: new Map() });
            assert.ok(result.name === patch.text || result.description === patch.text, id);
            count++;
        }
    }
    assert.ok(count > 0);
});

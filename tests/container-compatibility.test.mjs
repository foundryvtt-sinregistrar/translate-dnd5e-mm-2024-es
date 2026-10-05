import assert from "node:assert/strict";
import { test } from "node:test";

globalThis.foundry = { utils: { deepClone: structuredClone, hasProperty: () => false, setProperty() {} } };
const { mm2024AdvancementById } = await import("../scripts/converters/mm2024-advancement-by-id.js");
const { mm2024MergeEffects } = await import("../scripts/converters/mm2024-merge-effects.js");
const { mm2024ActorFullById } = await import("../scripts/converters/mm2024-actorFullById.js");

test("advancements and effects support arrays, keyed objects, and missing translations", () => {
  const advancements = { advance: { _id: "advance", name: "Feature", level: 3 } };
  assert.deepEqual(mm2024AdvancementById(advancements, { advance: { title: "Rasgo", level: 20 } }), { advance: { _id: "advance", name: "Rasgo", level: 3 } });
  assert.deepEqual(mm2024AdvancementById([{ _id: "advance", title: "Feature", level: 3 }], [{ _id: "advance", title: "Rasgo" }]), [{ _id: "advance", title: "Rasgo", level: 3 }]);
  assert.equal(mm2024AdvancementById(advancements, null), advancements);
  assert.deepEqual(mm2024MergeEffects({ effect: { _id: "effect", name: "English", changes: [{ key: "x" }] } }, { effect: { name: "Español", changes: [] } }), { effect: { _id: "effect", name: "Español", changes: [{ key: "x" }] } });
});

test("actor converter translates keyed embedded advancements", () => {
  const result = mm2024ActorFullById([{ _id: "item", system: { advancement: { advance: { _id: "advance", name: "Feature", level: 3 } } } }], { item: { advancement: { advance: { title: "Rasgo" } } } });
  assert.equal(result[0].system.advancement.advance.name, "Rasgo");
  assert.equal(result[0].system.advancement.advance.level, 3);
});

(async () => {
    const PACK_ID = "dnd-monster-manual.actors";
    const OUTPUT_FILE = "dnd-monster-manual.actors.en-source.json";

    const pack = game.packs.get(PACK_ID);

    if (!pack) {
        ui.notifications.error(`No se encontró el compendium: ${PACK_ID}`);
        console.error(`No se encontró el compendium: ${PACK_ID}`);
        return;
    }

    const getProperty = foundry.utils.getProperty;

    const getDescription = (obj) => {
        const paths = [
            "system.description.value",
            "description.value",
            "description"
        ];

        for (const path of paths) {
            const value = getProperty(obj, path);
            if (typeof value === "string" && value.trim() !== "") return value;
        }

        return undefined;
    };

    const exportEffects = (effects) => {
        const arr = Array.isArray(effects)
            ? effects
            : Array.isArray(effects?.contents)
                ? effects.contents
                : [];

        const out = {};

        for (const ef of arr) {
            const e = typeof ef.toObject === "function" ? ef.toObject() : ef;
            const id = e._id ?? e.id;
            if (!id) continue;

            const patch = {};

            if (typeof e.name === "string") patch.name = e.name;
            if (typeof e.description === "string" && e.description.trim() !== "") {
                patch.description = e.description;
            }

            if (Object.keys(patch).length > 0) out[id] = patch;
        }

        return out;
    };

    const exportActivities = (activities) => {
        if (!activities || typeof activities !== "object") return {};

        const source =
            activities instanceof Map
                ? Object.fromEntries(activities.entries())
                : activities;

        const out = {};

        for (const [id, raw] of Object.entries(source)) {
            const act = typeof raw?.toObject === "function" ? raw.toObject() : raw;
            if (!act || typeof act !== "object") continue;

            const patch = {};

            if (typeof act.name === "string") patch.name = act.name;

            const chatFlavor = getProperty(act, "description.chatFlavor");
            if (typeof chatFlavor === "string" && chatFlavor.trim() !== "") {
                patch.description = patch.description ?? {};
                patch.description.chatFlavor = chatFlavor;
            }

            const activationCondition = getProperty(act, "activation.condition");
            if (typeof activationCondition === "string" && activationCondition.trim() !== "") {
                patch.activation = patch.activation ?? {};
                patch.activation.condition = activationCondition;
            }

            const targetPrompt = getProperty(act, "target.prompt");
            if (typeof targetPrompt === "string" && targetPrompt.trim() !== "") {
                patch.target = patch.target ?? {};
                patch.target.prompt = targetPrompt;
            }

            if (Object.keys(patch).length > 0) out[id] = patch;
        }

        return out;
    };

    const exportAdvancement = (advancement) => {
        const arr = Array.isArray(advancement) ? advancement : [];
        const out = {};

        for (const adv of arr) {
            const a = typeof adv.toObject === "function" ? adv.toObject() : adv;
            const id = a._id ?? a.id;
            if (!id) continue;

            const patch = {};

            if (typeof a.title === "string" && a.title.trim() !== "") patch.title = a.title;
            if (typeof a.hint === "string" && a.hint.trim() !== "") patch.hint = a.hint;

            if (Object.keys(patch).length > 0) out[id] = patch;
        }

        return out;
    };

    const exportItems = (items) => {
        const arr = Array.isArray(items)
            ? items
            : Array.isArray(items?.contents)
                ? items.contents
                : [];

        const out = {};

        for (const raw of arr) {
            const item = typeof raw.toObject === "function" ? raw.toObject() : raw;
            const id = item._id ?? item.id;
            if (!id) continue;

            const patch = {};

            if (typeof item.name === "string") patch.name = item.name;

            const description = getDescription(item);
            if (description !== undefined) patch.description = description;

            const activities = exportActivities(getProperty(item, "system.activities"));
            if (Object.keys(activities).length > 0) patch.activities = activities;

            const effects = exportEffects(item.effects);
            if (Object.keys(effects).length > 0) patch.effects = effects;

            const advancement = exportAdvancement(getProperty(item, "system.advancement"));
            if (Object.keys(advancement).length > 0) patch.advancement = advancement;

            if (Object.keys(patch).length > 0) out[id] = patch;
        }

        return out;
    };

    const exportDetails = (actor) => {
        const details = getProperty(actor, "system.details") ?? {};
        const out = {};

        const fields = [
            "alignment",
            "eyes",
            "height",
            "faith",
            "hair",
            "weight",
            "gender",
            "skin",
            "age",
            "ideal",
            "bond",
            "flaw",
            "trait",
            "appearance"
        ];

        for (const key of fields) {
            const value = details[key];
            if (typeof value === "string" && value.trim() !== "") {
                out[key] = value;
            }
        }

        return out;
    };

    const docs = await pack.getDocuments();

    const out = {
        label: "Monstruos",
        mapping: {
            details: {
                path: "system.details",
                converter: "mm2024ActorDetails"
            },
            effects: {
                path: "effects",
                converter: "mm2024MergeEffects"
            },
            items: {
                path: "items",
                converter: "mm2024ActorFullById"
            }
        },
        folders: {},
        entries: {}
    };

    let actorCount = 0;
    let itemCount = 0;
    let activityCount = 0;
    let effectCount = 0;

    const sortedActors = docs
        .map(doc => doc.toObject())
        .sort((a, b) => {
            const an = a.name ?? "";
            const bn = b.name ?? "";
            return an.localeCompare(bn, "en", { sensitivity: "base" });
        });

    for (const actor of sortedActors) {
        const actorId = actor._id ?? actor.id;
        if (!actorId) continue;

        const patch = {};

        if (typeof actor.name === "string") patch.name = actor.name;

        const details = exportDetails(actor);
        if (Object.keys(details).length > 0) patch.details = details;

        const actorEffects = exportEffects(actor.effects);
        if (Object.keys(actorEffects).length > 0) {
            patch.effects = actorEffects;
            effectCount += Object.keys(actorEffects).length;
        }

        const items = exportItems(actor.items);
        if (Object.keys(items).length > 0) {
            patch.items = items;
            itemCount += Object.keys(items).length;

            for (const item of Object.values(items)) {
                if (item.activities) activityCount += Object.keys(item.activities).length;
                if (item.effects) effectCount += Object.keys(item.effects).length;
            }
        }

        out.entries[actorId] = patch;
        actorCount++;
    }

    console.log(`[MM2024 actors export] Actors: ${actorCount}`);
    console.log(`[MM2024 actors export] Items: ${itemCount}`);
    console.log(`[MM2024 actors export] Activities: ${activityCount}`);
    console.log(`[MM2024 actors export] Effects: ${effectCount}`);
    console.log(out);

    const json = JSON.stringify(out, null, 2);

    const save =
        globalThis.saveDataToFile ??
        foundry.utils.saveDataToFile;

    save(json, "application/json", OUTPUT_FILE);

    ui.notifications.info(`Exportado ${OUTPUT_FILE}`);
})();
(async () => {
    const PACK_ID = "dnd-monster-manual.features";
    const OUTPUT_FILE = "dnd-monster-manual.features.en-source.json";

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
            const e = typeof ef?.toObject === "function" ? ef.toObject() : ef;
            const id = e?._id ?? e?.id;
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
        const arr = Array.isArray(advancement)
            ? advancement
            : Array.isArray(advancement?.contents)
                ? advancement.contents
                : [];

        const out = {};

        for (const adv of arr) {
            const a = typeof adv?.toObject === "function" ? adv.toObject() : adv;
            const id = a?._id ?? a?.id;
            if (!id) continue;

            const patch = {};

            if (typeof a.title === "string" && a.title.trim() !== "") patch.title = a.title;
            if (typeof a.hint === "string" && a.hint.trim() !== "") patch.hint = a.hint;

            if (Object.keys(patch).length > 0) out[id] = patch;
        }

        return out;
    };

    const docs = await pack.getDocuments();

    const out = {
        label: "Rasgos",
        mapping: {
            activities: {
                path: "system.activities",
                converter: "mm2024ActivitiesById"
            },
            effects: {
                path: "effects",
                converter: "mm2024MergeEffects"
            },
            advancement: {
                path: "system.advancement",
                converter: "mm2024AdvancementById"
            }
        },
        folders: {},
        entries: {}
    };

    let featureCount = 0;
    let activityCount = 0;
    let effectCount = 0;
    let advancementCount = 0;
    let descriptionCount = 0;

    const sortedFeatures = docs
        .map(doc => doc.toObject())
        .sort((a, b) => {
            const an = a.name ?? "";
            const bn = b.name ?? "";
            return an.localeCompare(bn, "en", { sensitivity: "base" });
        });

    for (const feature of sortedFeatures) {
        const featureId = feature._id ?? feature.id;
        if (!featureId) continue;

        const patch = {};

        if (typeof feature.name === "string") patch.name = feature.name;

        const description = getDescription(feature);
        if (description !== undefined) {
            patch.description = description;
            descriptionCount++;
        }

        const activities = exportActivities(getProperty(feature, "system.activities"));
        if (Object.keys(activities).length > 0) {
            patch.activities = activities;
            activityCount += Object.keys(activities).length;
        }

        const effects = exportEffects(feature.effects);
        if (Object.keys(effects).length > 0) {
            patch.effects = effects;
            effectCount += Object.keys(effects).length;
        }

        const advancement = exportAdvancement(getProperty(feature, "system.advancement"));
        if (Object.keys(advancement).length > 0) {
            patch.advancement = advancement;
            advancementCount += Object.keys(advancement).length;
        }

        out.entries[featureId] = patch;
        featureCount++;
    }

    console.log(`[MM2024 features export] Features: ${featureCount}`);
    console.log(`[MM2024 features export] Descriptions: ${descriptionCount}`);
    console.log(`[MM2024 features export] Activities: ${activityCount}`);
    console.log(`[MM2024 features export] Effects: ${effectCount}`);
    console.log(`[MM2024 features export] Advancement: ${advancementCount}`);
    console.log(out);

    const json = JSON.stringify(out, null, 2);

    const save =
        globalThis.saveDataToFile ??
        foundry.utils.saveDataToFile;

    save(json, "application/json", OUTPUT_FILE);

    ui.notifications.info(`Exportado ${OUTPUT_FILE}`);
})();

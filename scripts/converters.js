import {mm2024MergeEffects} from "./converters/mm2024-merge-effects.js";
import {mm2024AdvancementById} from "./converters/mm2024-advancement-by-id.js";
import {mm2024JournalPagesById} from "./converters/mm2024-journalPagesById.js";
import {mm2024JournalEntryFullById} from "./converters/mm2024-journalEntryFullById.js";
import {mm2024ActorFullById} from "./converters/mm2024-actorFullById.js";
import {mm2024RollTableResultsById} from "./converters/mm2024-rollTableResultsById.js";
import {mm2024ActivitiesById} from "./converters/mm2024-activities-by-id.js";
import {mm2024ActorDetails} from "./converters/mm2024-actor-details.js";

Hooks.on("init", () => {
    const babele = game?.babele;
    if (!babele?.registerConverters) return;

    babele.registerConverters({
        mm2024ActivitiesById,
        mm2024MergeEffects,
        mm2024AdvancementById,
        mm2024JournalPagesById,
        mm2024JournalEntryFullById,
        mm2024ActorFullById,
        mm2024ActorDetails,
        mm2024RollTableResultsById
    });

    console.log(
        "[Babele - translate-dnd5e-mm-2024-es] Converters registered:",
        Object.keys(babele.converters ?? {})
    );
});
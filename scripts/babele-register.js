/**
 * Babele registration for this translation module.
 * - Registers for both "es" and "es-ES" style language codes.
 */
Hooks.on("init", () => {
  const babele = game?.babele;
  if (!babele) return;

  const current = game.i18n?.lang ?? "es";
  const base = current.split("-")[0];
  const langs = Array.from(new Set([current, base]));

    const compendium = {
        "dnd-monster-manual.content": {
            label: "MM 2024 - Contenido",
            path: "dnd-monster-manual.content.json"
        },
        "dnd-monster-manual.actors": {
            label: "MM 2024 - Monstruos",
            path: "dnd-monster-manual.actors.json"
        },
        "dnd-monster-manual.features": {
            label: "MM 2024 - Rasgos",
            path: "dnd-monster-manual.features.json"
        },
        "dnd-monster-manual.tables": {
            label: "MM 2024 - Tablas",
            path: "dnd-monster-manual.tables.json"
        }
    };

    for (const lang of langs) {
        try {
            babele.register({
                module: "translate-dnd5e-mm-2024-es",
                lang,
                dir: "compendium",
                compendium
            });

            console.log(
                `[Babele - translate-dnd5e-mm-2024-es] Registered ${Object.keys(compendium).length} compendiums for lang="${lang}" (dir=compendium)`
            );
        } catch (err) {
            console.error(
                `[Babele - translate-dnd5e-mm-2024-es] Failed registering for lang="${lang}"`,
                err
            );
        }
    }
});
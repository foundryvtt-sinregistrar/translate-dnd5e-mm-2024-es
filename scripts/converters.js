Hooks.on("init", () => {
  const babele = game?.babele;
  if (!babele?.registerConverters) return;

    babele.registerConverters({

    });

    console.log("[Babele - translate-dnd5e-mm-2024-es] Converters registered:", Object.keys(babele.converters ?? {}));
});
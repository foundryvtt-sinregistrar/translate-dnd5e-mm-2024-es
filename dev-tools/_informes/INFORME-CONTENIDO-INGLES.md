# Informe de contenido en inglés — Manual de Monstruos 2024

Fecha: 2026-09-21. Módulo: `translate-dnd5e-mm-2024-es`. Entorno indicado: Foundry VTT 14.368 y dnd5e 6.0.3.

## Corrección técnica completada (2026-09-21)

Corregido el corchete de cierre que faltaba en `compendium/dnd-monster-manual.actors.json`, ruta `entries.mmElementalCatac.items.mmCataclysmicEve.effects.NNfBNxg6PO0NlffF.description`.

La macro queda como `[[/check ability=str skill=ath format=long]]`. Se conservan sus parámetros y el texto restante. Verificado el JSON y que el único cambio en el compendio es este corchete adicional.

**La observación técnica de actores queda resuelta.** No quedan hallazgos confirmados pendientes de este informe. Las menciones posteriores a esta incidencia pendiente corresponden al historial anterior a esta corrección. No se ha comprobado el renderizado en Foundry.

## Actualización: rasgos corregidos (2026-09-21)

Se han corregido **7 campos** de `compendium/dnd-monster-manual.features.json`: los cinco hallazgos confirmados y los dos nombres editoriales `Berserk`.

- Traducidos el efecto de Espíritu animal, la condición de activación de Devastar, el nombre del efecto de Huida rencorosa y las descripciones de Tronar y Torbellino.
- La condición «se ha movido 20 pies o más» conserva el umbral y encaja en la frase que la inserta mediante `lookup`.
- Unificados el rasgo «Descontrol» y el efecto «Descontrolado» con los nombres ya usados en los actores.

**Estado actual: no quedan hallazgos confirmados pendientes de la revisión inicial de los compendios.** Los casos editoriales de rasgos también están resueltos. Las observaciones técnicas previas de actores quedan fuera de esta fase. Las secciones inferiores reflejan el historial de revisión, no nuevos pendientes.

Validación: JSON válido; exactamente 7 valores de texto modificados; estructura, macros, UUID, HTML y números conservados. La búsqueda léxica posterior no ha detectado nuevos candidatos visibles en inglés, excluidos los marcadores técnicos de la plantilla de lanzamiento de conjuros. No se ha comprobado el resultado visualmente en Foundry.

Rutas corregidas:

- `entries.mmAnimalSpirit00.effects.EaYfvxJPLJ2Ko434.description`
- `entries.mmBerserk0000000.effects.8SBNBxgUqwEyYJcK.name`
- `entries.mmBerserk0000000.name`
- `entries.mmRavage00000000.activities.Gi7NHst31Yf0KVM9.activation.condition`
- `entries.mmSpitefulEscape.effects.WP7LXEByRHwDlUE8.name`
- `entries.mmThunderclap000.description`
- `entries.mmWhirlwind00000.description`

## Actualización: contenido corregido (2026-09-21)

Se han corregido **15 campos** de `compendium/dnd-monster-manual.content.json`:

- Resueltos los dos hallazgos confirmados: nombres de la tabla de conversiones de 2014, etiqueta «dragón de oro anciano» y unidades en pies del registro de cambios.
- Localizados los títulos ingleses como «Manual de Monstruos», «Manual del Jugador» y «Guía del Dungeon Master».
- Unificados los nombres de modrones en las ilustraciones y la tabla de conversiones.

Se conservan las marcas y nombres propios (Wizards of the Coast, Foundry Virtual Tabletop, autores), la denominación «Dungeon Master» usada por el módulo y los nombres técnicos de archivos. Los casos editoriales de contenido listados en la revisión inicial quedan revisados: traducidos cuando correspondía o conservados por estos criterios.

**Estado actual: quedan 5 campos confirmados pendientes, todos en `features.json`**, además de sus casos editoriales. Las tablas de hallazgos e inventario iniciales son históricas. Las observaciones técnicas de actores siguen pendientes fuera de esta fase.

Validación: JSON válido; exactamente 15 valores de texto modificados; misma estructura, etiquetas HTML, atributos, UUID, macros y números. La búsqueda posterior no ha confirmado más restos de prosa inglesa; las coincidencias restantes corresponden a marcas o cadenas técnicas. No se ha realizado una comprobación visual en Foundry.

Rutas corregidas:

- `entries.mmArtHandouts000.pages.WykIOuhgQjo87lN1.name`
- `entries.mmArtHandouts000.pages.tYyUvYZLyr5C7u3k.name`
- `entries.mmArtHandouts000.pages.lNfr64YOHdeqMXn0.name`
- `entries.mmArtHandouts000.pages.4VYbWc8f1lZLMsrT.name`
- `entries.mmArtHandouts000.pages.rteWKEN08dVe23Gz.name`
- `entries.mmCredits0000000.pages.VpoUc0Eu4wWKZrJS.text.content`
- `entries.mmCredits0000000.pages.dtqA6TTb2PAbwRpm.text.content`
- `entries.mmMonsterManual0.pages.IJXSi0n0LwKyq6RO.text.content`
- `entries.mmMonsterManual0.pages.X1H2rUg0Z2D8BYVm.text.content`
- `entries.mmMonsterManual0.pages.YcOK2OcfuipNi24h.text.content`
- `entries.mmMonsterManual0.pages.L30mSCHBdIu0HYSW.text.content`
- `entries.mmAppendixBMonst.pages.saPG2kKobk5RjHhN.text.content`
- `entries.mmAppendixBMonst.pages.h3BTeEccSFxjFvqd.text.content`
- `entries.mmChangelog00000.name`
- `entries.mmChangelog00000.pages.3qT5PydsQbImmZC4.text.content`

## Actualización: actores corregidos (2026-09-21)

Se han traducido los **32 campos de los 18 actores** señalados en la revisión inicial de `compendium/dnd-monster-manual.actors.json`: descripciones, efectos y la condición de activación del Noble. Se han conservado los IDs, UUID, macros, parámetros de actividades y valores mecánicos. Se ha simplificado el HTML de Ataque múltiple del dragón verde anciano para recomponer correctamente la frase española.

En la comprobación posterior se ha corregido un campo adicional: `entries.mmAncientBlueDra.items.mmLightningBreat.description`, que conservaba `-pies-long, -pies-wide Line`. Total de esta fase: **33 campos corregidos en 19 actores**. La búsqueda ampliada no ha confirmado otros restos visibles en inglés.

Observación técnica fuera de esta traducción: `entries.mmElementalCatac.items.mmCataclysmicEve.effects.NNfBNxg6PO0NlffF.description` contiene una macro `[[/check ... format=long]` con un solo corchete de cierre. `long` es un parámetro técnico; se conserva y se deja su sintaxis pendiente de revisión.

**Pendientes confirmados de la revisión inicial: 7 campos** (5 en rasgos y 2 en contenido). Los 32 hallazgos de actores que aparecen más abajo se conservan como registro histórico y están **resueltos**. Los recuentos del inventario y las muestras corresponden al análisis inicial, anterior a esta corrección; no describen el estado posterior de actores. Los casos editoriales siguen separados.

Validación: JSON válido; exactamente 33 valores modificados; estructura y todas las referencias funcionales de esos valores conservadas.

## Alcance y método

Se han recorrido los **206 archivos JSON** del módulo, incluidos `compendium`, `lang`, `module.json` y los materiales de `dev-tools`. Se ha comprobado su sintaxis y examinado recursivamente sus valores de texto mediante detección de vocabulario inglés. Los candidatos de los compendios activos se han revisado en contexto y se han contrastado cadenas sin cambios con los cuatro originales `en-source.json` locales. No se han modificado las traducciones.

Se omiten de la detección las etiquetas HTML y el interior de macros `@UUID`, `@Embed`, `&Reference` y `[[...]]`; se conservan las etiquetas visibles `{...}` de enlaces. IDs, rutas, claves de objetos, nombres de conversores y parámetros técnicos no son traducciones pendientes. Los marcadores `{spell}`, `{type}`, `{ability}` y `{count}` tampoco se cuentan como prosa inglesa.

La detección es léxica, no una certificación lingüística exhaustiva. El inventario incluye todos los JSON; los candidatos de archivos históricos y auxiliares no se presentan como errores confirmados. No se ha verificado el texto que generan dinámicamente los enlaces en una sesión de Foundry ni la cobertura frente a los compendios oficiales actuales.

## Resumen inicial de los compendios activos

| Archivo | Entradas | Valores de texto | Campos con restos confirmados | IDs de entrada afectados |
| --- | ---: | ---: | ---: | ---: |
| `compendium/dnd-monster-manual.actors.json` | 504 | 11623 | 32 | 18 |
| `compendium/dnd-monster-manual.content.json` | 8 | 2164 | 2 | 2 |
| `compendium/dnd-monster-manual.features.json` | 680 | 2253 | 5 | 5 |
| `compendium/dnd-monster-manual.tables.json` | 116 | 889 | 0 | 0 |

**39 campos con restos confirmados**. Una misma entrada puede contener varios campos afectados; una misma frase puede repetirse en actores y rasgos. Los casos editoriales se cuentan aparte.

En las tablas no se han encontrado restos ingleses confirmados. `Kuo-toa`, `Kraken` y `Coyote` coinciden con el original, pero no constituyen por sí mismos traducciones pendientes. `lang/es.json` está en español.

## Hallazgos confirmados

### `compendium/dnd-monster-manual.actors.json` — 32 campos resueltos

| Ruta JSON exacta | Fragmento o explicación |
| --- | --- |
| `entries.mmAdultBrassDrag.items.mmScorchingSands.effects.n3I76HfSH6eKLALf.description` | El objetivo’s Velocidad is halved hasta el final de su siguiente turno |
| `entries.mmAdultBrassDrag.items.mmScorchingSands.description` |  , que el pueda ver a pies. Fallo: damage, and el objetivo’s Velocidad is halved hasta el final de su siguiente turno. Fallo o éxito: El no puede |
| `entries.mmAdultBronzeDra.items.mmSpellcasting00.description` | (CD de salvación de conjuros , +10 to hit with spell attacks): A voluntad: {Detectar magia} , {Saeta guía} (versión d |
| `entries.mmAdultCopperDra.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) or (B) to cast {Clavo mental} (level 4 version). |
| `entries.mmAdultCopperDra.items.mmSpellcasting00.description` | {Detectar magia} , {Clavo mental} (level 4 version), {Ilusión menor} , {Cambiar de forma} (solo forma de Bestia o H |
| `entries.mmAdultGoldDrago.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) to cast (versión de nivel 2) or (B) . |
| `entries.mmAdultRedDragon.items.mmSpellcasting00.description` | (CD de salvación de conjuros , +12 to hit with spell attacks): A voluntad: {Orden imperiosa} (versión de nivel 2), {D |
| `entries.mmAdultSilverDra.items.mmSpellcasting00.description` | (CD de salvación de conjuros , +11 to hit with spell attacks): A voluntad: {Detectar magia} , {Inmovilizar monstruo}  […] día cada uno: {Tormenta de hielo} (level 5 version), {Zona de la verdad} |
| `entries.mmAirElemental00.items.mmWhirlwind00000.description` | ue esté en el espacio del . Fallo: damage, y el objetivo es empujado hasta 20 pies en línea recta alejándo |
| `entries.mmAncientBlackDr.items.mmCloudOfInsects.description` | l pueda ver a pies o menos. Fallo: damage, y el objetivo tiene desventaja en las tiradas de salvación para |
| `entries.mmAncientBrassDr.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) or (B) para lanzar {Rayo abrasador} (versión de nivel 3). |
| `entries.mmAncientBrassDr.items.mmScorchingSands.description` |  , que el pueda ver a pies. Fallo: damage, and el objetivo’s Velocidad is halved hasta el final de su siguiente turno. Fallo o éxito: El no puede |
| `entries.mmAncientBrassDr.items.mmScorchingSands.effects.n3I76HfSH6eKLALf.description` | El objetivo’s Velocidad is halved hasta el final de su siguiente turno |
| `entries.mmAncientBronzeD.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) or (B) para lanzar Guiding Bolt (versión de nivel 2). |
| `entries.mmAncientCopperD.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) or (B) para lanzar {Clavo mental} (level 5 version). |
| `entries.mmAncientCopperD.items.mmMindJolt000000.description` | El uses to cast {Clavo mental} (level 5 version). El no puede volver a realizar esta acción hasta el inicio de s |
| `entries.mmAncientGoldDra.items.mmSpellcasting00.description` | 1/día cada uno: {Golpe flamígero} (level 6 version ) , {Palabra de regreso}, {Zona de la verdad} |
| `entries.mmAncientGoldDra.items.mmGuidingLight00.description` | El uses Spellcasting to cast {Saeta guía} (level 2 version). |
| `entries.mmAncientGreenDr.items.mmMultiattack000.description` | The makes three attacks. Puede reemplazar un ataque por un uso de Spellcasting para lanzar (level 5 version). |
| `entries.mmAncientGreenDr.items.mmMindInvasion00.description` | The dragon uses to cast (level 3 version). |
| `entries.mmAncientGreenDr.items.mmNoxiousMiasma0.description` |  point el pueda ver a pies. Fallo: damage, and el objetivo takes a −2 penalty to AC hasta el final de su siguiente turno. Fallo o éxito: El no pu |
| `entries.mmAncientRedDrag.items.mmMultiattack000.description` | reemplazar un ataque por un uso de Spellcasting para lanzar (versión de nivel 3). |
| `entries.mmAncientRedDrag.items.mmSpellcasting00.description` | ) 1/día cada uno: {Bola de fuego} (level 6 version), {Escudriñar} |
| `entries.mmAncientRedDrag.items.mmCommandingPres.description` | El uses to cast (level 2 version). El no puede volver a realizar esta acción hasta el inicio de s |
| `entries.mmAncientRedDrag.items.mmFieryRays00000.description` | El uses to cast . El no puede volver a realizar esta acción hasta el inicio de s |
| `entries.mmAncientSilverD.items.mmMultiattack000.description` | plazar un ataque por un uso de (A) or (B) Spellcasting para lanzar (versión de nivel 2). |
| `entries.mmAncientSilverD.items.mmSpellcasting00.description` | r el clima} , {Tormenta de hielo} (level 7 version), {Teletransporte} , {Zona de la verdad} |
| `entries.mmAncientSilverD.items.mmChill000000000.description` | El uses to cast . The dragon no puede volver a realizar esta acción hasta el inicio de su sig |
| `entries.mmAncientSilverD.items.mmColdGale000000.description` | e salvación de Destreza: CD , cada creature en un -pie-long, -pie-wide Line. Fallo: damage, and el objetivo is pushed up to 30 pies straight away from el . Éxito: La mitad del daño solamente. Fallo o éxito: El no pu |
| `entries.mmAnimalLord0000.items.mmAnimalSpirit00.effects.EaYfvxJPLJ2Ko434.description` | ne desventaja en tiradas de ataque and pruebas de característica hasta el final de su siguiente turno. |
| `entries.mmBloodHawk00000.items.mmBeak0000000000.description` | . , o daño si el objetivo is {Ensangrentado}. |
| `entries.mmNoble000000000.items.vyPsPLDVgeQfiZcP.activities.aLG3BRZL7P6OEjwd.activation.condition` | hit by a melee attack roll while holding a weapon |

### `compendium/dnd-monster-manual.content.json` — 2 campos resueltos

| Ruta JSON exacta | Fragmento o explicación |
| --- | --- |
| `entries.mmAppendixBMonst.pages.h3BTeEccSFxjFvqd.text.content` | Todos los monstruos del Monster Manual de 2014 aparecen en este libro o tienen un sustituto adecuado a  […] ie Dragón (if green, blue, indigo, or violet) {Dragón feérico adulto} Faerie Dragón (if red, orange, or yellow) {Dragón feérico joven} Fire Snake {Serpiente de fuego} {Espada voladora} {Espada voladora animada} Gas Spore {Hongo espora de gas} {Serpiente venenosa gigante} {Serpiente ve […] sticas de 2014 Equivalente de 2025 Half-Ogre (Ogrillon) {Ogrillón} {Veterano semidragón rojo} {Semidragón} {H […] garto} {Explorador} Hombre lagarto Shaman {Hombre lagarto geomante} Lagarto King/Queen {Hombre lagarto soberano} {Sirénido} {Sirénido experto en escara |
| `entries.mmChangelog00000.pages.3qT5PydsQbImmZC4.text.content` | Etiqueta visible {ancient gold dragon}; unidades «20 ft.» y «40 ft.». Los nombres de archivos swarm-of-insects.webp y swarm of insects.webp son técnicos. |

### `compendium/dnd-monster-manual.features.json` — 5 campos resueltos

| Ruta JSON exacta | Fragmento o explicación |
| --- | --- |
| `entries.mmAnimalSpirit00.effects.EaYfvxJPLJ2Ko434.description` | ne desventaja en tiradas de ataque and pruebas de característica hasta el final de su siguiente turno. |
| `entries.mmRavage00000000.activities.Gi7NHst31Yf0KVM9.activation.condition` | moved 20+ feet |
| `entries.mmSpitefulEscape.effects.WP7LXEByRHwDlUE8.name` | Cursed: Disadv. Checks & Saves |
| `entries.mmThunderclap000.description` | nt que el pueda ver a pies. Fallo: damage, and el objetivo tiene la condición hasta el final de su siguiente tu |
| `entries.mmWhirlwind00000.description` | ue esté en el espacio del . Fallo: damage, y el objetivo es empujado hasta 20 pies en línea recta alejándo |

### Detalle de la tabla de conversiones de monstruos

En `compendium/dnd-monster-manual.content.json`, ruta `entries.mmAppendixBMonst.pages.h3BTeEccSFxjFvqd.text.content`, quedan estos nombres o fragmentos ingleses visibles en la columna de 2014 (no son IDs de enlaces):

- `Faerie Dragón (if green, blue, indigo, or violet)` y `Faerie Dragón (if red, orange, or yellow)`.
- `Fire Snake`, `Gas Spore`, `Grick Alpha`, `Half-Ogre (Ogrillon)`.
- `Hombre lagarto Shaman`, `Lagarto King/Queen`, `Orco Eye of Gruumsh`, `Orco War Chief`.
- `Quaggoth Spore Servant`, `Sahuagin Priestess`, `Swarm of Poisonous Snakes`, `Swarm of Quippers`.
- `Young Red Dragón sombrío`, `Yuan-ti Pureblood` y la etiqueta visible `{Quipper}`.

También aparecen `Monodrone`, `Duodrone`, `Tridrone`, `Quadrone` y `Pentadrone`; conviene unificarlos con las formas españolas ya utilizadas en el módulo (monodrono, duodrono, tridrono, cuadrono, pentadrono).

## Casos de coherencia editorial

| Archivo | Ruta | Texto | Criterio |
| --- | --- | --- | --- |
| `compendium/dnd-monster-manual.content.json` | `entries.mmAppendixMonste.pages.Tnu6KW8hvlaLqaV3.text.content` |  sus presas. *Consulta la Guía del Dungeon Master. | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmAppendixMonste.pages.jHeADoGE11eL40yP.text.content` |  agua gélida. Consulta la Guía del Dungeon Master para las reglas de frío extremo y agua gélida. Penumbra glacial. | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmAppendixMonste.pages.wspNxVE4KofrKKnm.text.content` | us víctimas. *Consulta la Guía del Dungeon Master. | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmCredits0000000.pages.hX2cMPh7dAMlJEYc.text.content` | DUNGEONS & DRAGONS, D&D, Wizards of the Coast, el ampersand del dragón, Forgotten Realms, Manual del Jug […] dor, Manual de Monstruos, Guía del Dungeon Master, todos los demás nombres de productos de Wizards of the Coast, sus respectivos logotipos y El juego de rol más grande de […]  son marcas comerciales de Wizards of the Coast en EE. UU. y otros países. Todos los personajes y sus apar […] stintivas son propiedad de Wizards of the Coast. Los materiales descritos en esta declaración están proteg | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmCredits0000000.pages.VpoUc0Eu4wWKZrJS.text.content` | , Jodie Muir, Sean Murray, Hinchel Or, David Auden Nash, Nestor Ossandon Leal, Alexander Ostrowski, Al […] ión: Jefferson Dunlap Basado en el Monster Manual (2014) de Christopher Perkins (principal), Jeremy Crawford, Pete | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmCredits0000000.pages.dtqA6TTb2PAbwRpm.text.content` | El Monster Manual 2024 para Foundry Virtual Tabletop fue producido por un grupo de […] : Shane Martland Socios en Wizards of the Coast La creación de este libro fuente no habría sido posible si […] s contactos principales en Wizards of the Coast, que nos ayudaron a conseguir ilustraciones, impulsaron qu | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmMonsterManual0.pages.IJXSi0n0LwKyq6RO.text.content` | idas de D&D. Junto con el Player's Handbook (2024) y la Dungeon Master's Guide (2024), el Monster Manual forma parte de los fundamentos de D&D y requiere esos libros. Es […] uos y creación de encuentros de la Dungeon Master's Guide — para construir tus propias aventuras. Consulta el apén […] 25? Esta es la versión de 2025 del Monster Manual de la quinta edición. Si has leído la versión de 2014, gran part […] s de monstruos que aparecían en la Dungeon Master’s Guide de 2014. Todos los monstruos del Monster Manual de 2014 aparecen en este libro o tienen un reemplazo apropiado p | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmMonsterManual0.pages.X1H2rUg0Z2D8BYVm.text.content` | dicadas además de las del Player's Handbook . Acciones adicionales. Esta sección proporciona las acciones ad | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmMonsterManual0.pages.YcOK2OcfuipNi24h.text.content` | s mágicos con el tema indicado. La Dungeon Master's Guide detalla tesoros acumulados apropiados para cada tema. Ni […] o de su bloque de estadísticas. La Dungeon Master's Guide proporciona más información sobre el tesoro de los monst | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmMonsterManual0.pages.L30mSCHBdIu0HYSW.text.content` | el glosario de reglas del Player's Handbook y en esta sección. Tamaño Un monstruo es Diminuto, Pequeño, Medi […] sas opciones. Consulta el Player's Handbook para obtener información sobre el tamaño. Tipo de criatura Cada  […] s otros alineamientos. El Player's Handbook describe los nueve alineamientos y las criaturas sin alineamient […] ras defensas. Consulta el Player's Handbook para obtener información sobre la Clase de Armadura. Iniciativa  | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmAppendixBMonst.pages.saPG2kKobk5RjHhN.text.content` | dísticas que han cambiado entre el Monster Manual de 2014 y este libro, así como listas de monstruos organizadas p | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.content.json` | `entries.mmChangelog00000.name` | Registro de cambios del Monster Manual | Títulos de libros o denominación DM: revisión de coherencia editorial, separada de prosa sin traducir. |
| `compendium/dnd-monster-manual.features.json` | `entries.mmBerserk0000000.effects.8SBNBxgUqwEyYJcK.name` | Berserk | Terminología: valorar «Frenesí» y unificar con actores. |
| `compendium/dnd-monster-manual.features.json` | `entries.mmBerserk0000000.name` | Berserk | Terminología: valorar «Frenesí» y unificar con actores. |

Los nombres de autores, marcas como Wizards of the Coast y Foundry Virtual Tabletop, y nombres propios de criaturas como Aboleth, Balor, Kraken o Yeti no se clasifican automáticamente como fallos. `Neutral`, `Invisible`, `Noble`, `Solar` y `Necrosis` son coincidencias válidas con el español. El verbo español «uses» y «has» no debe traducirse por una coincidencia léxica inglesa.

## Otros JSON del módulo

- `module.json`: `title` = `D&D 5e MM 2024 Spanish Translation (Babele)` y `description` = `Spanish translation for the official D&D 5e Monster Manual 2024 using Babele.` Son metadatos visibles en inglés; localización opcional, independiente de los compendios. `languages.0.name = English` es la denominación del idioma inglés.
- `lang/en.json`: los dos textos están en inglés deliberadamente; no traducir este archivo al español.
- `dev-tools/export/data/**/en/*.en-source.json`: cuatro originales ingleses usados como referencia; conservar.
- `dev-tools/export/data/**/es/*.json`: instantáneas, parches e informes históricos. Hay candidatos ingleses en varias versiones; no son archivos registrados por Babele. Consultar el inventario antes de reutilizarlos para evitar reintroducir traducciones incompletas.
- `dev-tools/IA-ChatGPT/*.json`: glosarios, diccionarios bilingües y reglas de normalización. Las expresiones inglesas de origen son parte de su función.
- `dev-tools/pdf-audit/*.json` y `reports/*.json`: terminología, diferencias técnicas e informes de auditoría. Su inglés no implica necesariamente texto visible pendiente en el módulo.

## Prioridades recomendadas

1. Completar las descripciones mixtas de dragones y sus efectos: `is halved`, `uses … to cast`, `level … version`, `to hit with spell attacks`, `Spellcasting`, `damage, and`, etc.
2. Traducir las condiciones de activación de Noble y Ravage y el efecto `Cursed: Disadv. Checks & Saves`.
3. Corregir las etiquetas de la tabla de conversiones y del registro de cambios, manteniendo los UUID originales.
4. Unificar nombres editoriales y terminología; actualizar únicamente las fuentes históricas que vayan a reutilizarse.
5. Repetir la revisión y comprobar el resultado en Foundry después de traducir.

## Inventario completo de JSON

Archivos válidos: **206 / 206**. «Candidatos» cuenta valores de texto que activan el detector, no palabras, errores confirmados ni entradas únicas. Puede incluir marcas, texto de referencia y falsos positivos; cero significa sin coincidencias con este detector.

| Archivo relativo al módulo | Valores de texto | Candidatos | Estado |
| --- | ---: | ---: | --- |
| `compendium/dnd-monster-manual.actors.json` | 11623 | 36 | JSON válido |
| `compendium/dnd-monster-manual.content.json` | 2164 | 16 | JSON válido |
| `compendium/dnd-monster-manual.features.json` | 2253 | 10 | JSON válido |
| `compendium/dnd-monster-manual.tables.json` | 889 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/en/dnd-monster-manual.actors.en-source.json` | 12254 | 5087 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v1-names-and-alignments.json` | 6132 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v10-bulette-to-chain-devil-descriptions.json` | 7348 | 68 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v11-chasme-to-cockatrice-regent-descriptions.json` | 7435 | 70 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v12-colossus-to-cultist-hierophant-descriptions.json` | 7504 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v13-cyclops-oracle-to-death-knight-descriptions.json` | 7607 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v14-death-knight-aspirant-to-djinni-descriptions.json` | 7746 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v15-doppelganger-to-dryad-descriptions.json` | 7842 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v16-dust-mephit-to-empyrean-descriptions.json` | 7974 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v17-erinyes-to-flumph.json` | 8085 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v17-erinyes-to-flumph.patch.json` | 190 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v18-flying-snake-to-ghast-gravecaller.json` | 8149 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v18-flying-snake-to-ghast-gravecaller.patch.json` | 136 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v18-flying-snake-to-ghast-gravecaller.report.json` | 15 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v19-ghost-to-giant-crab.json` | 8193 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v19-ghost-to-giant-crab.patch.json` | 116 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v19-ghost-to-giant-crab.report.json` | 30 | 5 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v2-aarakocra-to-aboleth-descriptions.json` | 6187 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v20-giant-crocodile-to-giant-owl.json` | 8230 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v20-giant-crocodile-to-giant-owl.patch.json` | 115 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v20-giant-crocodile-to-giant-owl.report.json` | 17 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.json` | 8285 | 71 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.patch.json` | 122 | 1 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.report.json` | 14 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.json` | 8445 | 72 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.patch.json` | 331 | 1 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.report.json` | 19 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v23-gladiator-to-goblin-warrior.json` | 8527 | 72 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v23-gladiator-to-goblin-warrior.patch.json` | 178 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v23-gladiator-to-goblin-warrior.report.json` | 20 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.json` | 8665 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.patch.json` | 318 | 2 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.report.json` | 19 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v25-grick-to-harpy.json` | 8740 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v25-grick-to-harpy.patch.json` | 163 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v25-grick-to-harpy.report.json` | 20 | 5 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v26-haunting-revenant-to-hobgoblin-warlord.json` | 8813 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v26-haunting-revenant-to-hobgoblin-warlord.patch.json` | 149 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v26-haunting-revenant-to-hobgoblin-warlord.report.json` | 16 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v27-hobgoblin-warrior-to-imp.json` | 8894 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v27-hobgoblin-warrior-to-imp.patch.json` | 151 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v27-hobgoblin-warrior-to-imp.report.json` | 13 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v28-incubus-to-knight.json` | 8995 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v28-incubus-to-knight.patch.json` | 193 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v28-incubus-to-knight.report.json` | 19 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v29-kobold-warrior-to-lemure.json` | 9132 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v29-kobold-warrior-to-lemure.patch.json` | 274 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v29-kobold-warrior-to-lemure.report.json` | 19 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v3-abominable-yeti-to-adult-blue-dragon-descriptions.json` | 6233 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v30-lich-to-m (1).json` | 313 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v30-lich-to-m (2).json` | 19 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v30-lich-to-mammo.json` | 9258 | 74 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to- (1).json` | 240 | 2 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to- (2).json` | 30 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to-merr.json` | 9373 | 76 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v32-mezzoloth-to-.json` | 9486 | 76 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v32-mezzoloth-to-modron-quadrone.patch.json` | 245 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v32-mezzoloth-to-modron-quadrone.report.json` | 26 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v33-modron-tridrone-to-nalfeshnee.json` | 9583 | 76 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v33-modron-tridrone-to-nalfeshnee.patch.json` | 201 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v33-modron-tridrone-to-nalfeshnee.report.json` | 19 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.json` | 9701 | 82 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.patch.json` | 261 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.report.json` | 26 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v35-ogre-zombie-to-performer-legend.json` | 9776 | 82 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v35-ogre-zombie-to-performer-legend.patch.json` | 169 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v35-ogre-zombie-to-performer-legend.report.json` | 20 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-mae.json` | 9901 | 84 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-maestro-to-pixie.patch.json` | 244 | 2 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-maestro-to-pixie.report.json` | 27 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.json` | 10053 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.patch.json` | 311 | 9 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.report.json` | 18 | 5 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v38-psychic-gray-ooze-to-raven.json` | 10153 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v38-psychic-gray-ooze-to-raven.patch.json` | 232 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v38-psychic-gray-ooze-to-raven.report.json` | 16 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.json` | 10226 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.patch.json` | 155 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.report.json` | 16 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v4-adult-brass-to-adult-white-dragon-descriptions.json` | 6386 | 15 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v40-saber-toothed-tiger-to-scarecrow.json` | 10322 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v40-saber-toothed-tiger-to-scarecrow.patch.json` | 190 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v40-saber-toothed-tiger-to-scarecrow.report.json` | 16 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v41-scorpion-to-shield-guardian.json` | 10438 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v41-scorpion-to-shield-guardian.patch.json` | 226 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v41-scorpion-to-shield-guardian.report.json` | 14 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.json` | 10584 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.patch.json` | 307 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.report.json` | 41 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v43-sphinx-of-valor-to-stirge.json` | 10701 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v43-sphinx-of-valor-to-stirge.patch.json` | 232 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v43-sphinx-of-valor-to-stirge.report.json` | 29 | 4 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v44-stone-giant-to-swarm-of-lemures.json` | 10794 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v44-stone-giant-to-swarm-of-lemures.patch.json` | 181 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v44-stone-giant-to-swarm-of-lemures.report.json` | 28 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v45-swarm-of-pira.json` | 10886 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v45-swarm-of-piranhas-to-tough.patch.json` | 184 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v45-swarm-of-piranhas-to-tough.report.json` | 15 | 2 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v46-tough-boss-to-ultroloth.json` | 10996 | 93 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v46-tough-boss-to-ultroloth.patch.json` | 222 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v46-tough-boss-to-ultroloth.report.json` | 16 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v47-umber-hulk-to-violet-fungus.json` | 11153 | 94 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v47-umber-hulk-to-violet-fungus.patch.json` | 295 | 1 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v47-umber-hulk-to-violet-fungus.report.json` | 24 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v48-violet-fungus-necrohulk-to-water-weird.json` | 11237 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v48-violet-fungus-necrohulk-to-water-weird.patch.json` | 157 | 1 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v48-violet-fungus-necrohulk-to-water-weird.report.json` | 23 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v49-weasel-to-winged-kobold.json` | 11352 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v49-weasel-to-winged-kobold.patch.json` | 194 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v49-weasel-to-winged-kobold.report.json` | 84 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v5-air-elemental-to-animated-armor-descriptions.json` | 6647 | 64 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.json` | 11433 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.patch.json` | 170 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.report.json` | 28 | 4 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.json` | 11508 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.patch.json` | 175 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.report.json` | 30 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-final-general-review.report.json` | 2046 | 61 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie (1).json` | 11567 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.json` | 11567 | 95 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.patch (1).json` | 130 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.patch.json` | 130 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.report (1).json` | 14 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.report.json` | 14 | 3 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v53-applied.json` | 11623 | 76 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v53-applied.report.json` | 7 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v6-animated-boulder-to-archmage-descriptions.json` | 6836 | 67 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v7-archpriest-to-bandit-captain-descriptions.json` | 6945 | 67 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v8-bandit-crime-lord-to-zombie-beholder-descriptions.json` | 7089 | 67 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v9-berserker-to-bugbear-warrior-descriptions.json` | 7255 | 68 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/en/dnd-monster-manual.content.en-source.json` | 2164 | 725 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.appendix-a.v1.json` | 200 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v10-appendix-monster-details-azers-to-beholder-lairs.json` | 2164 | 499 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v11-appendix-monster-details-berserkers-to-blob.json` | 2164 | 481 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v12-appendix-monster-details-blue-dragons-to-bone-naga.json` | 2164 | 473 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v13-appendix-monster-details-brass-to-bronze-dragons.json` | 2164 | 461 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v14-appendix-monster-details-bugbe.json` | 2164 | 451 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v15-appendix-monster-details-carrion-crawler-to-chain-devil.json` | 2164 | 446 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v16-appendix-monster-details-chasme-to-couatl.json` | 2164 | 428 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v17-appendix-monster-details-crawling-claws-to-fiend-cultists.json` | 2164 | 414 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v18-appendix-monster-details-cyclo.json` | 2164 | 403 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v19-appendix-monster-details-demilich-to-dracolich-lairs.json` | 2164 | 395 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v2-how-to-.json` | 209 | 4 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v20-appendix-monster-details-drago.json` | 2164 | 382 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v21-appendix-monster-details-erinyes-to-flameskull.json` | 2164 | 373 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v22-appendix-monster-details-flesh.json` | 2164 | 362 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v23-appendix-monster-details-gargoyle-to-ghost.json` | 2164 | 355 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v24-appendix-monster-details-ghouls-to-gith-adventures.json` | 2164 | 341 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v25-appendix-monster-details-glabrezu-to-goblins.json` | 2164 | 329 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v26-appendix-monster-details-gold-dragons-to-psychic-gray-ooze.json` | 2164 | 316 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v27-appendix-monster-details-green-dragons-to-guards.json` | 2164 | 299 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v28-appendix-monster-details-half-dragon-to-incubus.json` | 2164 | 280 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v29-appendix-monster-details-intel.json` | 2164 | 269 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v3-appendi.json` | 283 | 6 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v30-appendix-monster-details-krake.json` | 2164 | 250 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v31-appendix-monster-details-lizardfolk-to-medusa.json` | 2164 | 235 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v32-appendix-monster-details-mephits-to-mind-flayer-arcanist.json` | 2164 | 218 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v33-appendix-monster-details-minotaur-of-baphomet-to-mummy-lor.json` | 2164 | 206 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v34-appendix-monster-details-myconids-to-nightmare.json` | 2164 | 198 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v35-appendix-monster-details-nobles-to-ochre-jelly.json` | 2164 | 192 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v36-appendix-monster-details-ogres-to-pirate-flags.json` | 2164 | 171 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v37-appendix-monster-details-pit-fiend-to-archpriest.json` | 2164 | 161 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v38-appendix-monster-details-pseudodragon-to-red-dragon-lairs.json` | 2164 | 148 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v39-appendix-monster-details-remorhazes-to-sahuagin.json` | 2164 | 135 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v4-credits.json` | 290 | 10 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v40-appendix-monster-details-salamanders-to-scouts.json` | 2164 | 124 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v41-appendix-monster-details-sea-hag-to-flaming-skeleton.json` | 2164 | 106 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v42-appendix-monster-details-slaadi-to-sphinx-lairs.json` | 2164 | 90 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v43-appendix-monster-details-spies-to-stirges.json` | 2164 | 81 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v44-appendix-monster-details-stone-giant-to-tarrasque.json` | 2164 | 76 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v45-appendix-monster-details-thri-kreen-to-unicorn-lairs.json` | 2164 | 63 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v46-appendix-monster-details-vampires-to-water-elemental.json` | 2164 | 50 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v47-appendix-monster-details-water-weird-to-yochlol.json` | 2164 | 27 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v48-appendix-monster-details-yuan-ti-to-zombie-beholder.json` | 2164 | 19 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v49-global-review.json` | 2164 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v5-changelog.json` | 300 | 14 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v6-art-handouts.json` | 622 | 14 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v7-monster.json` | 1117 | 14 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v8-appendix-monster-details.json` | 2164 | 537 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v9-appendix-monster-details-a-to-axe-beaks.json` | 2164 | 516 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/en/dnd-monster-manual.features.en-source.json` | 2712 | 1123 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v1-seed-from-actors.json` | 5991 | 41 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v2-align.json` | 1933 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v3-consu.json` | 2018 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v4-glare.json` | 2113 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v5-paral.json` | 2209 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v6-final.json` | 2253 | 16 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/en/dnd-monster-manual.tables.en-source.json` | 889 | 603 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/es/dnd-monster-manual.tables.es.v1-aboleth-to-flameskull.json` | 249 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/es/dnd-monster-manual.tables.es.v2-fle.json` | 499 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/es/dnd-monster-manual.tables.es.v3-mag.json` | 749 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/es/dnd-monster-manual.tables.es.v4-final-complete.json` | 889 | 0 | JSON válido |
| `dev-tools/export/data/dnd-monster-manual.tables/es/dnd-monster-manual.tables.ready.json` | 889 | 0 | JSON válido |
| `dev-tools/IA-ChatGPT/glossary_unified.json` | 1391 | 0 | JSON válido |
| `dev-tools/IA-ChatGPT/normalization_core.v7.generated.integrated.json` | 700 | 18 | JSON válido |
| `dev-tools/IA-ChatGPT/phb_en_es_group_dictionaries.json` | 68 | 2 | JSON válido |
| `dev-tools/pdf-audit/official-terms.es.json` | 29 | 0 | JSON válido |
| `dev-tools/pdf-audit/reports/mm-pdf-audit.json` | 339 | 7 | JSON válido |
| `dev-tools/pdf-audit/reviewed-command-differences.json` | 83 | 0 | JSON válido |
| `lang/en.json` | 2 | 1 | JSON válido |
| `lang/es.json` | 2 | 0 | JSON válido |
| `module.json` | 32 | 1 | JSON válido |

## Muestras de candidatos en materiales auxiliares

Una muestra por archivo auxiliar con coincidencias, para localizar el material. Estos casos no han recibido la misma confirmación individual que los hallazgos de los compendios activos.

| Archivo | Primera ruta candidata | Muestra |
| --- | --- | --- |
| `dev-tools/export/data/dnd-monster-manual.actors/en/dnd-monster-manual.actors.en-source.json` | `entries.mmAarakocraAerom.items.mmWindStaff00000.description` | Melee or Ranged Attack Roll: , reach ft. or range ft. Hit: damage. |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v10-bulette-to-chain-devil-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v11-chasme-to-cockatrice-regent-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v12-colossus-to-cultist-hierophant-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v13-cyclops-oracle-to-death-knight-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v14-death-knight-aspirant-to-djinni-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v15-doppelganger-to-dryad-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v16-dust-mephit-to-empyrean-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v17-erinyes-to-flumph.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v18-flying-snake-to-ghast-gravecaller.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v18-flying-snake-to-ghast-gravecaller.report.json` | `applied_previous_patch` | nster-manual.actors.es.v17-erinyes-to-flumph.patch.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v19-ghost-to-giant-crab.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v19-ghost-to-giant-crab.report.json` | `base` | -manual.actors.es.v18-flying-snake-to-ghast-gravecaller.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v20-giant-crocodile-to-giant-owl.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v20-giant-crocodile-to-giant-owl.report.json` | `source_base` | monster-manual.actors.es.v19-ghost-to-giant-crab.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.patch.json` | `_meta.base` | nual.actors.es.v20-giant-crocodile-to-giant-owl.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v21-giant-rat-to-giant-wasp.report.json` | `base` | nual.actors.es.v20-giant-crocodile-to-giant-owl.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.patch.json` | `entries.mmGlabrezu000000.items.o9zHpjCrGZEcIJzZ.description` | l nivel del espacio de conjuro que uses. |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v22-giant-weasel-to-glabrezu.report.json` | `base_file` | ter-manual.actors.es.v21-giant-rat-to-giant-wasp.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v23-gladiator-to-goblin-warrior.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v23-gladiator-to-goblin-warrior.report.json` | `base` | -manual.actors.es.v22-giant-weasel-to-glabrezu.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.patch.json` | `entries.mmGoldDragonWyrm.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de Cono. Fallo: de daño. Éxito: La mitad del daño. |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.report.json` | `base` | ter-manual.actors.es.v23-gladiator-to-goblin-warrior.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v25-grick-to-harpy.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v25-grick-to-harpy.report.json` | `base_file` | -monster-manual.actors.es.v24-gold-dragon-wyrmling-to-grell.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v26-haunting-revenant-to-hobgoblin-warlord.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v26-haunting-revenant-to-hobgoblin-warlord.report.json` | `base_file` | monster-manual.actors.es.v25-grick-to-harpy.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v27-hobgoblin-warrior-to-imp.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v28-incubus-to-knight.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v28-incubus-to-knight.report.json` | `base` | al.actors.es.v27-hobgoblin-warrior-to-imp.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v29-kobold-warrior-to-lemure.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v29-kobold-warrior-to-lemure.report.json` | `base` | nster-manual.actors.es.v28-incubus-to-knight.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v30-lich-to-m (2).json` | `base` | anual.actors.es.v29-kobold-warrior-to-lemure.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v30-lich-to-mammo.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to- (1).json` | `entries.mmMarid000000000.items.R7FNJUssksG8Ycmx.description` | Until el conjuro ends, you control any water inside an area you choose that is a Cube up to 100 pies on a side, using one of the following effects. As a acción mágica on your later |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to- (2).json` | `source_base` | -monster-manual.actors.es.v30-lich-to-mammoth.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v31-manes-to-merr.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v32-mezzoloth-to-.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v32-mezzoloth-to-modron-quadrone.report.json` | `source` | monster-manual.actors.es.v31-manes-to-merrow.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v33-modron-tridrone-to-nalfeshnee.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v33-modron-tridrone-to-nalfeshnee.report.json` | `base` | ter-manual.actors.es.v32-mezzoloth-to-modron-quadrone.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.patch.json` | `entries.mmNightHag000000.items.YL2yDZHhJnpRigTh.effects.4k92Sjfpcm5bnguO.description` | The target has Desventaja on pruebas de característica and tirada de ataques for the duration. For the duration, the target makes a tirada de salvación at the end of each of its tu |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v34-needle-blight-to-ogre.report.json` | `base` | nual.actors.es.v33-modron-tridrone-to-nalfeshnee.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v35-ogre-zombie-to-performer-legend.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v35-ogre-zombie-to-performer-legend.report.json` | `base_file` | manual.actors.es.v34-needle-blight-to-ogre.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-mae.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-maestro-to-pixie.patch.json` | `entries.mmPirateAdmiral0.items.mmDefensiveStanc.description` | e Armadura de esta criatura cuando uses la reacción. Puedes activar el AE en la pestaña de efectos de la |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v36-performer-maestro-to-pixie.report.json` | `source_base` | r-manual.actors.es.v35-ogre-zombie-to-performer-legend.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.patch.json` | `entries.mmPlanetar000000.items.LcdboPtDut4HQJfr.description` | You take control of the weather within 5 miles of you for the duration. You must be outdoors to cast this spell, and it ends early if you go indoors. When you cast the spell, you c |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v37-pixie-wonderbringer-to-pseudodragon.report.json` | `source` | al.actors.es.v36-performer-maestro-to-pixie.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v38-psychic-gray-ooze-to-raven.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v38-psychic-gray-ooze-to-raven.report.json` | `notes.0` | Generated from v37 cumulative JSON. |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.report.json` | `base` | al.actors.es.v38-psychic-gray-ooze-to-raven.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v4-adult-brass-to-adult-white-dragon-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v40-saber-toothed-tiger-to-scarecrow.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v40-saber-toothed-tiger-to-scarecrow.report.json` | `base` | d-monster-manual.actors.es.v39-red-dragon-wyrmling-to-rust-monster.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v41-scorpion-to-shield-guardian.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v41-scorpion-to-shield-guardian.report.json` | `source_base` | .actors.es.v40-saber-toothed-tiger-to-scarecrow.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.report.json` | `base_file` | ster-manual.actors.es.v41-scorpion-to-shield-guardian.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v43-sphinx-of-valor-to-stirge.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v43-sphinx-of-valor-to-stirge.report.json` | `base` | nual.actors.es.v42-shrieker-fungus-to-sphinx-of-secrets.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v44-stone-giant-to-swarm-of-lemures.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v44-stone-giant-to-swarm-of-lemures.report.json` | `base` | onster-manual.actors.es.v43-sphinx-of-valor-to-stirge.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v45-swarm-of-pira.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v45-swarm-of-piranhas-to-tough.report.json` | `notes.0` | Generated cumulatively from v44. |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v46-tough-boss-to-ultroloth.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v46-tough-boss-to-ultroloth.report.json` | `source` | monster-manual.actors.es.v45-swarm-of-piranhas-to-tough.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v47-umber-hulk-to-violet-fungus.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v47-umber-hulk-to-violet-fungus.patch.json` | `entries.mmUnicorn0000000.items.tqXlS6FGdENkOvOt.description` | You and up to five willing creatures a 5 pies of you instantly teleport to a previously designated sanctuary. You and any creatures that teleport with you appear in the nearest uno |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v48-violet-fungus-necrohulk-to-water-weird.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v48-violet-fungus-necrohulk-to-water-weird.patch.json` | `entries.mmWarriorCommand.items.mmCounterattack0.description` | e armadura de esta criatura cuando uses la reacción. Puedes activar el AE en la pestaña de efectos de la |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v49-weasel-to-winged-kobold.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v49-weasel-to-winged-kobold.report.json` | `generic_descriptions_preserved.1.source_name` | Handaxe (Humanoid or Hybrid Form Only) |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v5-air-elemental-to-animated-armor-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.report.json` | `base` | onster-manual.actors.es.v49-weasel-to-winged-kobold.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.report.json` | `base` | r-manual.actors.es.v50-winter-wolf-to-young-blue-dragon.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-final-general-review.report.json` | `meta.file` | .actors.es.v52-yuan-ti-infiltrator-to-zombie.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie (1).json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.report (1).json` | `source` | r-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v52-yuan-ti-infiltrator-to-zombie.report.json` | `source` | r-manual.actors.es.v51-young-brass-dragon-to-yuan-ti-abomination.json |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v53-applied.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v6-animated-boulder-to-archmage-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v7-archpriest-to-bandit-captain-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v8-bandit-crime-lord-to-zombie-beholder-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.actors/es/dnd-monster-manual.actors.es.v9-berserker-to-bugbear-warrior-descriptions.json` | `entries.mmAdultBrassDrag.items.mmFireBreath0000.description` | ada de salvación de Destreza: DC , each en un -pies de largo y -pies de ancho. Fallo: de daño. Éxito: La |
| `dev-tools/export/data/dnd-monster-manual.content/en/dnd-monster-manual.content.en-source.json` | `entries.mmAppendixAAnima.pages.CTjWCCwtyafG0uqR.text.content` | Fantastic Animals The following stat blocks in this appendix represent fantastical versions of real-world animals: {Blood Hawk}: Excessively aggressive hawklik […] ged, venomous sn |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v10-appendix-monster-details-azers-to-beholder-lairs.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v11-appendix-monster-details-berserkers-to-blob.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v12-appendix-monster-details-blue-dragons-to-bone-naga.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v13-appendix-monster-details-brass-to-bronze-dragons.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v14-appendix-monster-details-bugbe.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v15-appendix-monster-details-carrion-crawler-to-chain-devil.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v16-appendix-monster-details-chasme-to-couatl.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v17-appendix-monster-details-crawling-claws-to-fiend-cultists.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v18-appendix-monster-details-cyclo.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v19-appendix-monster-details-demilich-to-dracolich-lairs.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v2-how-to-.json` | `entries.mmMonsterManual0.pages.IJXSi0n0LwKyq6RO.text.content` | idas de D&D. Junto con el Player's Handbook (2024) y la Dungeon Master's Guide (2024), el Monster Manual forma parte de los fundamentos de D&D y requiere esos libros. Es […] uos y  |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v20-appendix-monster-details-drago.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v21-appendix-monster-details-erinyes-to-flameskull.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v22-appendix-monster-details-flesh.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v23-appendix-monster-details-gargoyle-to-ghost.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v24-appendix-monster-details-ghouls-to-gith-adventures.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v25-appendix-monster-details-glabrezu-to-goblins.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v26-appendix-monster-details-gold-dragons-to-psychic-gray-ooze.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v27-appendix-monster-details-green-dragons-to-guards.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v28-appendix-monster-details-half-dragon-to-incubus.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v29-appendix-monster-details-intel.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v3-appendi.json` | `entries.mmMonsterManual0.pages.IJXSi0n0LwKyq6RO.text.content` | idas de D&D. Junto con el Player's Handbook (2024) y la Dungeon Master's Guide (2024), el Monster Manual forma parte de los fundamentos de D&D y requiere esos libros. Es […] uos y  |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v30-appendix-monster-details-krake.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v31-appendix-monster-details-lizardfolk-to-medusa.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v32-appendix-monster-details-mephits-to-mind-flayer-arcanist.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v33-appendix-monster-details-minotaur-of-baphomet-to-mummy-lor.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v34-appendix-monster-details-myconids-to-nightmare.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v35-appendix-monster-details-nobles-to-ochre-jelly.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v36-appendix-monster-details-ogres-to-pirate-flags.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v37-appendix-monster-details-pit-fiend-to-archpriest.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v38-appendix-monster-details-pseudodragon-to-red-dragon-lairs.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v39-appendix-monster-details-remorhazes-to-sahuagin.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v4-credits.json` | `entries.mmCredits0000000.pages.hX2cMPh7dAMlJEYc.text.content` | DUNGEONS & DRAGONS, D&D, Wizards of the Coast, el ampersand del dragón, Forgotten Realms, Manual del Jug […] dor, Manual de Monstruos, Guía del Dungeon Master, todos los demás nomb |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v40-appendix-monster-details-salamanders-to-scouts.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v41-appendix-monster-details-sea-hag-to-flaming-skeleton.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v42-appendix-monster-details-slaadi-to-sphinx-lairs.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v43-appendix-monster-details-spies-to-stirges.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v44-appendix-monster-details-stone-giant-to-tarrasque.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v45-appendix-monster-details-thri-kreen-to-unicorn-lairs.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v46-appendix-monster-details-vampires-to-water-elemental.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v47-appendix-monster-details-water-weird-to-yochlol.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v48-appendix-monster-details-yuan-ti-to-zombie-beholder.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v49-global-review.json` | `entries.mmAppendixMonste.pages.Tnu6KW8hvlaLqaV3.text.content` |  sus presas. *Consulta la Guía del Dungeon Master. |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v5-changelog.json` | `entries.mmCredits0000000.pages.hX2cMPh7dAMlJEYc.text.content` | DUNGEONS & DRAGONS, D&D, Wizards of the Coast, el ampersand del dragón, Forgotten Realms, Manual del Jug […] dor, Manual de Monstruos, Guía del Dungeon Master, todos los demás nomb |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v6-art-handouts.json` | `entries.mmCredits0000000.pages.hX2cMPh7dAMlJEYc.text.content` | DUNGEONS & DRAGONS, D&D, Wizards of the Coast, el ampersand del dragón, Forgotten Realms, Manual del Jug […] dor, Manual de Monstruos, Guía del Dungeon Master, todos los demás nomb |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v7-monster.json` | `entries.mmCredits0000000.pages.hX2cMPh7dAMlJEYc.text.content` | DUNGEONS & DRAGONS, D&D, Wizards of the Coast, el ampersand del dragón, Forgotten Realms, Manual del Jug […] dor, Manual de Monstruos, Guía del Dungeon Master, todos los demás nomb |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v8-appendix-monster-details.json` | `entries.mmAppendixMonste.pages.1AB1kcMsMnE3ucAr.text.content` | Instrumentos, Individual Aarakocra are birdlike folk who soar the skies of countless worlds and the endless expanses of the Plano Elemental del Aire. They often resemble avians com |
| `dev-tools/export/data/dnd-monster-manual.content/es/dnd-monster-manual.content.es.v9-appendix-monster-details-a-to-axe-beaks.json` | `entries.mmAppendixMonste.pages.kB9xuOKJSZ9Dnp98.text.content` | Alone or in small groups, axe beaks stalk prey to feed their flocks. When working together, axe beaks use rudimentary tactics, with some distracting threats while others strike vul |
| `dev-tools/export/data/dnd-monster-manual.features/en/dnd-monster-manual.features.en-source.json` | `entries.mmAbduct00000000.description` | The needn’t spend extra movement to move a creature it is grappling. |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v1-seed-from-actors.json` | `entries.8fyeR6xiLPhR9TgR.description` | You and up to five willing creatures a 5 pies of you instantly teleport to a previously designated sanctuary. You and any creatures that teleport with you appear in the nearest uno |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v2-align.json` | `entries.mmAnimalSpirit00.description` | The conjures an animal spirit that strikes at a creature and then disappears. Tirada de salvación de Destreza: DC , una criat […] ra que el pueda ver a pies. Fallo: damage. Éxito:  |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v3-consu.json` | `entries.mmAnimalSpirit00.description` | The conjures an animal spirit that strikes at a creature and then disappears. Tirada de salvación de Destreza: DC , una criat […] ra que el pueda ver a pies. Fallo: damage. Éxito:  |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v4-glare.json` | `entries.mmAnimalSpirit00.description` | The conjures an animal spirit that strikes at a creature and then disappears. Tirada de salvación de Destreza: DC , una criat […] ra que el pueda ver a pies. Fallo: damage. Éxito:  |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v5-paral.json` | `entries.mmAnimalSpirit00.description` | The conjures an animal spirit that strikes at a creature and then disappears. Tirada de salvación de Destreza: DC , una criat […] ra que el pueda ver a pies. Fallo: damage. Éxito:  |
| `dev-tools/export/data/dnd-monster-manual.features/es/dnd-monster-manual.features.es.v6-final.json` | `entries.mmAnimalSpirit00.description` | The conjures an animal spirit that strikes at a creature and then disappears. Tirada de salvación de Destreza: DC , una criat […] ra que el pueda ver a pies. Fallo: damage. Éxito:  |
| `dev-tools/export/data/dnd-monster-manual.tables/en/dnd-monster-manual.tables.en-source.json` | `entries.mmAbolethSchemes.results.qHOo4M3sBjxuSZUW.text` | Accomplish incomprehensible plans that lead it to act in seemingly random ways. |
| `dev-tools/IA-ChatGPT/normalization_core.v7.generated.integrated.json` | `_meta.notes.2` | ario) y reglas regex (p.ej. DC→CD, feet→pies). |
| `dev-tools/IA-ChatGPT/phb_en_es_group_dictionaries.json` | `_meta.sources.0` | Player's Handbook.pdf |
| `dev-tools/pdf-audit/reports/mm-pdf-audit.json` | `pdf.warning` | Install pypdf to inspect the local PDF files. |

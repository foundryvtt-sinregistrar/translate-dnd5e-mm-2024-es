# Registro de adopción del proceso común

- Proyecto: `translate-dnd5e-mm-2024-es`.
- Repositorio: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es.
- Plantilla: versión 1 del piloto PHB.
- Commit de las plantillas: `caf298ee2c8b78c27634c2e2f23baf87e44243fe`.
- Base común disponible: `7ccfc5aaf85b39561a35da0b78209aefd68e1321`; todavía no se han incorporado sus archivos de configuración, constructor ni pruebas.
- Rama de trabajo: `chore/homogeneizacion-documentacion`, creada desde `develop` en `463e77ae4ba52340894017cae90ed2ad55458a8a`.

## Estado inicial de ramas

Después de `git fetch origin`, las ramas locales coinciden con sus referencias remotas. `main` (`2d27f1700e814726d83c43245a88840d07d13b95`) y `develop` divergen: uno y once commits exclusivos, respectivamente. Fuera de `dev-tools/`, sus árboles tienen contenido idéntico.

`develop` conserva 212 archivos ausentes en `main`: tres de `dev-tools/IA-ChatGPT/`, uno de `dev-tools/_informes/`, 198 de `dev-tools/export/` y diez de `dev-tools/pdf-audit/`. Se han conservado al crear la rama; no se ha realizado una fusión, eliminación ni reescritura de las ramas principales. Antes de integrar o publicar hay que revisar qué herramientas siguen versionadas y qué fuentes se conservan solo localmente.

## Archivos y adaptaciones

| Destino | Origen | Adaptación |
|---|---|---|
| `README.md` | `plantillas/README.md.template`, commit del kit indicado arriba | Producto MM; requisitos del manifiesto; cuatro compendios reales; activación según el runtime; Apache 2.0 y avisos existentes |
| `README.en.md` | `plantillas/README.en.md.template`, misma revisión | Equivalente inglés de la traducción al español, con los mismos requisitos, alcance y límites |
| `CHANGELOG.md` | Archivo propio | Entrada bajo `[Unreleased]`; se conserva el historial |
| Este registro | Estructura de `plantillas/ADOPCION.md.template` | Procedencia y pendientes específicos de MM |

Se conserva el manifiesto de instalación en `main/module.json` y el alias de ZIP actual. No se ha aplicado todavía la transición de canal del piloto. El producto oficial continúa como requisito documental pendiente de incorporar al manifiesto.

## Verificación del primer paso

Los requisitos se contrastan con `module.json`; los cuatro compendios, con los archivos de `compendium/`; la activación, con `scripts/babele-register.js` y `scripts/converters.js`. Se comprueban enlaces locales, ausencia de marcadores pendientes, coherencia ES/EN y diferencias de Git. El registro queda excluido de `git archive` por la regla existente `dev-tools/ export-ignore`.

No se han cambiado traducciones, scripts, manifiesto, licencia ni herramientas. Este paso documental no acredita nuevas pruebas de runtime, ejecución remota de CI ni comprobación funcional en Foundry.

## Commits del destino

Este registro se incorpora con el primer commit documental de la rama. Para localizarlo y seguir las adopciones posteriores, consulta `git log --oneline -- dev-tools/homogeneizacion/ADOPCION.md`.

## Pendientes

- Resolver la divergencia entre ramas antes de integrar o publicar, preservando herramientas útiles y fuentes locales.
- Ampliar y traducir DEVELOPER, con los ocho convertidores reales y los procedimientos de este proyecto.
- Revisar exclusiones, archivos privados ya versionados, `.editorconfig` y contenido del ZIP.
- Resolver la dependencia de Babele adyacente para las pruebas portables.
- Unificar los constructores Python/PowerShell/Bash conservando sus usos y añadir pruebas del contrato de distribución.
- Declarar el módulo oficial con evidencia para sus límites de versión; preservar Apache 2.0 y las atribuciones existentes.
- Adoptar CI compartida y revisar la coordinación de manifiesto, etiqueta y publicación.
- Completar la comprobación funcional en Foundry y registrar el entorno y alcance.

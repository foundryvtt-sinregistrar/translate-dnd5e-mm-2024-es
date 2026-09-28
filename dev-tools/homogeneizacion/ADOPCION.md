# Registro de adopción

Proyecto: `translate-dnd5e-mm-2024-es`. Rama: `chore/homogeneizacion-documentacion`.

Plantilla inicial: PHB `caf298ee2c8b78c27634c2e2f23baf87e44243fe`; base anterior a esta aplicación en el destino: `56c15b2e82bf5094e8cdf9a333928f5125bb2bc0`. Base común ampliada: `4ab392ea3fbe0e3d7eb44f803a07fe631d15916e` (plantilla versión 2; perfiles y SHA-256). La suite común y el constructor proceden de esa revisión; el perfil de cada destino se conserva por separado.

## Archivos y adaptaciones

Documentación bilingüe, DEVELOPER, CHANGELOG, `.editorconfig`, `.gitattributes`, base de `.gitignore`, constructor y suite de 24 pruebas compartida. El perfil versionado conserva alias `translate-dnd5e-mm-2024-es.zip`, canal `latest` y variante `standard`. Se mantiene la licencia existente de este proyecto. DM y Tomb adoptaron posteriormente MIT para sus aportaciones propias por elección expresa del titular; sus avisos conservan el alcance y los derechos de terceros.

Se mantienen los ocho convertidores `mm2024`. La prueba de integración real con Babele es opcional si falta el módulo hermano; la prueba portable recorre todos los parches de tablas con el convertidor. Los wrappers PowerShell y Bash delegan en el mismo constructor Python. Se conservan herramientas de exportación y auditoría; las exportaciones completas dejan de versionarse sin borrar la copia local.

## Sincronización

Antes de actualizar herramientas comunes, compara la base registrada con la nueva revisión de PHB y revisa las diferencias de cada archivo. Conserva este perfil, las suites propias y los adaptadores. No sobrescribas traducciones ni adaptes una licencia mediante una copia ciega. Los SHA-256 del inventario identifican los bytes de Git sin conversiones LF/CRLF.

## Validación y commits

El informe global registra los resultados definitivos, omisiones, inventario del ZIP y commits. Consulta `git log --oneline -- dev-tools/homogeneizacion/ADOPCION.md` para localizar la adopción. CI remota, pruebas funcionales en Foundry y publicación se verifican por separado; no se presentan como ejecutadas por una validación local.

El commit `56c15b2` integra el historial de main conservando la documentación revisada y las herramientas de develop. Las fuentes completas se retiran del índice conservando sus archivos locales. Las ramas principales no se han sobrescrito.

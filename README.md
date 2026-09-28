# D&D 5e Monster Manual (2024) — Traducción al español

**Español** | [English](README.en.md)

Traducción para Foundry VTT mediante Babele. Identificador: `translate-dnd5e-mm-2024-es`.

## Estado

Versión: **1.14.1**. Incluye traducciones para cuatro compendios del producto oficial: monstruos, contenido del manual, rasgos y tablas de tiradas.

Las pruebas automatizadas cubren el registro, la selección de idioma, los mappings de convertidores y los resultados de tablas. Parte de ellas requiere una instalación local de Babele. La verificación visual y funcional en Foundry durante esta homogeneización sigue pendiente; la presencia de traducciones no acredita por sí sola una revisión completa.

Consulta [CHANGELOG.md](CHANGELOG.md).

## Requisitos

Compatibilidad declarada en `module.json`:

| Dependencia | Versión mínima | Versión verificada |
|---|---|---|
| Foundry VTT | 14.367 | 14.368 |
| Sistema dnd5e | 6.0.0 | 6.0.3 |
| Babele | 2.9.1 | 2.9.1 |

También se necesita el módulo oficial **Monster Manual** (`dnd-monster-manual`), instalado y activado, y las dependencias de Babele. Adquiere e instala el producto oficial por separado. El manifiesto de esta traducción todavía no declara ese producto como dependencia y no establece una versión mínima o verificada para él.

## Instalación

En la configuración de Foundry, abre **Add-on Modules → Install Module** y utiliza este manifiesto:

```text
https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/main/module.json
```

Para instalar manualmente, descarga `translate-dnd5e-mm-2024-es.zip` de las [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases). Con Foundry detenido, extrae la carpeta `translate-dnd5e-mm-2024-es` en `Data/modules/`; el manifiesto debe quedar en `Data/modules/translate-dnd5e-mm-2024-es/module.json`.

## Activación

1. Abre un mundo con el sistema dnd5e.
2. Activa Babele y sus dependencias, el módulo oficial Monster Manual y esta traducción.
3. Selecciona **Español** como idioma de Foundry y recarga el mundo.
4. Abre un compendio del manual para comprobar la traducción.

El registro es automático para `es` y variantes regionales como `es-ES`. Con otros idiomas no se aplica la traducción española.

## Actualización

Actualiza desde Foundry o sustituye la carpeta con el ZIP publicado y Foundry detenido. Recarga el mundo. Las copias ya importadas no se sincronizan automáticamente: revisa las diferencias antes de sustituir documentos con cambios propios.

## Contenido incluido

- Monstruos (`actors`), incluidos campos e ítems anidados cubiertos por los mappings.
- Contenido del manual y diarios (`content`).
- Rasgos (`features`).
- Tablas de tiradas (`tables`).

Babele y los convertidores aplican las traducciones a los compendios del producto oficial conservando identificadores y referencias.

## Limitaciones

- Se requiere el producto oficial; este módulo aporta las traducciones.
- La tabla de requisitos reproduce el manifiesto; no representa una nueva validación funcional de esas combinaciones.
- La revisión visual y funcional sigue pendiente en esta homogeneización.
- Las copias importadas requieren la revisión descrita en Actualización.

## Soporte y contribuciones

Comunica errores en las [incidencias](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/issues), indicando versiones, compendio/documento afectado, pasos, resultado esperado y observado, y si se trata de una copia importada.

## Desarrollo

La [guía de desarrollo](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/blob/main/DEVELOPER.md) está disponible en el repositorio y se excluye del ZIP instalable.

## Licencia y créditos

La licencia Apache 2.0 incluida en el repositorio se puede consultar en [LICENSE.md](LICENSE.md).

Este proyecto contiene traducciones de material del **Monster Manual**, propiedad de Wizards of the Coast. Es una traducción no oficial y no está afiliada a Wizards of the Coast. Consulta también la [Wizards of the Coast Fan Content Policy](https://dnd.wizards.com/en/digital-tools-licensing).

Dungeons & Dragons Monster Manual 2024 © Wizards of the Coast LLC. Todos los derechos reservados.

Autor del módulo: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).

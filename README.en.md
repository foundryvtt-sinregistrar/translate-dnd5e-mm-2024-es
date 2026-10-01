# Monster Manual (2024) — Spanish Translation

**Current version — Foundry v14**

![Foundry v14](https://img.shields.io/badge/Foundry-v14-green)
[![Release v1.14.2](https://img.shields.io/badge/release-v1.14.2-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases/tag/v1.14.2)
![dnd5e 6.0.3](https://img.shields.io/badge/dnd5e-6.0.3-blue)
![Babele 2.9.1 required](https://img.shields.io/badge/Babele-2.9.1_required-orange)
![MM 2024 required](https://img.shields.io/badge/MM_2024-required-orange)
[![Downloads v14](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/main/downloads-v14.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases)

[Español](README.md) | **English**

Translation for Foundry VTT using Babele. Module ID: `translate-dnd5e-mm-2024-es`.

## Status

Version: **1.14.2**. Includes the four handbook compendiums. Tests cover registration, converters and table results. Complete visual and functional verification during this standardization remains pending.

See [CHANGELOG.md](CHANGELOG.md).

Checked on September 28, 2026 with Foundry 14.368, dnd5e 6.0.3 and Babele 2.9.1: loaded 1308 documents across 4 compendiums, checked names and explicit text fields, and imported and visually reviewed one sample. This is not an exhaustive linguistic or functional review; some English labels from the original content remain.

## Requirements

Versions declared in the manifest; “—” means that the corresponding limit is not declared.

| Dependency | Minimum | Verified |
|---|---|---|
| Foundry VTT | 14.367 | 14.368 |
| dnd5e | 6.0.0 | 6.0.3 |
| babele | 2.9.1 | 2.9.1 |
| dnd-monster-manual | — | — |

Install and enable the dependencies, purchasing official products separately when required.

## Installation

In Foundry's Setup screen, open **Add-on Modules → Install Module** and use this manifest:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases/latest/download/module.json
```

For manual installation, download `translate-dnd5e-mm-2024-es.zip` from [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases). With Foundry stopped, extract the `translate-dnd5e-mm-2024-es` folder into `Data/modules/`; the manifest must be at `Data/modules/translate-dnd5e-mm-2024-es/module.json`.

## Activation

1. Open a dnd5e world.
2. Enable Babele, its dependencies, the required official products and this translation.
3. Select **Spanish** and reload the world.
4. Open a translated compendium to check the result.

Registration is automatic for `es` and its regional variants. Other languages do not enable the Spanish translation.

## Updating

Update through Foundry or replace the folder with the published ZIP while Foundry is stopped. Reload the world. Previously imported copies do not synchronize automatically: review differences before replacing documents with your own changes.

## Included content

- `dnd-monster-manual.actors.json`.
- `dnd-monster-manual.content.json`.
- `dnd-monster-manual.features.json`.
- `dnd-monster-manual.tables.json`.

## Limitations

Text coverage and automated tests do not establish that every gameplay automation works. Observe the limitations listed under Status. Imported copies do not update automatically. New release URLs require a publication containing their assets; until available, use a validated ZIP. Private sources, PDFs, OCR and complete official exports are not distributed.

## Support and contributions

Report problems in [issues](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/issues), including versions, affected compendium/document, steps, expected and observed results, and whether it is an imported copy.

## Development

The [development guide](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/blob/main/DEVELOPER.md) is available in the repository and excluded from the installable ZIP.

## License and credits

See the license and its terms in [LICENSE.md](LICENSE.md). The existing Apache 2.0 license is preserved.

Unofficial translation, not affiliated with Wizards of the Coast or Foundry VTT. Official product materials belong to their respective owners. Module author: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).

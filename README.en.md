# D&D 5e Monster Manual (2024) — Spanish Translation

[Español](README.md) | **English**

Translation for Foundry VTT using Babele. Module ID: `translate-dnd5e-mm-2024-es`.

## Status

Version: **1.14.1**. Includes translations for four compendiums from the official product: monsters, handbook content, features, and roll tables.

Automated tests cover registration, language selection, converter mappings, and table results. Some require a local Babele installation. Visual and functional verification in Foundry during this standardization remains pending; the presence of translations alone does not establish a complete review.

See [CHANGELOG.md](CHANGELOG.md).

## Requirements

Compatibility declared in `module.json`:

| Dependency | Minimum version | Verified version |
|---|---|---|
| Foundry VTT | 14.367 | 14.368 |
| dnd5e system | 6.0.0 | 6.0.3 |
| Babele | 2.9.1 | 2.9.1 |

The official **Monster Manual** module (`dnd-monster-manual`) must also be installed and enabled, along with Babele's dependencies. Purchase and install the official product separately. This translation's manifest does not yet declare that product as a dependency or set a minimum or verified version for it.

## Installation

In Foundry's Setup screen, open **Add-on Modules → Install Module** and use this manifest:

```text
https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/main/module.json
```

For manual installation, download `translate-dnd5e-mm-2024-es.zip` from [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases). With Foundry stopped, extract the `translate-dnd5e-mm-2024-es` folder into `Data/modules/`; the manifest must be at `Data/modules/translate-dnd5e-mm-2024-es/module.json`.

## Activation

1. Open a world using the dnd5e system.
2. Enable Babele and its dependencies, the official Monster Manual module, and this translation.
3. Select **Spanish** as Foundry's language and reload the world.
4. Open a handbook compendium to check the translation.

Registration is automatic for `es` and regional variants such as `es-ES`. The Spanish translation is not applied with other languages.

## Updating

Update through Foundry or replace the folder with the published ZIP while Foundry is stopped. Reload the world. Previously imported copies do not synchronize automatically: review differences before replacing documents with your own changes.

## Included content

- Monsters (`actors`), including embedded fields and items covered by the mappings.
- Handbook content and journals (`content`).
- Features (`features`).
- Roll tables (`tables`).

Babele and the converters apply translations to the official product's compendiums while preserving identifiers and references.

## Limitations

- The official product is required; this module provides translations.
- The requirements table reproduces the manifest; it does not represent a new functional validation of those combinations.
- Visual and functional review remains pending during this standardization.
- Imported copies require the review described in Updating.

## Support and contributions

Report problems in [issues](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/issues), including versions, affected compendium/document, steps, expected and observed results, and whether it is an imported copy.

## Development

The [development guide](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/blob/main/DEVELOPER.md) is available in the repository and excluded from the installable ZIP.

## License and credits

The Apache 2.0 license included in the repository is available in [LICENSE.md](LICENSE.md).

This project contains translations of **Monster Manual** material owned by Wizards of the Coast. It is an unofficial translation and is not affiliated with Wizards of the Coast. See also the [Wizards of the Coast Fan Content Policy](https://dnd.wizards.com/en/digital-tools-licensing).

Dungeons & Dragons Monster Manual 2024 © Wizards of the Coast LLC. All rights reserved.

Module author: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).

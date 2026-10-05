# Changelog

Las nuevas entradas se redactan en español, bajo `[Unreleased]` y las categorías `Added`, `Changed` y `Fixed`. El historial anterior conserva su contenido e idioma.


All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.14.3] - 2026-10-05

### Fixed

- Compatibilidad de avances con arrays heredados y objetos indexados por ID en dnd5e 6.x; se conserva el contenedor y solo se traducen etiquetas y pistas, sin fusionar mecánicas.
- Normalizados también los efectos y los avances de objetos embebidos en actores.

### Added

- Pruebas de regresión y evidencia de validación en `dev-tools/VALIDACION-COMPATIBILIDAD-6X.md`.


## [1.14.2] - 2026-09-28

- Comprobados en Foundry 1308 documentos, nombres y campos explícitos; importada y revisada una muestra. Evidencia y límites en `dev-tools/homogeneizacion/VALIDACION-FOUNDRY.md`.

### Changed

- Homogeneizados documentación ES/EN, guía de desarrollo, configuración de edición, exclusiones y proceso de distribución. Constructor desde un único commit, perfil por proyecto, manifiesto externo, SHA-256 y validación compartida en PR y releases. Se conservan las particularidades y los avisos de licencia del proyecto.


### Fixed
- Register translations and converters through `babele.init` and `setup`, avoiding initialization-order dependencies and premature access to core settings in Foundry 14.
- Use the configured Spanish language (including regional variants) for registration.
- Adapt legacy RollTable result translations to Foundry 14 `name` and `description`, preserving IDs and mechanics.

### Changed
- Homogeneizados los README español e inglés: requisitos alineados con el manifiesto, activación automática para español, cuatro compendios reales, límites de validación y enlaces de soporte, desarrollo y licencia. Se conserva el canal de instalación actual.
- Updated compatibility metadata for Foundry VTT 14.368, dnd5e 6.0.3 and Babele 2.9.1.

### Added
- Node regression tests for registration, converter mappings and table results: `node --test tests/*.test.mjs` (requires the adjacent Babele installation).

---

## [1.14.1] - 2026-09-21

### Changed
- Updated compatibility metadata for Foundry VTT `14.368` and dnd5e `6.0.3`.
- Updated the documented dnd5e compatibility range to `6.0.x`.
- Bumped the module version to `1.14.1`.

### Fixed
- Synchronized the release version and compatibility information across `module.json`, `README.md`, and `README.en.md`.

---

## [1.14.0] - 2026-08-25

### Fixed
- Corrected Spanish translations across Monster Manual compendiums.
- Fixed Foundry activity references, target templates, and damage macros.
- Updated actor, content, feature, and roll table data.

### Changed
- Added release archive exclusions through `.gitattributes`.
- Updated `.gitignore` for temporary and distribution files.

### Added
- MM 2024 Spanish translation workflow
- Babele integration and converter infrastructure for Monster Manual 2024
- module.json with system compatibility and Babele dependencies
- Spanish localization files (en.json, es.json)
- 8 converter implementations for MM 2024 content normalization:
  - mm2024-activities-by-id
  - mm2024-actor-details
  - mm2024-actorFullById
  - mm2024-advancement-by-id
  - mm2024-journalEntryFullById
  - mm2024-journalPagesById
  - mm2024-merge-effects
  - mm2024-rollTableResultsById
- Babele compendium mapping configurations for actors, content, features, and tables
- Complete Spanish translations for Monster Manual content entries:
  - Introduction and usage guides (4 pages)
  - Appendix A: Animals (594 lines)
  - Appendix B: Monster conversion tables and organizing lists (6 pages with 500+ creatures)
  - Credits section with licensing and attribution (3 pages)
  - Changelog with version history (4 pages)
  - Art handouts (321 translated pages)
  - A-to-Z monster index (247 pages)
  - Monster detail appendix (comprehensive translations from Aarakocra to Zombie Beholder)
- Full Spanish translation for all Monster Manual actors (400+ creatures)
- Complete Spanish translation for Monster Manual features and abilities
- Spanish translations for Monster Manual roll tables and reference material

### Fixed
- corrected module name references in converter logging
- corrected duplicate converter function definitions
- fixed Githyanki Warrior page naming inconsistencies
- corrected residual typos and translation issues:
  - Amasijo de aniquilaciónn → Amasijo de aniquilación
  - Vampire portador de la noche → Vampiro portador de la noche
  - Pocíon → Poción
  - Mimeto → Mímico
  - Mephit/Mephits → Mefit/Mefits
  - Gorgon de latón → Gorgón de latón
- corrected malformed Flesh Golem Berserk item ID in actor data
- fixed embedded item patches and pending descriptions in actor translations

### Changed
- refined Babele converter function names from phb2024* to mm2024* for module consistency
- reorganized converter imports for cleaner module structure
- standardized Monster Manual glossary normalization across all content categories
- improved translation quality for creature lore, lair effects, and flavor text
- enhanced dragon terminology and planar reference consistency
- refined creature name pluralization and grammatical agreement in Spanish
- optimized title case semantics for structural field labels
- updated release preparation flow to align with Foundry module packaging

## Version Links

[Unreleased]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/compare/v1.14.3...HEAD
[1.14.3]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases/tag/v1.14.3
[1.14.2]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es/releases/tag/v1.14.2

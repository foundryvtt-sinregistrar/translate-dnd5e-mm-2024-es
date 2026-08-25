# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

No changes yet.

### Added
- —

### Changed
- —

### Fixed
- —

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
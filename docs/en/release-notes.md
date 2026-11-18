# Release notes

## 1.0.0

First release of Roguelike Deckbuilder Maker.

- **Data-driven game content.** Cards, relics, potions, powers, enemies, encounters, events, heroes and run rules, kept in content packs and combined into a project.
- **Editors.** Project Overview with project checks, Content Browser, and an editor window for each content type, under **Tools > Roguelike Deckbuilder Maker**. The card, relic, potion, enemy and event editors copy content you built as new content (**Copy as new …**).
- **Art library and sounds.** Default pictures and sounds, ready-made templates, and your own sprites and prefabs added to the same library.
- **Play Preview.** Play a run in the Editor without Play mode, let a test player play, and simulate up to 50 seeds with tables for fights, cards, relics, potions, powers and events.
- **Play screen.** A ready uGUI play screen with animation and sound, shown in the Editor by Game Screen and usable in your own scene and build. The title shows your game title and subtitle.
- **Saves.** Automatic checkpoints, Continue, separate saves per project, and a check of saved runs against changed content.
- **Custom rule modules.** C# card effects, relic effects and enemy actions registered by ID, with value fields in the editors, seed-reproducible random numbers and saved state.
- **Samples.** A complete sample project and an example custom rule module.

Requires Unity 6000.4 or later with the Universal Render Pipeline, uGUI and the Input System. See [Requirements](introduction/requirements.md).

Before updating a project to a later version, back up your project and its saves.

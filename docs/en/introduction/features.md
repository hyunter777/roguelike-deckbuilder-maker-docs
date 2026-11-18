# Feature overview

This page lists what Roguelike Deckbuilder Maker includes. Each item links to the page that explains it.

## A complete game loop

- **Runs across three acts.** Each act has a generated map of 15 floors with fights, elites, events, shops, rest sites and treasure, and ends with a boss. See [Run flow](../concepts/run-flow.md).
- **Turn-based card combat.** Energy, a draw pile, a hand, a discard pile and an exhaust pile, Block, enemy intents, buffs and debuffs, potions, orbs and stances.
- **Rewards and economy.** Card rewards, gold, potions, relics from elites and chests, a boss relic choice, a shop with a card removal service, and rest sites that heal or upgrade.
- **Ascension levels.** An optional ladder of 20 harder levels. Winning with a hero opens the next level. Turn it on or off per project in [Project Overview](../authoring/project-overview.md).
- **Saves and Continue.** A run saves at checkpoints and continues later. When you change content, the maker tells you whether an old save can still continue. See [Saves and continue](../playtesting/saves-continue.md).
- **Score.** The end screen shows a score built from floors, enemies, elites and bosses defeated, bonuses and the ascension level.

## Editors for every kind of content

| Editor | What you make |
|---|---|
| [Card Editor](../authoring/cards.md) | Cards with cost, values, upgraded values, keywords and up to 10 play steps |
| [Relic Editor](../authoring/relics.md) | Relics with up to 4 triggers, each running up to 6 steps |
| [Potion Editor](../authoring/potions.md) | Potions with up to 6 steps, rarity and hero pools |
| [Power Editor](../authoring/powers.md) | New buffs and debuffs that run steps on their own triggers |
| [Enemy Editor](../authoring/enemies.md) | Enemies with HP, moves, intents, AI rules, phases and ascension values |
| [Encounter Editor](../authoring/encounters.md) | Fights and the weak, strong, elite and boss lists of each act |
| [Event Editor](../authoring/events.md) | Events with pages, choices, conditions and outcomes, and the event lists of each act |
| [Hero Editor](../authoring/heroes.md) | Up to four heroes with starting HP, gold, energy, draw, deck and relics |
| [Run Rule Editor](../authoring/run-rules.md) | Run-wide numbers: shop prices, reward chances, chest contents, map room shares, rest healing |
| [Sound & Effects](../authoring/sound-effects.md) | Sounds, music and hit effects for each moment of the play screen |

The Card, Relic, Potion and Enemy editors list ready-made templates under **New from a template**. The Card, Relic, Potion, Enemy and Event editors copy content you made with **Copy as new card**, **Copy as new relic**, **Copy as new potion**, **Copy as new enemy** and **Copy as new event**, keeping its steps and numbers.

## Project tools

- **New Project...** creates a project with starter content or empty. See [Your first game](../getting-started/first-game.md).
- **Create Sample Project** writes a complete sample game: four heroes, 59 cards, three acts. See [Sample project](../getting-started/sample-project.md).
- **Project Overview** sets the game title, subtitle and ascension, manages content packs (add, duplicate, reorder, export and import as JSON) and runs the project check. See [Project Overview](../authoring/project-overview.md).
- **Content Browser** lists every definition in the project with its details and problems. See [Content Browser](../authoring/content-browser.md).

## Pictures and sound

- **Art library.** A default library of pictures for cards, relics, enemies, heroes, events and battle backgrounds is included. Add your own sprite or prefab with **+ Add your picture** in any editor. See [Art library](../authoring/art-library.md).
- **Default sounds.** A default cue library covers the play screen's sounds, music and hit effects. Replace any of them in [Sound & Effects](../authoring/sound-effects.md).

## Playtesting in the Editor

- **Play Preview** runs your project on the real engine in an editor window. A test player can finish a combat, play to the next floor or play to the end, and **Simulate** runs many runs and reports fights, cards, relics, potions, powers and events. See [Play Preview](../playtesting/play-preview.md).
- **Game Screen** and **Player Screen** show the release play screen inside the Editor without entering Play Mode. See [Game Screen](../playtesting/game-screen.md) and [Player Screen and your build](../playtesting/player-screen.md).
- **Seeds.** A fixed seed replays the same run, which makes balance comparisons repeatable.

## Extending with C#

Write a **custom rule module** to add your own card effects, relic effects and enemy actions. They appear as the **Run a custom rule (C#)** step in the editors, with value fields you define. A sample module is included. See [Custom rule modules](../extending/custom-rule-modules.md) and [Example module](../extending/example-module.md).

<!-- figure: features-editors | The Tools > Roguelike Deckbuilder Maker menu expanded, showing its five groups -->

## Related pages

[Welcome](../index.md) · [Requirements](requirements.md) · [Installation](../getting-started/installation.md)

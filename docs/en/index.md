# Welcome

Roguelike Deckbuilder Maker builds a single-player roguelike deck-building game inside the Unity Editor. You make cards, relics, potions, powers, enemies, encounters, events, heroes and run rules in editor windows, and the game plays on a ready-made play screen. You do not write code to make a playable game; C# is only needed if you want to add your own rule types.

[Open the sample project](getting-started/sample-project.md){ .md-button .md-button--primary }
[Make your first game](getting-started/first-game.md){ .md-button }

<!-- figure: welcome-overview | Project Overview, Card Editor and the Game Screen open side by side on the sample project -->

## Who this manual is for

| Reader | Start with |
|---|---|
| Designers who want to make a game from data | [Sample project](getting-started/sample-project.md), then [Your first game](getting-started/first-game.md) |
| Designers who balance an existing project | [Run flow](concepts/run-flow.md), [Run rules](authoring/run-rules.md), [Play Preview](playtesting/play-preview.md) |
| Programmers who add new rule types in C# | [Effects and powers](concepts/effects-and-powers.md), then [Custom rule modules](extending/custom-rule-modules.md) |
| Anyone evaluating the package | [Feature overview](introduction/features.md) and [Requirements](introduction/requirements.md) |

## Where to find the tools

Every tool is in the Unity menu **Tools > Roguelike Deckbuilder Maker**. The menu is grouped in this order:

| Group | Menu items |
|---|---|
| Start | **New Project...**, **Create Sample Project** |
| Project | **Project Overview**, **Content Browser** |
| Content editors | **Card Editor**, **Relic Editor**, **Potion Editor**, **Power Editor**, **Enemy Editor**, **Encounter Editor**, **Event Editor**, **Hero Editor**, **Run Rule Editor**, **Sound & Effects** |
| Play | **Play Preview**, **Game Screen**, **Player Screen** |
| Utilities | **New Custom Rule Module...**, **Rebuild Play Screen Skin**, **About** |

## Learning paths

**Look first (about 10 minutes)**

1. [Install the package](getting-started/installation.md).
2. Choose **Tools > Roguelike Deckbuilder Maker > Create Sample Project**.
3. Play it in **Play Preview** or **Game Screen**. See [Sample project](getting-started/sample-project.md).

**Make your own game (about 30 minutes)**

1. Read [Projects and content](concepts/projects-and-content.md).
2. Follow [Your first game](getting-started/first-game.md): create a project, set the title, add a card and a hero, play a run.
3. Continue with the editor pages under **Editors**, starting with [Cards](authoring/cards.md).

**Understand the rules**

- [Run flow](concepts/run-flow.md) explains the map, rooms, combat turns, rewards and the end of a run.
- [Effects and powers](concepts/effects-and-powers.md) explains the step vocabulary that cards, relics, potions, powers and enemies share.

## Check your setup

- The menu **Tools > Roguelike Deckbuilder Maker** exists after the package finishes compiling.
- **Create Sample Project** finishes with a dialog that names the sample folder.
- **Project Overview** on the sample shows "Project check: no problems found." or only notes.

## Related pages

[Feature overview](introduction/features.md) · [Requirements](introduction/requirements.md) · [Installation](getting-started/installation.md) · [Troubleshooting](help/troubleshooting.md) · [FAQ](help/faq.md)

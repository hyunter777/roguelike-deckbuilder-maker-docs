# Installation

This page explains how to import Roguelike Deckbuilder Maker from the Asset Store and where its files go.

## Before you start

Check the [Requirements](../introduction/requirements.md): Unity 6000.4 or later with URP, Unity UI and Input System. A new project made from the Unity 6 Universal (URP) template already meets them.

## Import the package

1. Open your project in Unity.
2. Open **Window > Package Manager**.
3. Select **My Assets**, find **Roguelike Deckbuilder Maker**, then select **Download** and **Import**.
4. In the import dialog, keep every item selected and select **Import**.
5. Wait until scripts finish compiling. On the first Editor load the package imports the TextMesh Pro essential resources by itself (see [Requirements](../introduction/requirements.md#textmesh-pro-essential-resources)).
6. Confirm that the menu **Tools > Roguelike Deckbuilder Maker** appears.

<!-- figure: install-menu | The Unity menu bar with Tools > Roguelike Deckbuilder Maker open after import -->

## What is installed

Everything is installed under `Assets/DeckForge/`. `DeckForge` is the package's internal folder and code name.

| Path | Contents |
|---|---|
| `README.txt` | Getting-started steps, requirements and the link to this manual |
| `Third-Party Notices.txt` | Licenses of included fonts and other third-party material |
| `Runtime/` | The game engine, content model, saves and run session |
| `Definitions/` | The asset types you author: project, content pack, art library, cue library, custom rule module |
| `MakerEditor/` | The editor windows and menus |
| `Player/` | The release play screen and its scene `Player/Scenes/DeckForgePlayer.unity` |
| `ArtLibrary/Default/` | Default pictures for cards, relics, enemies, heroes, events and backgrounds |
| `CueLibrary/Default/` | Default sounds, music and hit effects |
| `Samples/StarterProject/` | The sample project, written by **Create Sample Project** |
| `Samples/CustomRules/` | A sample custom rule module in C# |

## Keep your own work outside the package folder

Save your projects, content packs, pictures, sounds and C# modules in a folder of your own, for example `Assets/MyGame/`. Do not save them inside `Assets/DeckForge/`.

- A package update replaces files under `Assets/DeckForge/`.
- **Create Sample Project** rewrites the sample's content in `Assets/DeckForge/Samples/StarterProject/` each time you run it. Changes you make to the sample are lost. To build on the sample, use **New Project...** with **Starter content** instead; it creates an independent copy in your own folder. See [Your first game](first-game.md).

## Update the package

1. Back up your project or commit it to version control.
2. Import the new version from **My Assets** as above.
3. Open **Project Overview** with your project and check the project check line for errors.
4. Saves of earlier runs may not continue after an engine change. See [Saves and continue](../playtesting/saves-continue.md).

## Remove the package

Delete the folder `Assets/DeckForge/`. Your projects in other folders stay, but they reference the package's asset types and cannot be opened without it.

## Check your result

- `Assets/DeckForge/README.txt` exists.
- The Console shows no compile errors.
- **Tools > Roguelike Deckbuilder Maker > About** opens a dialog that describes the product.

## Related pages

[Requirements](../introduction/requirements.md) · [Sample project](sample-project.md) · [Your first game](first-game.md) · [Troubleshooting](../help/troubleshooting.md)

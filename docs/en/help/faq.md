# FAQ

## Do I need to enter Play mode to test my game?

No. [Play Preview](../playtesting/play-preview.md), [Game Screen](../playtesting/game-screen.md) and [Player Screen](../playtesting/player-screen.md) all run in Editor windows without Play mode. Use Play mode only when you want to try the play screen in your own scene.

## Which window should I use to playtest?

Use Play Preview to check rules quickly, let the test player play, and simulate many seeds. Use Game Screen to play the way your players will see it, with art, animation and sound.

## Can I make a standalone game with it?

Yes. Use the scene `Player/Scenes/DeckForgePlayer.unity`, or add the **Ugui Player Screen** component to your own scene, set your project and the skin, and add the scene to your build. See [Player Screen and your build](../playtesting/player-screen.md).

## Where are my players' saves?

In a built game, under `Application.persistentDataPath/DeckForge/<Project ID>`. Each project has its own folder, so two games made with the maker never share saves. See [Saves and continue](../playtesting/saves-continue.md).

## Will my players lose their saved run when I update the game?

Not if the update only changes values: the run continues with the new values after a confirmation. If the update removes a card, relic, potion, event, encounter, enemy or custom rule that a saved run uses, that run cannot continue and the player has to start a new run. Keep content that existing saves use, or accept that those runs end.

## Does running Create Sample Project again overwrite my changes?

Yes. **Create Sample Project** writes the sample into `Assets/DeckForge/Samples/StarterProject` and rewrites its content each time you run it. Start your own game with **New Project...**, or copy the sample project and give the copy its own Project ID on Project Overview.

## Where does the title screen get its name?

From **Game title** and **Subtitle** on [Project Overview](../authoring/project-overview.md). An empty title shows "Untitled".

## What happens when content has no art?

It still plays. The play screen shows a plain token, disc or frame in place of the picture. Pick pictures from the [Art library](../authoring/art-library.md), or add your own with **+**.

## Can I write my own effects in C#?

Yes, as custom rule modules: card effects, relic effects and enemy actions, registered by ID and picked in the editors as **Run a custom rule (C#)**. See [Custom rule modules](../extending/custom-rule-modules.md). Custom powers are not part of the module interface.

## Why must custom rules use `context.Rng`?

So that the same seed replays the same run, and simulations can be compared. Other random sources (`System.Random`, `UnityEngine.Random`, the clock) break that.

## Does the test player play like a person?

No. The **Basic** test player follows simple rules and rough card values. Use its win rate to compare versions of your content, not as an exact difficulty measure.

## Does Play Preview open ascension levels?

No. Play Preview shows a run's ending but does not record end-of-run progress. Ascension levels open on the play screen, when **Ascension levels** is on for the project.

## Can I rename the `Assets/DeckForge` folder or its namespaces?

Keep the folder name and the `DeckForge` namespaces. Some editor tools look for files at fixed paths under `Assets/DeckForge`, for example the play screen skin.

## Related pages

- [Troubleshooting](troubleshooting.md)
- [Support and license](../support-license.md)

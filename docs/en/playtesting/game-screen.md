# Game Screen

Game Screen shows the release play screen inside an Editor window without entering Play mode. It is the same uGUI screen your built game uses, with its animations, sounds and art, so you can play your project the way a player will see it while you keep editing.

Open it from **Tools > Roguelike Deckbuilder Maker > Game Screen**.

<!-- figure: game-screen-title | Game Screen window showing the title screen with the game title, subtitle and hero choice -->

## How it works

- The window plays the project that is selected in the Project window when you open it from the menu. If a content pack is selected, it uses the project that contains the pack. Otherwise it uses the first project it finds.
- The screen is drawn at 1920×1080 and scaled to fit the window. The window's minimum size is 960×560.
- Mouse move, click and wheel go to the screen. A right click drops a card or potion you are aiming.
- The screen redraws about 30 times a second while the tab is visible and stops while it is hidden.
- Sound plays only while the Game Screen window has focus, so a window left open does not keep playing music.

## Saves

Game Screen saves under `Library/DeckForgePlayerScreen` in your Unity project, in a folder for the project's ID. This is the same folder the [Player Screen](player-screen.md) window uses, so a run saved in one window can be continued in the other. It is separate from [Play Preview](play-preview.md) saves and from saves of a built game.

## Workflow

1. Select your project asset in the Project window.
2. Open **Tools > Roguelike Deckbuilder Maker > Game Screen**.
3. Pick a hero on the title screen and press **Start**.
4. Play through combats, rewards, the map, shops, rest sites and events.
5. Use **Save & quit** in the top bar, then **Continue** on the title screen to check that the run resumes.

To switch to another project, select that project and choose the menu item again. The window rebuilds the screen for it.

<!-- figure: game-screen-combat | Game Screen during combat with the hand, enemies, intents and the end turn button -->

## When you change content or the game title

The window builds its screen when it opens. After you change the **Game title**, **Subtitle** or **Ascension levels** on [Project Overview](../authoring/project-overview.md), or change content, reopen the window from the menu to see the change. A saved run made with older content is checked when you continue it; see [Saves and continue](saves-continue.md).

## Check your result

- The title screen shows your **Game title** and **Subtitle**. A project with no title shows "Untitled".
- Your heroes appear on the title screen, and **Start** begins a run.
- Enemies, cards, relics and events show their pictures. Content without a picture shows a plain token or frame instead; see [Art library](../authoring/art-library.md).

If the window shows "Select a MakerProjectDefinition (Project Overview) and reopen this window.", no project was found. If it shows "The screen could not be built. See the Console.", read the Console error; see [Troubleshooting](../help/troubleshooting.md).

## Related pages

- [Player Screen and your build](player-screen.md)
- [Play Preview](play-preview.md)
- [Saves and continue](saves-continue.md)

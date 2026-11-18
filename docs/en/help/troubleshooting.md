# Troubleshooting

Each entry names what you see and what to do. Start with the Console: fix compile errors first, because the maker's windows and menus only appear when all scripts compile.

## The Tools > Roguelike Deckbuilder Maker menu is missing

The package's scripts did not compile. Open the Console and fix the first compile error. Check that the project has the packages listed in [Requirements](../introduction/requirements.md) (Universal Render Pipeline, uGUI, Input System).

## Play screen text is missing or drawn with the wrong material

The play screen uses TextMesh Pro. The first time the Editor opens the project, the maker imports TextMesh Pro's essential resources if they are missing, and logs "importing TextMesh Pro essential resources for the play screen text." If the Console instead says "the play screen needs TextMesh Pro's essential resources", import them yourself with **Window > TextMeshPro > Import TMP Essential Resources**, then reopen Game Screen.

## Game Screen or Player Screen says "Select a MakerProjectDefinition (Project Overview) and reopen this window."

No project was found. Create one with **Tools > Roguelike Deckbuilder Maker > New Project...** or **Create Sample Project**, select it in the Project window and open the window again.

## Game Screen says "The screen could not be built. See the Console."

Read the Console error. If `PlayerSkin.asset` is missing, Game Screen tries to rebuild it; you can also run **Tools > Roguelike Deckbuilder Maker > Rebuild Play Screen Skin**. See [Player Screen and your build](../playtesting/player-screen.md).

## The play screen in my scene shows nothing

The Console says "assign the project and the skin to the play screen." Set **Project** and **Skin** on the **Ugui Player Screen** component.

## My change to the title or content does not show in Game Screen

The window builds its screen when it opens. Reopen it from the menu after you change **Game title**, **Subtitle**, **Ascension levels** or content.

## Start run is refused in Play Preview

- "A run is already active. Abandon it first." — press **Save and quit** or **Abandon run** first.
- "The project has no hero in the … slot" — the chosen hero does not exist in the project. Choose another hero, or create one in the [Hero Editor](../authoring/heroes.md).
- "Could not open a preview session: …" — the project does not compose. Open [Project Overview](../authoring/project-overview.md) and fix the errors under **Project checks**.

## Project checks show errors or warnings

**Project checks** on Project Overview lists problems by level. Errors stop runs or saves and must be fixed. Warnings mean content that never appears or does nothing. Notes are for your information. Press **Check again** after a fix; the Content Browser lists every issue.

## Continue is refused, or asks to confirm

The saved run was made with different content. If only values changed, confirm to continue with the current values. If content the run uses was removed, Continue is refused and the missing items are listed; restore them or start a new run. See [Saves and continue](../playtesting/saves-continue.md).

## Continue resumed from an earlier point

The latest checkpoint could not be written or read. Play Preview shows "The last checkpoint could not be saved" or "The saved run was recovered from its backup". Check that the save folder is writable and not locked by another program.

## Two projects overwrite each other's saves

They have the same Project ID, usually because one project asset was copied. Project Overview shows a warning; press **Give this project a new ID** on the copy.

## The run stopped ("The run stopped" or "The engine stopped this run")

The engine stopped the run because a rule could not run, for example a custom rule threw an exception or a step names a rule that no longer exists. The message names the rule and the reason. Fix the content or the rule, then press **Abandon run** and start again.

## An enemy shows an unknown intent

The enemy uses a custom rule whose `Preview` failed or returned an intent kind the screen does not know. The move still runs. Check the rule's `Preview`; see [Custom rule modules](../extending/custom-rule-modules.md).

## "The modules could not register"

A custom rule module failed while registering, for example two rules with the same ID, an ID with `:` or a space, or a value field whose default is outside its range. The message names the rule. Fix the module script and wait for Unity to compile.

## Removing a custom rule module is refused

A card, relic or enemy step still uses one of its rules. Remove or change those steps, then press **Remove** again.

## The same seed gives different results

- The content changed. The simulation summary shows the content fingerprint; the same seeds replay the same runs only while it matches.
- **Fixed seed** is off in Play Preview, so **Start run** uses a random seed.
- A custom rule uses its own random numbers, the clock or a static field. Use only `context.Rng` and the state scopes.

## An enemy, card or relic has no picture

Content without art still plays. Enemies and heroes show a plain token with an icon, relics show a disc with initials, and cards and events show their frame and text without a picture. Pick art in the editors; see [Art library](../authoring/art-library.md).

## The Editor stops responding during Simulate

Simulation plays every run before the window updates. Use **Cancel** on the progress bar to stop after the current run; the finished runs are kept. Simulate fewer runs at a time.

## Game Screen plays no sound

Sound plays only while the Game Screen window has focus. Click into the window. Check the sounds assigned in [Sound and effects](../authoring/sound-effects.md).

## Related pages

- [FAQ](faq.md)
- [Saves and continue](../playtesting/saves-continue.md)
- [Support and license](../support-license.md)

# Saves and continue

A run is saved automatically at fixed points, and **Continue** resumes it later. Saves are kept per project, and before a run continues the maker compares the save with the project's current content. This page explains when saves happen, where they go, and what happens to a saved run after you change your content.

## When a run is saved

The engine writes a checkpoint at these points:

- when the run's opening event is done,
- when you enter a room on the map,
- when a combat ends, before you claim its rewards.

There is one saved run per hero. Starting a new run with a hero that has a saved run replaces that save; the play screen asks first ("Start a new run? … will be replaced.") with **Start new run** and **Back**.

**Save & quit** (play screen) and **Save and quit** (Play Preview) leave the run without writing the current combat. **Continue** resumes from the last checkpoint, so a run quit in the middle of a combat starts that room again. **Abandon run** deletes the hero's saved run.

## Where saves go

Each place that plays your game has its own save folder, and inside it each project has its own folder named after its Project ID.

| Played in | Save folder |
|---|---|
| [Play Preview](play-preview.md) | `Library/DeckForgeMakerPreview` in your Unity project |
| [Game Screen](game-screen.md) and [Player Screen](player-screen.md) windows | `Library/DeckForgePlayerScreen` in your Unity project |
| Your built game | `Application.persistentDataPath/DeckForge/<Project ID>` |

The saves of the Editor windows never mix with the saves of your built game. A project's progress (for example opened ascension levels) is kept in the same project folder as its runs.

The Project ID is shown on [Project Overview](../authoring/project-overview.md) under **Project file**. Two projects with the same ID share their saved runs and progress. Project Overview warns when another project uses the same ID and offers **Give this project a new ID**; the old saves stay with the old ID.

Each save file keeps a backup copy. If the main file cannot be read, the run continues from the backup, and Play Preview shows "The saved run was recovered from its backup … The latest checkpoint may be lost." If a checkpoint cannot be written, the run goes on and Play Preview warns that Continue would resume from an earlier point.

## Continuing after you change content

Every save records the project's ID and a fingerprint of its content and rules. When you press **Continue**, the maker compares the save with the current project. The comparison only reads the save; it never deletes or rewrites it.

| Result | What happens |
|---|---|
| Nothing changed | The run continues. |
| Only values changed | You changed content or rules, but every card, relic, potion, event, encounter, enemy and custom rule the run uses still exists. The run can continue after you confirm, and uses the new values from then on. |
| Content is missing | The run uses something the project no longer has. Continue is refused and the missing items are listed. |
| Different project | The save belongs to another project. Continue is refused. |
| Unsupported | The save's format or rules version cannot be continued by this version. Continue is refused. |

### Values changed

In Play Preview, a dialog **Content changed since this run was saved** explains the change. **Continue with current packs** resumes the run, keeping its deck, relics and floor and using the new values from now on. **Cancel** keeps the save as it is.

On the play screen, the title shows "The game changed since this run was saved. Continuing uses the current content." under the buttons, and **Continue** resumes with the current content.

<!-- figure: continue-values-changed | Play Preview dialog "Content changed since this run was saved" -->

Raising the **Version** of a custom rule counts as a value change. See [Custom rule modules](../extending/custom-rule-modules.md).

### Content missing

If you delete or rename something the saved run uses, for example a card in its deck, a relic it owns or can still find, an event or an encounter it will still meet, an enemy, or a custom rule one of its cards, relics or enemies uses, the run cannot continue.

- Play Preview shows "Cannot continue: …" and a **Missing from the current packs** list, each line naming the kind, the ID and where the run uses it (for example "Card my-card (deck)"). Put these back (or the pack that had them) to continue the run, or start a new run.
- The play screen shows "Continue is not available." with the first five missing items, and hides **Continue**.

The maker does not skip missing content. Restore it, or start a new run.

<!-- figure: continue-missing | Play Preview showing the Missing from the current packs list after a refused Continue -->

## Workflow: check that your changes keep saves working

1. In Game Screen, start a run and play into the first act.
2. Press **Save & quit**.
3. Change a number on a card your deck holds, and reopen Game Screen. **Continue** is offered with the "game changed" note.
4. Delete a card your deck holds, and reopen Game Screen. **Continue** is not available and the card is named.
5. Undo the deletion, or start a new run.

## Check your result

- After **Save & quit**, the title screen offers **Continue** for that hero.
- Changing values does not block **Continue**; removing used content does.
- A copied project has its own Project ID, so it does not share saves with the original.

## Related pages

- [Play Preview](play-preview.md)
- [Game Screen](game-screen.md)
- [Player Screen and your build](player-screen.md)
- [Projects and content](../concepts/projects-and-content.md)
- [Troubleshooting](../help/troubleshooting.md)

# Projects and content

This page explains the two assets every game is made of, the maker project and the content pack, and how the editors write into them.

## The maker project

A **maker project** is one asset (type `MakerProjectDefinition`) that stands for one game. **New Project...** and **Create Sample Project** create it; every editor window has a **Maker project** field at the top that chooses which project it works on. When you open a window, it picks the project selected in the Project window, if any.

| Field | What it does | Where to edit |
|---|---|---|
| Project ID | Identifies the game's saved runs and progress. 1 to 64 letters, digits, hyphens or underscores | Shown in **Project Overview > Project file** |
| Display Name | The game title the play screen shows | **Project Overview > Game title** |
| Subtitle | A short line under the title; empty shows none | **Project Overview > Subtitle** |
| Ascension Enabled | Whether the title screen offers Ascension levels | **Project Overview > Ascension levels** |
| Content Packs | The packs that hold the game's content, in apply order | **Project Overview > Manage packs** |
| Unlock Rules | Keep **Maker**: everything in the catalog is available from the start | **Project Overview > Unlock rules** |
| Art Libraries | Picture libraries the editors offer | Filled by the editors; see [Art library](../authoring/art-library.md) |
| Cue Libraries, Cues | Sound and effect libraries, and the project's choice per play screen moment | [Sound and effects](../authoring/sound-effects.md) |
| Custom Rule Modules | C# modules that add custom card effects, relic effects and enemy actions | [Custom rule modules](../extending/custom-rule-modules.md) |

Leave **Base Catalog** empty. A project's content packs are its whole catalog.

!!! warning "Copied projects share saves"
    Saved runs and progress are kept per Project ID. If you duplicate a project asset, both copies have the same ID and share their saves. **Project Overview** warns about this and offers **Give this project a new ID**. **New Project...** always creates a new ID.

## Content packs

A **content pack** is an asset (type `MakerContentPack`) that holds content definitions. One pack is enough for a game. It holds:

- **Definitions**: cards, relics, potions, powers, enemies, encounters and encounter lists, events and event lists, heroes and run rule values.
- **Card rules**: the play steps of each card you made.
- **Art**: which library picture each card, relic, enemy, hero, event and battle background uses.

### Apply order

A project lists its packs in order. When the project is used, the packs are combined into one catalog in that order:

- A definition with an ID that no earlier pack has is added.
- A definition with the same ID as one in an earlier pack replaces it. A later pack can therefore change content without editing the earlier pack.
- **Every editor saves into the last pack** in the list.

**Project Overview** shows the packs and their counts under **Content packs (apply order)**. Under **Manage packs** you can **Rename**, move **Up** and **Down**, **Duplicate**, **Export JSON** and **Remove** a pack, and add a **New empty pack** or **Import JSON...**. Every change is first tried by combining the whole project; a change that would break the project is not applied. **Remove** takes the pack out of the project but keeps its asset file, and **Edit > Undo** brings it back.

!!! note
    Reordering packs can change which definition wins. Saved runs made with the old order may no longer continue.

### Sharing content as JSON

**Export JSON** writes a pack to a `.json` file. **Import JSON...** reads such a file into a new pack at the end of the list. Use this to move content between Unity projects or to keep a text copy in version control.

## IDs and names

Every definition has an **ID** and a display **Name**.

- The ID is how other content refers to it: a hero's starting deck lists card IDs, an encounter lists enemy IDs, an event step names a card or relic ID, and saved runs store IDs.
- The Name is what players see. You can change a name at any time.
- You choose the ID when you create or copy an item, for example in **New card ID** before **Copy as new card**. Keep IDs stable once saved runs or other content use them.
- A card ID is 1 to 64 letters, digits, spaces, hyphens or underscores, starting with a letter or digit.

Deleting a definition that other content uses is refused. For example, **Delete card** asks you to remove the card from starting decks first.

## Heroes, colors and pools

A project has four **hero slots**. Each slot has a fixed **card color**: Red, Green, Blue or Purple. A hero's card rewards and shop cards come from cards of its slot's color plus colorless cards.

| Pool | What decides membership |
|---|---|
| Card rewards, shop cards, random cards | **Color** and **Rarity** of the card, and the card's **In reward, shop and random-card pools** switch. BASIC and SPECIAL cards never appear as rewards |
| Relic drops and shop relics | The relic's **Tier** (for example COMMON, UNCOMMON, RARE, SHOP, BOSS) and its pool membership in the Relic Editor |
| Potion drops and shop potions | The potion's **Rarity** and which heroes' pools hold it |
| Fights | The act and the weak, strong, elite or boss list of the Encounter Editor |
| Events | The act and the ordinary, shrine or one-time list of the Event Editor |

## How the editors write

All editors follow the same pattern:

1. Choose an item in the left list, start from a template under **New from a template**, or copy an item.
2. Edit the form. Changes stay in a draft; the window shows "Unsaved changes."
3. Select **Save** (or **Create card**, **Create hero** and so on). The editor first combines the whole project with your change. If it fails, nothing is saved and the status box says "Not saved:" with the reason.
4. The change is recorded for **Edit > Undo**.
5. Close and restart a Play Preview session to play with the change.

**Revert** discards the draft. Picture choices are saved at once when you pick them.

### What changing content means for saves

Saved runs remember a fingerprint of the content they were played with. Picture choices are not part of it, so changing a picture never affects saved runs. Changing values, steps or lists can: when you continue an old run after such a change, the game tells you whether it can continue. See [Saves and continue](../playtesting/saves-continue.md).

## Check your project

- **Project Overview** shows the project check line: "Project check: no problems found." or counts of errors, warnings and notes. Select **See checks** for the list, **Check again** to repeat it and **Open Content Browser** to see every entry.
- **Content Browser** lists every definition with its details and problems. See [Content Browser](../authoring/content-browser.md).

<!-- figure: projects-packs-overview | Project Overview showing the content pack table and the Manage packs buttons -->

## Related pages

[Project Overview](../authoring/project-overview.md) · [Content Browser](../authoring/content-browser.md) · [Run flow](run-flow.md) · [Effects and powers](effects-and-powers.md) · [Saves and continue](../playtesting/saves-continue.md)

# Heroes

The Hero Editor sets what each hero starts a run with: name, picture, max HP, gold, energy, cards drawn per turn, orb slots, starting deck, starting relic and ascension curse.

## Open the editor

- Menu: **Tools > Roguelike Deckbuilder Maker > Hero Editor**
- From the [Content Browser](content-browser.md): open a hero entry.

Select the project in the **Maker project** field. Saves go into the project's last content pack.

## Hero slots and card colors

The left column always lists four hero slots. A slot decides which cards the hero uses:

| Slot | Card color |
|---|---|
| Hero slot 1 | Red cards |
| Hero slot 2 | Green cards |
| Hero slot 3 | Blue cards |
| Hero slot 4 | Purple cards |

A hero uses the cards of its slot's color (the **Color** of a card in the [Card Editor](cards.md)) and colorless cards. A filled slot shows the hero's picture, name, max HP and deck size; an empty slot shows **EMPTY**.

<!-- figure: hero-editor-overview | Hero Editor with four hero slots on the left and the form of a hero with starting values, deck and relic -->

## Workflow

1. Select an empty slot and click **Create hero**. The new hero starts with the name "New Hero", 80 max HP, 99 gold, 3 energy, 5 cards drawn per turn and 0 orb slots.
2. Enter a **Name** and adjust the starting values.
3. Build the starting deck with **Add card**, **+1** and **−1**.
4. Pick a **Starting relic** and click **Add**. A hero needs at least one starting relic. If the project has no free STARTER-tier relic, make one in the [Relic Editor](relics.md) first.
5. Click **Save**.
6. After the first save, choose a picture in the **Hero picture** section.
7. Start a new Play Preview run to use the hero.

## Fields

| Field | Range | Meaning |
|---|---|---|
| **Name** | | What the hero select screen and the run show. |
| **Hero picture** | | See [Art library](art-library.md). |
| **Max HP** | 1–999 | Starting max HP. |
| **Gold** | 0–99999 | Starting gold. |
| **Energy per turn** | 1–9 | Energy at the start of each turn. |
| **Cards drawn per turn** | 1–10 | Cards drawn at the start of each turn. |
| **Orb slots** | 0–10 | Starting orb slots. |

The range of each number is shown next to its field. Relics that change energy, draw or orb slots add to these values.

Some starting values are project run rules, shown in a note under the fields:

- Potion slots: 3 by default, 2 from ascension 11.
- From ascension 6 the run starts at 90% HP.
- From ascension 14 max HP is lower: 5 less for slot 1, 4 less for the other slots. The note shows the resulting value for this hero.

Click **Open Run Rule Editor** to change the potion slots and the ascension HP share (area **Run start and ascension**, see [Run rules](run-rules.md)).

## Starting deck

The heading shows the deck size (1 to 100 cards). Each row is one card with its count:

| Control | Meaning |
|---|---|
| **+1** | Adds a copy right after the last copy of the same card. |
| **−1** | Removes the last copy. |
| **Remove** | Removes every copy. |
| **Add card** / **Add** | Adds the chosen card. The list offers this hero's color and colorless cards, without status and curse cards. |

The deck order is kept: a run's first shuffle starts from it. A row shows a warning (not an error) for a curse, a status card or a card of another color, which are legal but unusual.

## Ascension curse

| Field | Meaning |
|---|---|
| **Card** | **None**, or a card added to the starting deck from a set ascension. Curse cards are listed first; status cards are not offered. |
| **From ascension** | 1–20. Shown when a card is chosen; choosing a card suggests 10. |

With a card chosen, runs at that ascension or higher start with one copy of the card at the end of the deck. With **None**, the hero's runs get no ascension curse card.

## Starting relics

The section lists the hero's starting relics. Starting relics are managed in the [Relic Editor](relics.md): only STARTER-tier relics can start a run, and a hero needs at least one because the start event's relic swap takes the first. Click **Open Relic Editor** to change them. A new hero, or a hero without a starting relic, picks its first relic here with **Starting relic** and **Add**.

## Buttons

| Button | Meaning |
|---|---|
| **Save** | Saves the hero into the project's last content pack. |
| **Revert** / **Discard** | Discards unsaved changes, or drops a new unsaved hero. |

## Validation

The editor checks the whole project before it saves. If a check fails the status box shows `Not saved:` with the reason and nothing is written. Common reasons:

- "A hero needs at least one starting relic"
- "A starting relic must be a registered relic"
- "A hero cannot start with two relics that share an implementation ID"
- "A hero needs a starting deck"
- "A starting deck card must be a registered card"
- "A hero ... must be between ... and ..." (a number outside its range)

The [Project Overview](project-overview.md) reports "The project has no hero yet, so no run can start." until a hero is saved.

## Tips

- Create the hero's cards and a STARTER-tier relic before the hero, so the deck and relic lists are ready.
- Keep the deck order in mind: it is the order before the first shuffle.

## Related pages

- [Cards](cards.md)
- [Relics](relics.md)
- [Run rules](run-rules.md)
- [Art library](art-library.md)
- [Projects and content](../concepts/projects-and-content.md)

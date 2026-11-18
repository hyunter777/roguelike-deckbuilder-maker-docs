# Potions

The Potion Editor changes the project's potions and makes new ones. A potion runs a list of steps when it is used. The editor also sets its rarity and which heroes' runs can find it. Saves go into the project's last content pack.

Open it from **Tools > Roguelike Deckbuilder Maker > Potion Editor**, or select a potion in the [Content Browser](content-browser.md) and press **Open in editor**.

<!-- figure: potion-editor | The Potion Editor with the potion list, the What it does steps and the Hero pools toggles -->

## Layout

- **List** on the left: a **Search** field and every potion of the project, ordered by rarity. Each row shows a dot colored by rarity, the potion name and a grey line with its rarity and target.
- **Form** on the right.

The Potion Editor has no template list and no preview column.

## Create a potion

New potions start from an existing one. Select a potion, then under **Make a new potion from this one** type a **New potion ID** and press one of:

| Button | Result |
|---|---|
| **Copy as new potion** | Keeps this potion's steps, numbers, rarity and hero pools. |
| **New potion with its own steps** | Keeps this potion's name and rarity and starts with one step: 10 damage to the chosen enemy, marked as potency. The new potion joins no hero pool until you tick one. |

The new potion is not saved yet. Edit it, then press **Create potion**, or **Discard** to drop it.

A project with no potion yet has nothing to start from in this window. Start the project with the starter content (**New Project...** > **Starter content**) to get a set of potions to copy.

## Save, revert and delete

| Button | What it does |
|---|---|
| **Create potion** / **Save** | Composes the whole project with the change and writes it to the last pack. A refused composition writes nothing. |
| **Discard** / **Revert** | Drops the unsaved new potion, or the unsaved changes. |
| **Delete potion** | Deletes the potion and takes it out of every hero pool. Saved runs that hold it refuse to continue. |

Restart a Play Preview session to use a saved change.

## Fields

| Field | Meaning |
|---|---|
| **Name** | The potion's shown name. |
| **Rarity** | COMMON, UNCOMMON or RARE. Each potion roll picks common 65%, uncommon 25%, rare 10%. Rarity also sets the shop price. |
| **Usable outside combat** | On: the potion can be used on the map too, but its steps can only heal, give gold or raise max HP. Turning it on changes steps that are not allowed outside combat. |

Whether using the potion asks for a target is not a field. It follows the steps: when a step aims at the chosen enemy, using the potion asks for a target. The note under **What it does** says which case applies.

## What it does: steps

Steps run in order when the potion is used. A potion has 1 to 6 steps. Each step is one numbered row:

| Control | Meaning |
|---|---|
| Action dropdown | What the step does. |
| Key dropdown | The power, orb, stance or card the step names, when the action needs one. |
| **(card to create)** | For a power that adds a card each turn: the card it makes. Required; an empty choice is refused. |
| Target | The player, the chosen enemy, a random enemy or all enemies, when the action allows a choice. |
| **Amount** / **Count** | The step's number. **Count** for orbs and cards made. Not shown for Change stance. |
| **Potency** | On: this number is the potion's potency, so a relic that doubles potion potency doubles it. Not shown for Change stance or Add a card to the discard pile. |
| **↑** | Moves the step up. |
| **Remove** | Deletes the step. |

Actions in combat: Deal damage, Deal damage to all enemies, Gain Block, Lose HP, Apply a power, Draw cards, Gain energy, Heal, Channel orbs, Change stance, Add cards to the hand, Add a card to the discard pile, Shuffle cards into the draw pile and Gain gold.

Actions for a potion **Usable outside combat**: Heal, Gain gold and Raise max HP.

A potion cannot run a custom C# rule.

A new step starts with a typical amount for its action, for example 10 damage or 12 Block, with **Potency** on.

An error box under the steps lists every problem the potion would be refused for. It updates on every change.

<!-- figure: potion-editor-steps | Two potion step rows with the Target, Amount and Potency fields -->

## Hero pools

One toggle per hero, labeled with the hero's name and "runs". A pool decides which potions a hero's runs can drop, sell and make with effects that create random potions. Outside every pool, runs never drop or sell the potion.

Each pool must keep at least one common, one uncommon and one rare potion; a save that breaks this is refused.

## Checks

- The error box under the steps.
- "Not saved: ..." in the status box when a save is refused.
- The [Project Overview](project-overview.md) check.

## Tips

- Mark every number a potion-doubling relic should double with **Potency**, and leave it off for numbers that must stay fixed.
- A potion that targets the chosen enemy cannot be used outside combat; keep map potions to healing, gold and max HP.

## Related pages

- [Effects and powers](../concepts/effects-and-powers.md)
- [Powers](powers.md)
- [Relics](relics.md)
- [Heroes](heroes.md)

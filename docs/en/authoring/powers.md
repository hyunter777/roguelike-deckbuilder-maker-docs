# Powers

The Power Editor makes new powers: buffs and debuffs that sit on the player or an enemy as a stack and act through triggers. Cards, relics, potions and enemies put a power on someone with their **Apply a power** step. Saves go into the project's last content pack.

Open it from **Tools > Roguelike Deckbuilder Maker > Power Editor**.

<!-- figure: power-editor | The Power Editor with the New powers list and a power form with one trigger -->

## Built-in powers and your own powers

The maker comes with a set of built-in powers, such as Strength, Dexterity, Vulnerable, Weak and Poison. They need no entry here: every **Apply a power** step lists them by name. The Power Editor lists and edits only the powers your project makes.

Once saved, a new power appears in the **Apply a power** lists of the Card, Relic, Potion, Power and Enemy editors, shown as "Name (ID)".

## Layout

- **List** on the left, under **New powers**: one button per power of your own, showing its name and type. **Create a new power…** opens the new-power form.
- **Form** on the right.

The status box says how many powers of your own the project has and which pack the editor saves into.

## Create a power

1. Press **Create a new power…**.
2. Type a **Power ID** and press **New power**.
3. The new power starts as a buff that gives its holder Block equal to its stack at the start of each turn. Change its fields, triggers and steps.
4. Press **Create power**, or **Discard** to drop it.

A power ID is 1 to 64 letters, digits, spaces, hyphens, underscores or apostrophes, starting with a letter or digit. It must not match an existing power.

## Save, revert and delete

| Button | What it does |
|---|---|
| **Create power** / **Save** | Checks the power, composes the whole project with it and writes it to the last pack. A refused save writes nothing and shows the first problem. |
| **Discard** / **Revert** | Drops the unsaved new power, or reloads the saved one. |
| **Delete power** | Deletes the power after a confirmation. Refused while a card, relic, potion, power or enemy still applies it. |

Restart a Play Preview session to use a saved change.

## Fields

| Field | Meaning |
|---|---|
| **Name** | The power's shown name. |
| **Description** | The power's text. |
| **Type** | **Buff** helps its holder; **Debuff** hurts it. Effects that block debuffs block a Debuff power. |
| **Loses 1 each round** | At the end of every round the stack drops by 1, also the round it was applied; at 0 the power is removed. |
| **Order** | Powers run in this order (0 to 999). Most built-in powers use 5. Equal values keep the order the powers were applied. |

The same power works on the player and on enemies. "The holder" is whoever has it. "The other side" is the player for an enemy, or a random enemy / every enemy for the player.

## Triggers

A power has 1 to 4 triggers, and each trigger has 1 to 6 steps.

| Control | Meaning |
|---|---|
| **When** | The moment the trigger waits for (see below). |
| Card type | Shown for **the player uses a card**: any card, ATTACK, SKILL, POWER, STATUS or CURSE. |
| **Player only** | Run this trigger only while the player holds the power. Needed for steps that use the hand, energy, orbs or a stance; the editor ticks it when you pick such a step. |
| **Remove trigger** | Deletes the trigger. A power keeps at least one. |
| **Add step** | Adds a step (Gain Block equal to the stack). |
| **Add trigger** | Below the last trigger: adds a trigger that runs when the holder's turn ends. |

| When | Moment |
|---|---|
| the holder's turn starts | The holder's turn begins. |
| the holder's turn ends | The holder's turn ends. |
| the player uses a card | The player plays a card (of the chosen type). |
| the holder loses HP | The holder loses HP. |

<!-- figure: power-editor-trigger | A power trigger with Player only ticked and a step using Amount = stack -->

## Steps

Each step is one numbered row:

| Control | Meaning |
|---|---|
| Action dropdown | What the step does. |
| Key dropdown | The power, orb, stance or card the step names, when the action needs one. |
| **(card to create)** | For a power that adds a card each turn: the card it makes. Required; an empty choice is refused. |
| Target | **the holder**, **one on the other side** or **the whole other side**, when the action allows a choice. |
| **Amount = stack** | Use the holder's current stack as the number. |
| **Amount** | A fixed number, shown when **Amount = stack** is off. |
| **↑** | Moves the step up. |
| **Remove** | Deletes the step. A trigger keeps at least one. |

Actions for both sides: Deal damage, Deal damage to all, Gain Block, Lose HP, Heal and Apply a power.

Actions that need **Player only**: Draw cards, Gain energy, Add cards to the hand, Add a card to the discard pile, Shuffle cards into the draw pile, Channel orbs and Change stance.

An error box under the triggers lists every problem the power would be refused for. It updates on every change.

## Use the power

1. Save the power.
2. In the [Card Editor](cards.md), [Relic Editor](relics.md), [Potion Editor](potions.md) or [Enemy Editor](enemies.md), add an **Apply a power** step and pick the new power.
3. Choose who gets it and the amount, which becomes the stack.

For a power you make, a card step can target the player, the chosen enemy or all enemies; a relic step the player, a random enemy or all enemies; a potion step the player, the chosen enemy, a random enemy or all enemies.

## Checks

- The error box under the triggers.
- "Not saved: ..." in the status box when a save is refused.
- The [Project Overview](project-overview.md) check.

## Tips

- Use **Amount = stack** so the same power grows stronger as more is applied.
- Turn on **Loses 1 each round** for a power that should wear off.
- Pick **Debuff** for anything that hurts its holder, so debuff-blocking effects treat it correctly.

## Related pages

- [Effects and powers](../concepts/effects-and-powers.md)
- [Cards](cards.md)
- [Relics](relics.md)
- [Potions](potions.md)
- [Enemies](enemies.md)

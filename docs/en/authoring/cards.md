# Cards

The Card Editor changes the project's cards and makes new ones. A card's values, keywords and picture are fields; what it does when played is a list of steps you build from a fixed set of actions. Saves go into the project's last content pack.

Open it from **Tools > Roguelike Deckbuilder Maker > Card Editor**, or select a card in the [Content Browser](content-browser.md) and press **Open in editor**.

<!-- figure: card-editor | The Card Editor with the card list on the left, the form in the middle and the base and upgraded previews on the right -->

## Layout

The window has three columns:

- **List** on the left: a **Search** field, the **New from a template** buttons and every card of the project.
- **Form** in the middle: the selected card's fields and steps.
- **Preview** on the right: the card as the play screen frames it, once as **PREVIEW** and once as **PREVIEW · UPGRADED**. The preview redraws on every change. It hides while the window is narrower than 1000 pixels.

The status box under the header shows how many cards the project has and which pack the editor saves into.

## The card list

Cards are grouped by color. A hero color group also shows that hero's name. Each row shows:

- a round cost badge in the card's color (`X` for an X cost card, empty for an unplayable card);
- the card name;
- a grey line with the type and rarity.

Type in **Search** to filter by name or ID.

## Create a card

**From a template.** Press one of the **+** buttons under **New from a template**. The maker's templates cover a single-target attack, a block skill, a two-hit attack, an all-enemy attack, a draw skill and a heavy attack. Each template comes with its steps, its values and a default picture from the art library. The new card takes the color of the first hero's starting deck, so it joins that hero's reward pools. It is not saved yet: change what you want, then press **Create card**. The template picture is assigned when the card is created.

**From an existing card.** Select a card. Under **Make a new card from this one**, type a **New card ID** and press **Copy as new card**. The copy keeps the values and plays with a copy of the source card's steps. Change it, then press **Create card**.

A card ID is 1 to 64 letters, digits, spaces, hyphens or underscores, starting with a letter or digit. It must not already exist in the project.

## Save, revert and delete

| Button | What it does |
|---|---|
| **Create card** / **Save** | Composes the whole project with the change and writes it to the last pack. A refused composition writes nothing and the status box shows why. |
| **Revert** | Drops the unsaved changes (or the unsaved new card). |
| **Delete card** | Deletes the card from the last pack after a confirmation. Refused while a hero's starting deck holds it. The card's picture choice and its own steps are removed with it. **Edit > Undo** restores it. |

While there are unsaved changes, **Save** and **Revert** also appear at the top of the form next to "Unsaved changes." (or "Not created yet." for a new card).

Restart a Play Preview session to play with a saved change.

## Identity

| Field | Meaning |
|---|---|
| **Name** | The card's shown name. |
| **Description** | The card text. `!D!`, `!B!` and `!M!` stand for the card's Damage, Block and Magic number; the preview fills them in. `NL` starts a new line. |
| **Type** | ATTACK, SKILL, POWER, STATUS or CURSE. |
| **Target** | ENEMY, ALL_ENEMY, SELF, NONE, SELF_AND_ENEMY or ALL. The target decides whether playing the card asks for an enemy. |
| **Rarity** | BASIC, COMMON, UNCOMMON, RARE, SPECIAL or CURSE. Rewards roll COMMON, UNCOMMON and RARE only. |
| **Color** | One of the hero colors, COLORLESS or CURSE. A card of a hero color appears in that hero's pools only. |

The dropdowns always offer the standard values, plus any other value a card of the project already uses.

## Card picture

The **Card picture** section picks the card's illustration from the art library. It shows the current picture and a button grid of every card picture in the project's libraries.

- Press a picture to use it. The choice is saved at once into the last pack.
- **No picture** clears the choice. The play screen then shows only the card frame.
- **▸ Choose another picture** / **▾ Hide the picture library** opens or folds the grid.
- **+ Add your picture** takes a sprite, a texture (it is switched to Sprite import) or a prefab asset. It joins the project's own art library and is picked for this card.

A new card must be created before it can get a picture. See [Art library](art-library.md).

## Values

| Field | Meaning |
|---|---|
| **Cost** | Energy to play. `-1` makes an X cost card: it spends all energy, and its steps can use X. |
| **Damage** | The number `!D!` shows and damage steps use. |
| **Block** | The number `!B!` shows and Block steps use. |
| **Magic number** | A free number `!M!` shows and steps can read. |

`-1` in Damage, Block or Magic number means the card does not use that value.

## Upgraded values

The values after the card is upgraded at a rest site or by an effect. `-99` keeps the value above.

| Field | Meaning |
|---|---|
| **Upgraded cost** | Cost after upgrade. |
| **Upgraded damage** | Damage after upgrade. |
| **Upgraded block** | Block after upgrade. |
| **Upgraded magic** | Magic number after upgrade. |

The upgraded preview shows the card name with `+` and these values.

## Keywords

| Toggle | Meaning |
|---|---|
| **Exhaust** | The card is removed for the rest of the combat after it is played. |
| **Ethereal** | The card is exhausted if it is still in the hand at the end of the turn. |
| **Innate** | The card starts every combat in the opening hand. |
| **Retain** | The card stays in the hand at the end of the turn. |
| **Unplayable** | The card cannot be played. |

## Play rule: steps

Under **Play rule**, steps run top to bottom when the card is played. A card has 1 to 10 steps.

Each step box has **Up**, **Down** and **Remove** buttons and an **Action** dropdown. The fields under it change with the action:

| Action | Fields |
|---|---|
| Deal damage to the chosen enemy | Amount: this card's Damage. **Multiplier**. |
| Deal damage to all enemies | Amount: this card's Damage, per enemy. |
| Gain Block | Amount: this card's Block. **Multiplier**. |
| Lose HP | **Amount**: Magic number or a fixed amount. |
| Apply a power | **Power**, **Target**, **Amount**. See [Card to create](#card-to-create). |
| Draw cards | **Amount**. |
| Gain energy | **Amount**. |
| Heal | **Amount**. |
| Channel orbs | **Orb**, **Amount**. |
| Change stance | **Stance**. |
| Add cards to the hand | **Card**, **Amount**: a fixed amount or the Magic number. |
| Add a card to the discard pile | **Card**. Always one card. |
| Shuffle cards into the draw pile | **Card**, **Amount**: a fixed amount or the Magic number. |
| Exhaust cards from the hand | **Pick**: the player chooses, or at random. **Cards**. |
| Discard cards from the hand | **Pick**: the player chooses, or at random. **Cards**. |
| Upgrade cards in the hand | **Pick**: the player chooses, or all of them. **Cards** (not for all). |
| Put cards from the discard pile on top of the draw pile | **Cards**. The player chooses. |
| Take cards from the draw pile into the hand | **Cards**. The player chooses. |
| Take cards from the discard pile into the hand | **Cards**. The player chooses. |
| Take cards from the exhaust pile into the hand | **Cards**. The player chooses. |
| Run a custom rule (C#) | **Custom rule** and the rule's own value fields. Listed only when the project has custom card rules. |

Common step fields:

| Field | Meaning |
|---|---|
| **Amount** | Where the step's number comes from: this card's Damage, Block or Magic number, a fixed amount, or X (energy spent) on an X cost card. When there is only one choice, the form shows it as a note. |
| **Fixed amount** | The number used when **Amount** is a fixed amount (-99 to 999). |
| **Multiplier** | Multiplies the card value the step reads (-10 to 10). |
| **Target** | The player, the chosen enemy or all enemies. Most actions have a fixed target shown as a note. A power can only go on the side it is made for (a buff on the player, a debuff on an enemy). |
| **Cards** | How many cards the step picks (1 to 10). |
| **Repeat X times** | On an X cost card: repeat the step X times. |
| **Only when** | always, the card is upgraded, the card is not upgraded, the target does not have the power (Apply a power only), or the player has no Block (Gain Block only). |

Damage uses the card's Damage and Gain Block its Block, so damage and block modifiers from powers still apply. Card-making actions make 1 to 4 cards (amount × multiplier, the upgraded amount too); cards beyond a full hand of 10 go to the discard pile. Pile actions note what happens with an empty pile or a full hand.

**X cost cards.** With **Cost** set to `-1`, a step can repeat X times or take X as its amount. At least one step must use X; with X = 0 those steps do nothing. **Upgrade X bonus** (0 to 9) adds to X when the card is upgraded.

**Write description from steps** fills **Description** from the keywords and steps, using `!D!`, `!B!`, `!M!`, `NL` and `[E]` (the energy icon).

**Show the plan the engine runs** is a closed fold that lists the steps as the engine reads them. A note under it says which of the card's values (Damage, Block, Magic number) change the effect.

An error box under the steps lists every problem the card would be refused for, for example "Add at least one step." The same checks run again when you save. A card with no valid steps is unbound and cannot be played.

<!-- figure: card-editor-steps | Two steps of a card rule with the Action, Target, Amount and Only when fields -->

### Card to create

Some powers add a card each turn. When an **Apply a power** step names such a power, a **Card to create** field appears under it. Choose the card the power makes; the list holds the cards a step may create.

If you leave it empty, the field shows "Choose a card: the power has no card to make otherwise." and the step is refused. The same field appears in the Relic, Potion and Power editors as **(card to create)**.

### Custom rules

**Run a custom rule (C#)** runs one of the project's C# card rules. Pick it in **Custom rule**; the form shows its description, version and target, then one field per value the rule declares: a number with its range, a check box, or a list of card, power or enemy IDs. See [Custom rule modules](../extending/custom-rule-modules.md).

## Card pools

**In reward, shop and random-card pools** puts the card in the card library. Saving adds it at the end of the library order, so existing pools keep their order.

Pools still filter by **Color** and **Rarity**: a BASIC or SPECIAL card never appears as a reward, and a card of a hero color appears only for that hero. Curse pools are not extended.

## Starting deck

Pick a **Hero**. The note shows how many copies of this card that hero's starting deck holds. **+1** adds a copy and **−1** removes one. Save the card first: the buttons are disabled while it has unsaved changes.

## Checks

- The status box shows "Not saved: ..." with the reason when a save is refused.
- The error box under the steps updates on every change.
- The [Project Overview](project-overview.md) check warns about cards that never appear in rewards, steps that resolve to 0 and card creation loops.

## Tips

- Start from a template or copy a card that already plays close to what you want.
- Keep **Description** in step with the steps; **Write description from steps** gives a starting text.
- Use **Only when** with upgraded / not upgraded to make the upgrade change what the card does, not only its numbers.

## Related pages

- [Effects and powers](../concepts/effects-and-powers.md)
- [Powers](powers.md)
- [Heroes](heroes.md)
- [Art library](art-library.md)
- [Play Preview](../playtesting/play-preview.md)

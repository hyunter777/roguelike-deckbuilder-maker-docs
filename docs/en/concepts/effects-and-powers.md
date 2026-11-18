# Effects and powers

This page explains how content does things. Cards, relics, potions, powers, enemy moves and event choices all run a list of **steps**, and most steps come from one shared vocabulary. Powers are the buffs and debuffs that steps apply.

## Steps

A step is one action with its settings, for example "Deal damage to the chosen enemy, amount = this card's Damage". Steps run in list order. In every editor you add steps with an **Add step** button (or **Add trigger** first, for relics and powers), reorder them with **Up** and **Down**, and delete them with **Remove**. The editor checks the steps when you save and lists any problem in a red box.

| Content | Where its steps live | Limits |
|---|---|---|
| Card | **Play rule** in the [Card Editor](../authoring/cards.md) | 1 to 10 steps |
| Relic | Triggers in the [Relic Editor](../authoring/relics.md) | 1 to 4 triggers, each with 1 to 6 steps |
| Potion | Steps in the [Potion Editor](../authoring/potions.md) | 1 to 6 steps |
| Power | Triggers in the [Power Editor](../authoring/powers.md) | 1 to 4 triggers, each with 1 to 6 steps |
| Enemy move | Effects in the [Enemy Editor](../authoring/enemies.md) | Effects run in list order |
| Event choice | Steps in the [Event Editor](../authoring/events.md) | Up to 4 pages, 4 choices per page, 0 to 6 steps per choice |

Amounts are whole numbers from −99 to 999 unless the editor shows another range.

## The shared step vocabulary

The labels below are the ones the editors show. Not every kind is available everywhere; the right-hand columns show where each kind can be used.

| Step | What it does | Card | Relic | Potion | Power |
|---|---|:-:|:-:|:-:|:-:|
| Deal damage | Damages one enemy: the chosen enemy (card, potion), a random enemy (relic) or one on the other side (power) | ✓ | ✓ | ✓ | ✓ |
| Deal damage to all enemies | Damages every enemy | ✓ | ✓ | ✓ | ✓ |
| Gain Block | Adds Block | ✓ | ✓ | ✓ | ✓ |
| Lose HP | Loses HP directly, ignoring Block | ✓ | ✓ | ✓ | ✓ |
| Heal | Restores HP up to max HP | ✓ | ✓ | ✓ | ✓ |
| Apply a power | Adds stacks of a power to the target (see below) | ✓ | ✓ | ✓ | ✓ |
| Draw cards | Draws cards | ✓ | ✓ | ✓ | ✓ |
| Gain energy | Adds energy this turn | ✓ | ✓ | ✓ | ✓ |
| Add cards to the hand | Creates 1 to 4 copies of a card in the hand | ✓ | ✓ | ✓ | ✓ |
| Add a card to the discard pile | Creates a card in the discard pile | ✓ | ✓ | ✓ | ✓ |
| Shuffle cards into the draw pile | Creates cards at random places in the draw pile | ✓ | ✓ | ✓ | ✓ |
| Channel orbs | Channels orbs of a chosen type into the hero's orb slots | ✓ | ✓ | ✓ | ✓ |
| Change stance | Puts the hero into a chosen stance | ✓ | ✓ | ✓ | ✓ |
| Exhaust / Discard / Upgrade cards from the hand | Picks 1 to 10 cards from the hand | ✓ | | | |
| Take cards from the draw, discard or exhaust pile into the hand; put cards from the discard pile on top of the draw pile | The player picks 1 to 10 cards from a pile | ✓ | | | |
| Gain gold | Adds gold | | ✓ | ✓ | |
| Raise max HP | Raises max HP | | ✓ | ✓ | |
| Run a custom rule (C#) | Runs a rule from a [custom rule module](../extending/custom-rule-modules.md) | ✓ | ✓ | | |

Notes:

- Created cards can be any card the project allows the step to create. A full hand holds 10 cards; extra created cards go to the discard pile.
- **Channel orbs** and **Change stance** choose from a fixed list of orb types and stances in the step's dropdown. Orbs need orb slots; set **Orb slots** on the hero in the [Hero Editor](../authoring/heroes.md).
- A relic's **When picked up** and **After a won combat** triggers run outside the combat queue, so they offer only **Heal**, **Gain gold**, **Raise max HP** and custom rules.
- A potion used outside combat (with **Can use outside combat**) can only heal, gain gold or raise max HP.

### Card step settings

| Setting | Choices |
|---|---|
| **Action** | A step kind from the table above |
| **Target** | the player, the chosen enemy, all enemies. Some kinds fix the target |
| **Amount** | a fixed amount, this card's Damage, this card's Block, this card's Magic number, this card's Damage per enemy, or X (energy spent) on an X cost card |
| Multiplier | Multiplies the amount, for example 2 × Magic number |
| **Only when** | always, the card is upgraded, the card is not upgraded, the target does not have a power, the player has no Block |
| Pick (hand and pile steps) | the player chooses, at random, or all of them, depending on the step |

Using the card's own Damage, Block and Magic number keeps the card text, the upgrade and the effect in sync: the description tokens `!D!`, `!B!` and `!M!` show the same values. A card with **Cost** −1 is an X cost card: it spends all energy, and its steps can use X as the amount or repeat X times.

### Relic triggers

| Trigger | When it runs |
|---|---|
| At the start of each combat | Once per combat, after the opening draw |
| At the start of your turn | Every player turn start |
| At the end of your turn | Every player turn end |
| After you play a card of type | When a card is played, optionally only cards of one type, such as ATTACK or SKILL |
| When an enemy dies | Each time an enemy is killed |
| After a won combat | When a combat is won |
| When picked up | Once, when the relic is obtained |

A trigger can run only **Every Nth time** (using the relic's counter) or **Once per combat**. Relic targets are the player, a random enemy or all enemies.

### Power triggers

| Trigger | When it runs |
|---|---|
| the holder's turn starts | Each turn start of the creature that has the power |
| the holder's turn ends | Each turn end of the creature that has the power |
| the player uses a card | When the player plays a card, optionally of one type |
| the holder loses HP | After the holder actually loses HP |

Power targets are relative to the holder: **the holder**, **one on the other side** and **the whole other side**. For the player, "the other side" is a random enemy or every enemy; for an enemy, it is the player. **Amount = stack** uses the power's current stack as the amount. Steps that need a hand, energy, orbs or a stance run only when the holder is the player (**Player only**).

### Enemy move effects

Enemy moves use their own list in the Enemy Editor:

| Effect | What it does |
|---|---|
| Deal damage | Attacks the player, optionally several hits |
| Gain block | The enemy gains Block |
| Give the player / Give itself | Applies a power to the player or to the enemy itself |
| Add to discard pile / Add to draw pile / Add to discard and draw pile | Adds status cards to the player's piles |
| Summon | Adds another enemy to the fight, up to a maximum alive |
| Split when hurt | Splits into smaller enemies at an HP percent |
| Heal itself | Heals the enemy up to its max HP |
| Block a random ally | Gives Block to another living enemy |
| Steal gold | Takes gold; killing the enemy returns it |
| Escape the fight | The enemy leaves the fight without being killed |
| Re-arm damage shift / Remove its power | Special state changes for enemies that change form |
| Run a custom rule (C#) | Runs a custom enemy action |

AI rules then choose the next move with conditions such as **First move of the combat**, **Last move was**, **AI roll below**, **HP below percent**, **Every Nth move** and **Ascension level at least**.

### Event steps

Event choices have their own steps: **Gain gold**, **Lose gold**, **Lose HP**, **Heal**, **Raise max HP**, **Lower max HP**, **Obtain a card**, **Obtain a random card**, **Obtain a curse**, **Remove a card (player picks)**, **Upgrade a card (player picks)**, **Transform a card (player picks)**, **Obtain a relic**, **Obtain a random relic**, **Obtain a random potion** and **Start a fight**. A choice can require a condition: gold or HP at least an amount, a card to upgrade, a removable curse, a relic the player has, or a minimum act.

## Powers

A **power** is a buff or a debuff that sits on the player or an enemy with a number of stacks. Powers show as icons with their amount on the play screen, and their description explains what they do.

### Built-in powers

The maker includes a vocabulary of built-in powers that any **Apply a power** step can use. Examples:

| Power | Effect |
|---|---|
| Strength | Increases attack damage by the amount |
| Dexterity | Increases Block gained from cards by the amount |
| Weak | Deals 25% less attack damage for a number of turns |
| Vulnerable | Takes 50% more damage from attacks for a number of turns |
| Poison | At the start of its turn, loses HP equal to the amount, then the amount decreases by 1 |
| Thorns | When attacked, deals the amount back |
| Artifact | Negates the next debuffs |
| Vigor | The next Attack deals additional damage |

The **Apply a power** dropdown lists every built-in power by name, and the target list offers only the targets that power allows. Some built-in powers create a card each turn; for those, the step shows a **Card to create** field where you choose which of your cards it makes.

### Your own powers

Make new powers in the [Power Editor](../authoring/powers.md):

| Field | Meaning |
|---|---|
| **Power ID** | The ID steps use to apply it |
| **Name**, **Description** | What the play screen shows |
| **Type** | Buff (helps its holder) or Debuff (hurts it; Artifact blocks debuffs) |
| **Loses 1 each round** | The stack drops by 1 at the end of every round; at 0 the power is removed |
| **Order** | Powers run in this order (0 to 999); equal values keep the order they were applied |
| Triggers | When the power acts and which steps it runs |

A new power starts as a buff that gives its holder Block equal to its stack at the start of each turn. Your powers appear in every **Apply a power** list as "Name (ID)", next to the built-in powers. The same power works on the player and on enemies. A power still applied by some content cannot be deleted.

## Custom rules in C#

When the vocabulary is not enough, a programmer can write a **custom rule module**: card effects, relic effects and enemy actions in C# with value fields you fill in the editors. They appear as **Run a custom rule (C#)** in the Card, Relic and Enemy editors. Potions cannot use custom rules. See [Custom rule modules](../extending/custom-rule-modules.md).

<!-- figure: effects-card-steps | Card Editor Play rule section with three steps: Deal damage to the chosen enemy, Apply a power (Weak), Draw cards -->
<!-- figure: effects-power-editor | Power Editor with a new power's Type, Loses 1 each round, Order and one trigger with two steps -->

## Related pages

[Cards](../authoring/cards.md) · [Relics](../authoring/relics.md) · [Potions](../authoring/potions.md) · [Powers](../authoring/powers.md) · [Enemies](../authoring/enemies.md) · [Events](../authoring/events.md) · [Run flow](run-flow.md)

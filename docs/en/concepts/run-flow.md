# Run flow

This page describes what happens in a run, from the hero choice to victory or defeat, so you know where each piece of content appears. The numbers given are the defaults; most of them are project values you change in the [Run Rule Editor](../authoring/run-rules.md).

## Overview

1. The player chooses a hero (and, if the project allows it, an Ascension level).
2. The run starts at the **start event**.
3. The run climbs **three acts**. Each act is a map of 15 floors that ends with a boss.
4. After the act 1 and act 2 bosses, the player opens a **boss chest** and moves on to the next act.
5. Defeating the act 3 boss wins the run. Reaching 0 HP loses it.
6. The end screen shows the score.

<!-- figure: run-flow-map | The play screen map of act 1 with room icons and the boss at the top -->

## Start of the run

The hero starts with the values set in the [Hero Editor](../authoring/heroes.md): max HP, gold, energy per turn, cards drawn per turn, the starting deck and starting relics. The run starts with 3 potion slots.

The **start event** offers the player a choice of gifts before the first floor, such as taking a card, removing, upgrading or changing a card, gaining gold, max HP, potions or a relic. Some gifts come with a price, such as losing max HP or gold, or taking a curse. One gift replaces the hero's first starting relic with a random boss relic. You can choose the start event's picture in the [Event Editor](../authoring/events.md).

## The map

Each act generates a new map from the run's seed: 15 floors, 7 columns, with several paths that branch and join. The player chooses one connected room per floor.

| Floor | Room |
|---|---|
| 1 | Always a fight |
| 2–5 | No elites and no rest sites |
| 9 | Always a treasure room |
| 14 | No rest sites |
| 15 | Always a rest site |
| After 15 | The act's boss |

The remaining rooms are filled by share:

| Room | Default share | Notes |
|---|---|---|
| Shop | 5% | |
| Rest site | 12% | |
| Elite | 8% | Multiplied by 1.6 from Ascension 1 |
| Event (`?`) | 22% | |
| Fight | The rest | |

### `?` rooms

A `?` room usually holds an event. Each time, it may instead turn into a fight, an elite, a shop or a treasure room. The chance of each grows every time it does not happen and resets when it does. A `?` room never becomes an elite below floor 6.

When a `?` room holds an event, it comes from the act's **shrine** list with a 25% chance and from the act's **ordinary** event list otherwise. Events on the run-wide **one-time** list can also appear. See [Events](../authoring/events.md).

## Fights

The first fights of each act come from the act's **weak** list; later fights come from the **strong** list. Elite rooms use the **elite** list and the boss comes from the **boss** list. Each list's weights and the number of fights rolled for the act are set in the [Encounter Editor](../authoring/encounters.md).

### Turn order in combat

**Player turn start**

1. Start-of-turn relics and powers take effect.
2. The player's Block is removed (some powers keep it).
3. Energy is set to the hero's energy per turn.
4. The player draws the hero's cards per turn. When the draw pile is empty, the discard pile is shuffled into it.
5. After-draw relics and powers take effect. Enemy intents for the coming turn are shown.

**Player actions.** The player plays cards by paying their energy cost, uses potions, and selects **End turn**. The hand holds at most 10 cards.

**Player turn end**

1. End-of-turn relics and powers take effect.
2. The hand is discarded, except cards that are retained. Ethereal cards still in the hand are exhausted.

**Enemy turn**

1. Each enemy's Block is removed and its start-of-turn powers (such as Poison) take effect.
2. Each living enemy, in order, performs the move its intent showed, then chooses its next move by its AI rules.

**End of round.** Turn-based buffs and debuffs, such as Weak and Vulnerable, go down by 1. Then the next player turn starts.

Combat ends when every enemy is dead or has escaped (victory), or when the player's HP reaches 0 (defeat).

## Rewards after a fight

| Reward | Normal fight | Elite | Boss |
|---|---|---|---|
| Gold | 10–20 | 25–35 | 95–105 (×0.75 from Ascension 13) |
| Card choice | Pick 1 of 3, or skip | Pick 1 of 3, or skip | Pick 1 of 3 rare cards, or skip |
| Relic | — | 1 relic of a rolled tier | — |
| Potion | 40% chance | 40% chance | 40% chance |

- Card rarities are rolled per card. A rare card lowers the next chance of a rare; commons slowly raise it.
- From act 2, a card reward may already be upgraded.
- The potion chance goes up by 10 after a fight without a potion and down by 10 after one with a potion.
- A card reward offers fewer than three cards when the hero's pools hold fewer different cards.

## Other rooms

**Rest site.** Choose one action: **Rest** heals 30% of max HP, or **Smith** upgrades a card. Some relics add more actions.

**Shop.** Sells cards of the hero's color, colorless cards, relics and potions, and offers a card removal service. One card is on sale at half price. Prices vary slightly around their base value, and the removal price goes up each time it is used. Prices are 10% higher from Ascension 16.

**Treasure room.** Holds a small, medium or large chest with one relic. Larger chests favor rarer relics, and each chest may also hold gold.

**Event.** Shows pages of text with choices. A choice can cost or give gold, HP, max HP, cards, curses, relics or potions, open a card selection to remove, upgrade or transform a card, or start a fight. See [Events](../authoring/events.md).

## Bosses and acts

- Defeating the boss of act 1 or act 2 leads to a **boss chest** that offers 3 relics from the **BOSS** tier. The player takes one or skips.
- The player then moves to the next act. Below Ascension 5, the hero is fully healed; from Ascension 5, 75% of missing HP is restored.
- Defeating the act 3 boss wins the run.

!!! note
    Projects with the **Maker** unlock rules play three acts. There is no fourth act.

## Ascension

When **Ascension levels** is on in [Project Overview](../authoring/project-overview.md), the title screen offers levels 0 to 20. Winning a run opens the next level. Each level adds harder rules, for example more elite rooms (from 1), a run start at 90% HP (from 6), fewer potion slots (from 11), less boss gold (from 13) and higher shop prices (from 16). Enemies get their ascension HP and move values from the [Enemy Editor](../authoring/enemies.md), and heroes can get an ascension curse in their starting deck from the [Hero Editor](../authoring/heroes.md).

## End of the run

- **Defeat**: the player's HP reaches 0.
- **Victory**: the player defeats the act 3 boss.

The end screen shows the score. It is built from floors reached, enemies, elites and bosses defeated, bonus lines and, in an Ascension run, the Ascension level.

## Saves during a run

The run saves at checkpoints, such as entering a room and after a fight's rewards are generated. The player can quit and continue later. See [Saves and continue](../playtesting/saves-continue.md).

## Related pages

[Projects and content](projects-and-content.md) · [Effects and powers](effects-and-powers.md) · [Run rules](../authoring/run-rules.md) · [Encounters](../authoring/encounters.md) · [Events](../authoring/events.md) · [Play Preview](../playtesting/play-preview.md)

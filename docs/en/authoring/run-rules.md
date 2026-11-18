# Run rules

The Run Rule Editor changes run-wide numbers: shop prices, combat rewards, chests, map room chances, resting and run start values. A content pack keeps only the numbers you change; every other number keeps its default.

Card, relic, enemy, event, potion and hero values are edited in their own editors.

## Open the editor

- Menu: **Tools > Roguelike Deckbuilder Maker > Run Rule Editor**
- From the [Hero Editor](heroes.md): **Open Run Rule Editor** opens the **Run start and ascension** area.

Select the project in the **Maker project** field. The status box shows how many rules exist, how many the project changes, and which content pack receives your saves (the project's last content pack).

<!-- figure: run-rule-editor-shop | Run Rule Editor with the Shop area selected, showing rule rows with value fields and default labels -->

## Layout

The left column lists the six areas with the number of rules in each and how many are changed, for example `Shop (27)  [2 changed]`:

- **Shop**
- **Rewards**
- **Chests**
- **Map and ? rooms**
- **Rest sites**
- **Run start and ascension**

The form shows a short explanation of the area, then one row per rule:

| Part of a row | Meaning |
|---|---|
| Description | What the number does. Hover it to see the rule key, the kind of number and the accepted range. |
| Value field | The value used in a run. |
| **Asc N+** field | Only on rules that change with ascension: the value used from ascension N. |
| **default** label | Shows `default` when the value is unchanged, otherwise the default value(s). |

Buttons under the rows:

| Button | Meaning |
|---|---|
| **Save** | Saves the area into the project's last content pack. |
| **Revert** | Discards unsaved changes. |
| **Use default values** | Sets every row of the area back to its default (click **Save** to keep it). |

When the project has only one content pack, values equal to the default are not stored. With several packs, saving an area stores every key of that area so the later pack fully decides it.

## Kinds of numbers

| Kind | How to read it |
|---|---|
| Whole number | A count, price or amount. |
| Multiplier | 1 = unchanged. Rules whose description says "chance" or "share" are values from 0 to 1 (0.25 = 25%). |
| Roll threshold | Splits a roll of 0–99: below the first value is the rarer result. A pair of thresholds may not add up to more than 100. |

## Workflow

1. Select an area on the left.
2. Change the values. Keep each one inside the range shown in its tooltip.
3. Click **Save**. If a value is out of range or a threshold pair is too large, the status box shows `Not saved:` and nothing is written.
4. Start a new Play Preview run to use the change.

## Pictures in Map and ? rooms

The **Map and ? rooms** area also holds picture pickers that are not numbers:

- **Battle background — Act 1** to **Act 4**: the background drawn behind combat in each act.
- **Start event picture**: the picture of the start event.

These are art-library pickers; see [Art library](art-library.md). A picture choice is saved immediately and does not need **Save**.

## Area notes

- **Shop**: prices are before the random spread and relic discounts; relics that change shop prices keep their own rules.
- **Rewards**: the rare-card offset is added to each card roll. Every common card lowers it by the step (not below the minimum), making a rare more likely, and a rare resets it to the start value. Relics that change rewards keep their own rules.
- **Chests**: the size thresholds pick small, medium or large; each size has its own relic tiers, gold chance and gold amount (the amount is spread by ±10%).
- **Map and ? rooms**: room shares set how many of each room the map gets. Shop + rest + elite × the ascension 1 multiplier + event may not exceed 1; the rest are normal fights. A ? room starts each act at the start chances; a chance that does not come up grows by its step, and one that comes up goes back to its reset value. Map size and fixed rows (first fight, treasure, rest before the boss) are not editable.
- **Rest sites**: resting heals this share of max HP, rounded down; the rest site shows the same number.
- **Run start and ascension**: the ascension 6 HP share and the ascension 5 act-change heal apply only from those ascensions; below ascension 5 an act change heals fully. Hero starting values are in the [Hero Editor](heroes.md).

Numbers that change how many random numbers a run draws, such as cards per reward or map size, are not offered.

## Rule reference

### Shop

| Rule | Default | Range |
|---|---|---|
| Shop price of a COMMON card before the random spread | 50 | 0 to 9999 |
| Shop price of an UNCOMMON card before the random spread | 75 | 0 to 9999 |
| Shop price of a RARE card before the random spread | 150 | 0 to 9999 |
| Lower bound of the random card price multiplier | 0.9 | 0 to 10 |
| Upper bound of the random card price multiplier | 1.1 | 0 to 10 |
| Colorless card price multiplier applied after the random spread | 1.2 | 0 to 10 |
| The one card on sale has its price divided by this | 2 | 1 to 100 |
| Shop price of a COMMON relic before the random spread | 150 | 0 to 9999 |
| Shop price of an UNCOMMON relic before the random spread | 250 | 0 to 9999 |
| Shop price of a RARE relic before the random spread | 300 | 0 to 9999 |
| Shop price of a SHOP-tier relic before the random spread | 150 | 0 to 9999 |
| Shop price of a STARTER relic (a shop never draws this tier) | 300 | 0 to 9999 |
| Shop price of a SPECIAL relic (a shop never draws this tier) | 400 | 0 to 9999 |
| Lower bound of the random relic price multiplier | 0.95 | 0 to 10 |
| Upper bound of the random relic price multiplier | 1.05 | 0 to 10 |
| Shop price of a COMMON potion before the random spread | 50 | 0 to 9999 |
| Shop price of an UNCOMMON potion before the random spread | 75 | 0 to 9999 |
| Shop price of a RARE potion before the random spread | 100 | 0 to 9999 |
| Lower bound of the random potion price multiplier | 0.95 | 0 to 10 |
| Upper bound of the random potion price multiplier | 1.05 | 0 to 10 |
| A shop relic tier roll below this is COMMON | 48 | 0 to 99 |
| A roll below this and at or above the common bound is UNCOMMON | 82 | 0 to 99 |
| A shop card rarity roll below this is RARE | 9 | 0 to 99 |
| A roll below this and at or above the rare bound is UNCOMMON | 46 | 0 to 99 |
| Gold for the first card removal of a run | 75 | 0 to 9999 |
| Gold added to the removal price after each removal | 25 | 0 to 9999 |
| Shop price multiplier applied from Ascension 16 | 1.1 | 0 to 10 |

### Rewards

| Rule | Default | Range |
|---|---|---|
| A normal combat card reward roll below this is RARE | 3 | 0 to 100 |
| Added to the rare bound; a normal combat roll below the sum is UNCOMMON | 37 | 0 to 100 |
| An elite card reward roll below this is RARE | 10 | 0 to 100 |
| Added to the elite rare bound; a roll below the sum is UNCOMMON | 40 | 0 to 100 |
| Rare card chance offset after a rare card is offered | 5 | 0 to 99 |
| Amount the rare card chance offset drops after a common card | 1 | 0 to 99 |
| Lowest rare card chance offset | -40 | -99 to 0 |
| Chance a card reward is already upgraded in Act 1 | 0 | 0 to 1 |
| Chance a card reward is already upgraded in Act 2 | 0.25 (ascension 12+: 0.125) | 0 to 1 |
| Chance a card reward is already upgraded in Act 3 | 0.5 (ascension 12+: 0.25) | 0 to 1 |
| Chance a card reward is already upgraded in Act 4 | 0.5 (ascension 12+: 0.25) | 0 to 1 |
| Lowest gold from a normal combat | 10 | 0 to 9999 |
| Highest gold from a normal combat | 20 | 0 to 9999 |
| Lowest gold from an elite combat | 25 | 0 to 9999 |
| Highest gold from an elite combat | 35 | 0 to 9999 |
| Lowest gold from a boss combat | 95 | 0 to 9999 |
| Highest gold from a boss combat | 105 | 0 to 9999 |
| Boss gold multiplier applied from Ascension 13 | 0.75 | 0 to 10 |
| Percent chance a combat offers a potion | 40 | 0 to 100 |
| Amount the potion chance moves after a miss or a drop | 10 | 0 to 100 |
| A potion rarity roll below this is COMMON | 65 | 0 to 100 |
| Added to the common bound; a roll below the sum is UNCOMMON | 25 | 0 to 100 |
| A relic tier roll below this is COMMON | 50 | 0 to 100 |
| Added to the common bound; a roll below the sum is UNCOMMON | 33 | 0 to 100 |

### Chests

| Rule | Default | Range |
|---|---|---|
| A chest size roll below this is a small chest in Acts 1 to 3 | 50 | 0 to 100 |
| Added to the small bound; a roll below the sum is a medium chest in Acts 1 to 3 | 33 | 0 to 100 |
| A chest size roll below this is a small chest in Act 4 | 0 | 0 to 100 |
| Added to the Act 4 small bound; a roll below the sum is a medium chest | 100 | 0 to 100 |
| A small chest relic roll below this is COMMON | 75 | 0 to 100 |
| Added to the small chest common bound; a roll below the sum is UNCOMMON | 25 | 0 to 100 |
| A medium chest relic roll below this is COMMON | 35 | 0 to 100 |
| Added to the medium chest common bound; a roll below the sum is UNCOMMON | 50 | 0 to 100 |
| A large chest relic roll below this is COMMON | 0 | 0 to 100 |
| Added to the large chest common bound; a roll below the sum is UNCOMMON | 75 | 0 to 100 |
| Percent chance a small chest also holds gold | 50 | 0 to 100 |
| Percent chance a medium chest also holds gold | 35 | 0 to 100 |
| Percent chance a large chest also holds gold | 50 | 0 to 100 |
| Base gold in a small chest before the random spread | 25 | 0 to 9999 |
| Base gold in a medium chest before the random spread | 50 | 0 to 9999 |
| Base gold in a large chest before the random spread | 75 | 0 to 9999 |

### Map and ? rooms

| Rule | Default | Range |
|---|---|---|
| Share of assignable map nodes that become shops | 0.05 | 0 to 1 |
| Share of assignable map nodes that become rest sites | 0.12 | 0 to 1 |
| Share of assignable map nodes that become elites before the ascension factor | 0.08 | 0 to 1 |
| Share of assignable map nodes that become events | 0.22 | 0 to 1 |
| Elite room share multiplier applied from Ascension 1 | 1.6 | 0 to 10 |
| Elite chance in a ? room at the start of an act | 0 | 0 to 1 |
| Elite chance added to a ? room after any other result | 0.1 | 0 to 1 |
| Elite chance in a ? room after an elite (a modifier may keep its own value) | 0 | 0 to 1 |
| Monster chance in a ? room at the start of an act | 0.1 | 0 to 1 |
| Monster chance added to a ? room after any other result | 0.1 | 0 to 1 |
| Monster chance in a ? room after a monster | 0.1 | 0 to 1 |
| Shop chance in a ? room at the start of an act | 0.03 | 0 to 1 |
| Shop chance added to a ? room after any other result | 0.03 | 0 to 1 |
| Shop chance in a ? room after a shop | 0.03 | 0 to 1 |
| Treasure chance in a ? room at the start of an act | 0.02 | 0 to 1 |
| Treasure chance added to a ? room after any other result | 0.02 | 0 to 1 |
| Treasure chance in a ? room after a treasure | 0.02 | 0 to 1 |
| A ? room below this floor never rolls an elite | 6 | 0 to 99 |
| Chance an event room draws from the shrine pool | 0.25 | 0 to 1 |

### Rest sites

| Rule | Default | Range |
|---|---|---|
| Fraction of max HP restored by resting (0.3 = 30%) | 0.3 | 0 to 1 |

### Run start and ascension

| Rule | Default | Range |
|---|---|---|
| Potion slots a run starts with (ascension 11 starts with the ascension value) | 3 (ascension 11+: 2) | 0 to 10 |
| Fraction of max HP a run starts with at ascension 6 (0.9 = 90%) | 0.9 | 0 to 1 |
| Fraction of missing HP restored when an act ends at ascension 5 (0.75 = 75%) | 0.75 | 0 to 1 |

## Tips

- Change one area at a time and play a few runs in [Play Preview](../playtesting/play-preview.md) to see the effect.
- Changing chances and thresholds changes which rooms, rewards and prices a seed produces.

## Related pages

- [Heroes](heroes.md)
- [Encounters](encounters.md)
- [Events](events.md)
- [Run flow](../concepts/run-flow.md)

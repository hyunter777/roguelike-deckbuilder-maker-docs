# Enemies

The Enemy Editor creates and edits the enemies of your project: name, picture, HP, moves, and the AI rules that pick the next move. An enemy does nothing on its own; place it in a fight with the [Encounter Editor](encounters.md).

## Open the editor

- Menu: **Tools > Roguelike Deckbuilder Maker > Enemy Editor**
- From the [Content Browser](content-browser.md): open an enemy entry.

At the top of the window, the **Maker project** field selects the project. The status box below it shows how many enemies the project has and which content pack receives your saves (always the project's last content pack).

<!-- figure: enemy-editor-overview | Enemy Editor with the template list on the left, a data enemy form in the middle and the combat preview on the right -->

The window has three columns:

| Column | Contents |
|---|---|
| Left | **Search** field, **New from a template** buttons, then the project's enemies grouped by act. Each row shows the picture thumbnail, the name and the HP range. |
| Middle | The form of the selected enemy. |
| Right | A preview of the enemy as combat shows it, with its name and HP. The column is hidden while the window is narrower than 1000 pixels. |

## Workflow

1. Click a template under **New from a template** (for example **+ Slime**). The editor opens an unsaved draft. Its ID is the template key; a number is added when that ID is already taken.
2. Change the **Name**, the HP fields and the moves and rules.
3. Click **Save**. The editor checks the whole project first; if anything is wrong the status box shows `Not saved:` and the first problem, and nothing is written.
4. After the first save, choose a picture in the picture section. A template draft keeps its template picture when you save it for the first time.
5. Open the [Encounter Editor](encounters.md) and put the enemy in a fight. Restart a Play Preview session to use the change.

To start from one of your own saved enemies instead, select it, type an ID in **New enemy ID** under **Make a new enemy from this one**, and click **Copy as new enemy**. The copy keeps HP, moves, AI rules, starting powers and picture. It stays unsaved until you click **Save**.

## Templates

Templates use damage and block only, so they work in a project that has no powers yet. All start in Act 1 and draw an AI roll.

| Button | HP | Behaviour |
|---|---|---|
| **+ Slime** | 12–16 | Weak. Tackles for 5, then oozes for 4 block, and repeats. |
| **+ Goblin Bandit** | 20–24 | Weak. Opens by ducking behind 6 block, then stabs for 7 twice before ducking again. |
| **+ Cave Bat** | 10–13 | Weak. Bites twice for 3 each turn; every third turn it dives for 8. |
| **+ Stone Golem** | 42–46 | Strong. Hardens for 10 block first, then smashes for 12 and hardens again. |
| **+ Dark Knight** | 78–84 | Elite. Rends for 14, or guards with 16 block and strikes back for 6, and never guards twice in a row. |

Each template also sets higher HP from a high ascension level (+2 HP from ascension 7 for most, +3 for Stone Golem, +4 from ascension 8 for Dark Knight).

## Identity and actions

| Control | Purpose |
|---|---|
| **Name** | The name combat shows for the enemy. A name is required. |
| **Save** | Saves the draft into the project's last content pack. |
| **Revert** | Discards unsaved changes. |
| **Remove from pack** | Removes the enemy from the pack and forgets its picture choice. An unsaved draft is simply discarded. |

## Picture

The **Enemy picture** section chooses a picture from the art library or adds your own with **+ Add your picture**. It is available after the first save. Without a picture the play screen shows only the enemy panel. See [Art library](art-library.md).

## Health

| Field | Meaning |
|---|---|
| **HP min** / **HP max** | Each fight rolls the HP between these values. |
| **High ascension HP min** / **High ascension HP max** | The HP range used from the high ascension level. |
| **High ascension from** | The ascension level (0–20) from which the high ascension range applies. |

HP must be at least 1 and at most 99,999, and a maximum may not be below its minimum.

## Moves and AI

Each time the enemy picks its next move it draws one AI roll from 0 to 99 (unless turned off), then checks the rules from top to bottom; the first rule that matches picks the move. A move with a follow-up skips the rules.

| Field | Meaning |
|---|---|
| **Draws an AI roll** | When off, the enemy draws no AI roll and its rules may not use **AI roll below**. |
| **Move values from ascension** | 0 turns it off. From this ascension (1–20), effects that have an ascension value use it, and the intent shows the same number. |
| **Second level from ascension** | 0 turns it off. A higher level (up to 20) whose values win from that ascension. Turning a level off clears every value of that level. |

### Starts the combat with

| Control | Meaning |
|---|---|
| **Add starting power** | Adds a power row (power and **Amount**). Up to 4 starting powers. The list offers the built-in powers enemies may use plus the project's own powers from the [Power Editor](powers.md). |
| **Starting powers by ascension** / **Add ascension entry** | Up to 4 entries. An entry set to "at every ascension" changes the amount of a listed starting power at the ascension levels. An entry set to a level gives a power that is not listed above, only from that level. Amounts are −999 to 999; 0 keeps the lower value. |
| **Starting Block** | Block the enemy has when the combat starts (0–999). |

### Revive

| Field | Meaning |
|---|---|
| **Turns down** | 0 = never revives. 1–5: how many of its own turns it stays down at 0 HP. |
| **At HP %** | Percent of its max HP it gets back (1–100). |
| **Times per battle** | 1–3. Past this count it dies for good. |
| **Only while another of this enemy is up** | It dies for good when no other copy of the same enemy is up. |

While down, its powers are removed, it shows the unknown intent, and the combat goes on. Minions that die with their summoner and enemies that split never revive. An enemy whose phase 2 starts on death cannot also revive.

### Damage shift

The enemy shifts into a defensive move each time it loses a set amount of HP.

| Field | Meaning |
|---|---|
| **Shift after HP lost** | 0 = off. 1–999: HP it must lose (after Block) before it shifts. |
| **Raised by** | Added to the threshold at each shift (0–999). |
| **Block on shift** | Block gained when it shifts (0–999). |
| **Shift move** | The move it plays after shifting. |
| **From ascension** / **threshold** (two rows) | 0 = no change. From that ascension the starting threshold is the value on the right. The second row is a higher ascension. |

After a shift, the shift stays off until a move with the **Re-arm damage shift** effect runs. That effect turns it on again at the raised threshold, resets the count and removes the enemy's Block. The editor warns when no move re-arms the shift. The remaining damage shows as a power on the enemy. An enemy with phase 2, revive or a split effect cannot use a damage shift.

### Moves

Click **Add move** to add a move (up to 12). Each move starts as a 6-damage attack.

| Control | Meaning |
|---|---|
| **Move** | The move ID that rules refer to. Renaming it updates the rules and follow-ups that point at it. |
| **Name** | The move name. |
| **Intent** | The intent icon the player sees: attack, attack buff, attack debuff, attack defend, buff, debuff, strong debuff, debug, defend, defend debuff, defend buff, escape, magic, none, sleep, stun or unknown. A move with a split effect always shows unknown. |
| **Then** | "roll by the rules", or "always" a given move, which is played next without a roll. |
| **↑** / **↓** / **Remove move** | Reorder or delete the move. |
| **Add follow-up rule** | Up to 8 rules checked after this move. The first match picks the next move without an AI roll; if none matches, **Then** decides. AI roll conditions are not offered here. |
| **Add effect** | Adds an effect (up to 8 per move). Effects run in list order; **↑** moves one up. |

### Effects

| Effect | Main fields | Notes |
|---|---|---|
| **Deal damage** | **Damage** (0–999), **Hits** (1–15) | Always runs; cannot be limited by ascension. |
| **Gain block** | **Block** (0–999), **All monsters**, **Block from damage** | **Block from damage** with Block 0 uses the move's damage after the enemy's powers; the move needs exactly one damage effect. |
| **Give the player** | power, **Amount** | The amount may be negative (−999 to 999). |
| **Give itself** | power, **Amount**, **All monsters** | **All monsters** gives every living monster in the fight the power. |
| **Add to discard pile** | status card, **Cards** (1–5) | Offers the status cards the engine allows for this effect that your project defines. |
| **Add to draw pile** | status card, **Cards** (1–5), **Top of draw pile** | Off: each card goes to a random place. On: the cards go on top and no random roll is used. |
| **Add to discard and draw pile** | status card, **Pairs** | Each pair puts one card in the discard pile and one at a random place of the draw pile. |
| **Summon** | enemy, **Count** (1–2), **Max alive** (1–5), **Minion** | Only enemies built from moves and rules can be summoned. No new summon while that many are alive. A minion dies with its summoner. |
| **Split when hurt** | enemy, **Count** (1–2), **At HP %** (1–99) | Must be the move's only effect. The move is forced once HP falls to the percent; the enemy is replaced by the split enemies, each with its current HP. Splits can nest two levels deep. |
| **Heal itself** | **Heal** (1–999) | Up to its max HP. |
| **Block a random ally** | **Amount** | A random other living enemy gains the Block; with no other enemy, this one does. |
| **Steal gold** | **Gold** (1–999) | Never more than the player has. Killing the enemy gives the stolen gold back as a reward. |
| **Escape the fight** | none | Must be the move's only effect, with the escape intent, and not in phase 2. Not a kill: no kill rewards. If every enemy escapes, the fight ends without gold and potion rewards. |
| **Re-arm damage shift** | none | See [Damage shift](#damage-shift). Damage effects above it count toward the new threshold. |
| **Remove its power** | power | Removes that power from this enemy after the effects above it. |
| **Run a custom rule (C#)** | rule and its values | Shown only when the project has enemy custom rules. The rule's preview decides the intent; the move's intent is used only when the rule shows none. See [Custom rule modules](../extending/custom-rule-modules.md). |

Optional fields that appear when they apply:

| Field | Meaning |
|---|---|
| **Ascension N+** | The value used from the first or second ascension level. 0 keeps the lower value. |
| **Ascension N+ hits** / **cards** / **pairs** | The count used from that level (damage up to 15, cards up to 5). 0 keeps the lower count. |
| **Runs** | "at every ascension", or only from the first or second ascension level. The intent shows only what runs. Not available for damage. |
| **Stops at ascension** | 0 = never stops. 1–20 = the effect runs below this ascension level only. |

The editor warns when an effect or starting power waits for an ascension level the enemy does not set, because it would never run.

### Rules

Click **Add rule** to add a rule (up to 24). A new rule is inserted above a final **Always** rule. Each rule has a condition, an optional second condition (both must match; "and (nothing else)" means none), and **→ use** with the move it picks.

| Condition | Value |
|---|---|
| **Always** | none |
| **First move of the combat** | none |
| **Not yet used this combat:** | a move |
| **AI roll below** | 1–99. Matches that many of the 100 rolls. |
| **Last move was** / **Last move was not** | a move |
| **Last two moves were** / **Last two moves were not both** | a move |
| **Move before last was** / **Move before last was not** | a move |
| **HP below percent** | 1–99. Compares current HP with max HP × percent ÷ 100, rounded down. |
| **From move number** | 1–99. Move numbers count picks from 1. |
| **Every Nth move** | 2–99 |
| **Ascension level at least** | 1–20 |

The last rule must be **Always**, so a move is always picked. For a weighted choice, use increasing roll values, for example below 30 → A, below 75 → B, Always → C.

### Phase 2

| Field | Meaning |
|---|---|
| **Starts** | None, **HP below %** (checked when it picks its next move) or **On death** (at 0 HP it goes down and plays the first phase 2 move on its next turn). |
| **HP below %** | 1–99. |
| **First move** | The phase 2 move played when the phase starts. |
| **New max HP** | 0 keeps the max HP; 1–9999 replaces it. |
| **Heal to %** | 0 = no heal; 1–100 heals up to that percent of max HP. |
| **Removes its debuffs** | Clears its debuffs when the phase starts. |

Choosing a trigger adds a "Power up" move and an attack under **Phase 2 moves**, with **Phase 2 rules** below. Phase 2 happens once per fight; enemies it summons or splits into start in phase 1. Setting **Starts** back to None clears all phase 2 settings.

## Validation

- Problems in moves and rules appear live in a red box under the form. **Save** refuses while any remain and shows the first one.
- HP errors: "HP must be at least 1.", "HP max must not be below HP min.", "HP must be at most 99,999.", "The high ascension level must be between 0 and 20."
- A new enemy ID must not already exist: "An enemy with ID ... already exists."
- If the project uses custom rule modules that fail to register, saving is refused with the registration error.

## Tips

- Give every rule list a final **Always** rule and check the preview column before you save.
- To make a move happen at fixed intervals without randomness, turn off **Draws an AI roll** and use **Every Nth move** or **Last move was** rules.
- Use **Copy as new enemy** to make variants (for example a tougher elite version) without rebuilding the moves.

## Related pages

- [Encounters](encounters.md)
- [Powers](powers.md)
- [Art library](art-library.md)
- [Effects and powers](../concepts/effects-and-powers.md)
- [Play Preview](../playtesting/play-preview.md)

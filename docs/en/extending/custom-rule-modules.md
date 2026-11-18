# Custom rule modules

A custom rule module adds your own C# card effects, relic effects and enemy actions to a project. You register each rule under an ID, and the Card, Relic and Enemy editors then offer it as the step **Run a custom rule (C#)**, with value fields you declare. Use a module when the built-in steps cannot express an effect.

Custom rules run inside the engine. They must use the random numbers and state the engine gives them, so that a seed replays the same run and **Continue** restores the rule's values.

## Create a module

1. Choose **Tools > Roguelike Deckbuilder Maker > New Custom Rule Module...**.
2. Pick a file name inside the `Assets` folder, for example `MyCustomRules.cs`. The file name becomes the class name and must be a valid C# class name. The command writes a script with one example card effect, one relic effect and one enemy action.
3. Wait for Unity to compile, then create the module asset: **Assets > Create > Roguelike Deckbuilder Maker > Custom Rules > MyCustomRules**.
4. Open [Project Overview](../authoring/project-overview.md). Under **Custom rule modules (C#)**, drag the asset into **Add module**.
5. Open the Card, Relic or Enemy editor, add a step of the kind **Run a custom rule (C#)** and pick the rule.

<!-- figure: custom-rule-modules-overview | Project Overview section "Custom rule modules (C#)" with one module, its rule table and the Add module field -->

## The Custom rule modules section

| Control | What it does |
|---|---|
| Module list | Each module asset with its class name. **Select** pings the asset; **Remove** takes it out of the project. |
| Rule table | Every registered rule: **Rule** (ID), **Kind** (Card, Relic, Enemy), **Version**, **Name**. |
| **Add module** | Adds a module asset. It is added only if its rules register and the project still composes. |
| **New module script...** | Same as the menu command. |

**Remove** is refused while a card, relic or enemy step still uses one of the module's rules: remove those steps first. If a module fails to register (for example two rules with the same ID), the section shows "The modules could not register:" with the reason.

## Write a module

A module is a class that derives from `CustomRuleModuleAsset` (namespace `DeckForge.Unity`) and registers rules in `Register`. The rule types are in the namespace `DeckForge.Custom`. A script in your `Assets` folder can use them directly; a script in your own assembly definition must reference `DeckForge.Data`, `DeckForge.Content` and `DeckForge.Content.Unity`.

```csharp
using System.Collections.Generic;
using DeckForge.Custom;
using DeckForge.Unity;
using UnityEngine;

[CreateAssetMenu(menuName = "Roguelike Deckbuilder Maker/Custom Rules/MyCustomRules", fileName = "MyCustomRules")]
public sealed class MyCustomRules : CustomRuleModuleAsset
{
    public override void Register(CustomRuleRegistry registry)
    {
        registry.AddCardEffect(new CustomRuleInfo("my-rules.double-hit", "Double Hit")
        {
            Description = "Deal damage twice to the chosen enemy.",
            Target = CustomTarget.Enemy,
            Params = new List<CustomParam> { new CustomParam("damage", CustomParamKind.Int, 0, 99, 5) },
        }, new DoubleHit());
    }

    sealed class DoubleHit : ICustomCardEffect
    {
        public void Use(ICustomCardContext context) =>
            context.Damage(CustomEffectTarget.Target, context.Param("damage"), 2);
    }
}
```

### Registering rules

| Method | Registers |
|---|---|
| `AddCardEffect(CustomRuleInfo, ICustomCardEffect)` | A card effect, used by card steps. |
| `AddRelicEffect(CustomRuleInfo, ICustomRelicEffect)` | A relic effect, used by relic trigger steps. |
| `AddEnemyAction(CustomRuleInfo, ICustomEnemyAction)` | An enemy action, used by enemy move effects. |

`CustomRuleInfo` describes the rule:

| Field | Meaning |
|---|---|
| `Id` | Unique in the project, at most 64 characters, no `:` and no spaces. Steps and saves refer to the rule by this ID. |
| `DisplayName` | The name shown in the editors' rule list. |
| `Description` | Shown under the rule picker and used as the step's text. |
| `Version` | Starts at 1. Raise it when the rule's behaviour changes. |
| `Target` | `CustomTarget.None`, `Enemy` or `AllEnemies`. A card rule with `Enemy` makes the card need an enemy target. |
| `Params` | The value fields the editors show for the step. |

Each `CustomParam(name, kind, min, max, default)` becomes one field in the editor:

| `CustomParamKind` | Editor field | Read with |
|---|---|---|
| `Int` | Number field labelled "name (min to max)" | `context.Param("name")` |
| `Bool` | Check box (value 0 or 1) | `context.Param("name")` |
| `CardId`, `PowerId`, `EnemyId` | List of the project's cards, powers or enemies | `context.ParamId("name")` |

Field names must be unique within a rule and contain no `:`. The default must lie between min and max. A step that leaves a field out reads its default. Reading a field name the rule did not declare is an error.

### Card effects

`ICustomCardEffect.Use(ICustomCardContext context)` runs when the card's step is reached. The context gives:

- Reads: `Player` (HP, max HP, block, energy, `PowerAmount`), `Enemies`, `Target` (the chosen enemy, or null), `Upgraded`, `PileCount(CustomPile)`.
- Actions: `Damage`, `DamageAll`, `Block`, `ApplyPower`, `Draw`, `AddCard`, `GainEnergy`, `Heal`, `LoseHp`.

Actions are added to the same action queue the built-in steps use, in order. Nothing changes immediately: reads show the state when the card is played, before its queued actions run.

### Relic effects

`ICustomRelicEffect.Run(ICustomRelicContext context)` runs when the relic step's trigger fires (for example **At the start of each combat** or **After you play a card of type**). The relic context reads `Player` and has the actions `Damage`, `DamageAll`, `Block`, `ApplyPower`, `Draw`, `AddCard`, `GainEnergy`, `Heal`, `LoseHp` and `GainGold`. It has `RunState` and `OwnerState`, but no `CombatState`.

Two triggers run outside combat: **When picked up** and **After a won combat**. There a rule can only use `Heal`, `GainGold` and `LoseHp`. Any other action stops the run with a message naming the rule.

### Enemy actions

`ICustomEnemyAction` has two methods:

- `Act(ICustomEnemyContext context)` runs when the move's effect is reached. It can read `Player`, `Self` and `Enemies`, and use `AttackPlayer(amount, hits)`, `GainBlock`, `ApplyPowerToPlayer` and `ApplyPowerToSelf`.
- `Preview(ICustomEnemyIntentContext context)` returns the intent shown above the enemy before it acts, as `new CustomIntent(kind, damage, hits)`. The engine applies the usual damage modifiers to the shown number. The kind is one of `ATTACK`, `ATTACK_BUFF`, `ATTACK_DEBUFF`, `ATTACK_DEFEND`, `BUFF`, `DEBUFF`, `STRONG_DEBUFF`, `DEFEND`, `DEFEND_DEBUFF`, `DEFEND_BUFF`, `ESCAPE`, `MAGIC`, `NONE`, `SLEEP`, `STUN`, `UNKNOWN`.

`Preview` must not change state: calling `Set` there is an error. Decide random values in `Act` and store them, as the template and the [example module](example-module.md) do. If `Preview` fails or returns an unknown kind, the intent shows `UNKNOWN` and the move still runs.

## Random numbers

Use only `context.Rng` (`ICustomRandom`):

| Method | Returns |
|---|---|
| `NextInt(maxInclusive)` | A whole number from 0 to `maxInclusive`, both included. A negative value is an error. |
| `NextBool()` | true or false. |

`Rng` draws from the run's own random streams (card and relic rules share the card stream, enemy actions use the enemy stream), so the same seed gives the same run. Do not use `System.Random`, `UnityEngine.Random`, the clock, or static fields that change; a seed would then no longer replay the same run, and simulations in [Play Preview](../playtesting/play-preview.md) would not be repeatable.

## Saved state

A rule keeps whole numbers in `ICustomState` scopes with `Get(key)`, `Set(key, value)` and `Has(key)`. `Get` returns 0 for a key that was never set.

| Scope | Available to | Lasts |
|---|---|---|
| `RunState` | Card and relic rules | The whole run; saved with the run. |
| `CombatState` | Card rules | One combat; cleared when a combat starts. Not saved. |
| `OwnerState` | All rules | For a card in the deck: the whole run, saved with that card. For a card created during a combat: that combat. For a relic: the whole run, kept separately for each relic. For an enemy: that enemy in that combat. |

Keys are the rule's own names: the engine keeps each rule's keys apart. Each rule may hold at most 16 keys per scope, and a key has at most 64 characters and no `:`. Keep every value the rule needs later in these scopes, not in fields of your class, so that **Continue** restores it.

## Errors and saves

- If a rule throws an exception, the engine stops the run as unsupported and shows the rule ID and the message. The play screen shows "The run stopped" with **Abandon run**; Play Preview shows "The engine stopped this run: …".
- If a step names a rule that is no longer registered, the editor shows "… is not a registered custom rule any more." and the step must be changed.
- Saves record the rules the project's content uses, with their versions. A saved run that uses a rule the project no longer registers cannot continue. A changed **Version** counts as a value change: the run can continue after confirmation. See [Saves and continue](../playtesting/saves-continue.md).

## Check your result

- The rule table on Project Overview lists your rules with the right kind and version.
- The rule appears in the editor's **Custom rule** list with your value fields.
- Play the content in Play Preview, then simulate the same seeds twice: the results match.
- Save and quit in the middle of a run, continue, and check that counted values were kept.

## Related pages

- [Example module](example-module.md)
- [Cards](../authoring/cards.md), [Relics](../authoring/relics.md), [Enemies](../authoring/enemies.md)
- [Effects and powers](../concepts/effects-and-powers.md)
- [Saves and continue](../playtesting/saves-continue.md)

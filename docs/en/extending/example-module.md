# Example module

The package includes a complete custom rule module in `Assets/DeckForge/Samples/CustomRules`. It registers one card effect, one relic effect and one enemy action, and shows how each one uses value fields, saved state and the engine's random numbers. This page walks through it and shows how to try it in a project.

| File | Contents |
|---|---|
| `SampleCustomRuleModule.cs` | The module class with the three rules. |
| `SampleCustomRules.asset` | The module asset to add to a project. |
| `DeckForge.Samples.CustomRules.asmdef` | The sample's assembly. It references `DeckForge.Data`, `DeckForge.Content` and `DeckForge.Content.Unity`. |

The sample project made by **Create Sample Project** does not use this module. Add it to a project yourself to try the rules.

## The complete code

```csharp
using System.Collections.Generic;
using DeckForge.Custom;
using DeckForge.Unity;
using UnityEngine;

namespace DeckForge.Samples
{
    [CreateAssetMenu(menuName = "Roguelike Deckbuilder Maker/Samples/Sample Custom Rules", fileName = "SampleCustomRules")]
    public sealed class SampleCustomRuleModule : CustomRuleModuleAsset
    {
        public override void Register(CustomRuleRegistry registry)
        {
            registry.AddCardEffect(new CustomRuleInfo("sample.echo-strike", "Echo Strike")
            {
                Description = "Deal damage, then extra damage for every time this card was played this run.",
                Target = CustomTarget.Enemy,
                Params = new List<CustomParam>
                {
                    new CustomParam("damage", CustomParamKind.Int, 0, 99, 6),
                    new CustomParam("perUse", CustomParamKind.Int, 0, 20, 1),
                },
            }, new EchoStrike());

            registry.AddRelicEffect(new CustomRuleInfo("sample.tally-stone", "Tally Stone")
            {
                Description = "Every third card played gives energy.",
                Params = new List<CustomParam>
                {
                    new CustomParam("every", CustomParamKind.Int, 2, 10, 3),
                    new CustomParam("energy", CustomParamKind.Int, 1, 3, 1),
                },
            }, new TallyStone());

            registry.AddEnemyAction(new CustomRuleInfo("sample.charge-up", "Charge Up")
            {
                Description = "Guards while it charges, then releases every charge in a double strike.",
                Params = new List<CustomParam>
                {
                    new CustomParam("charges", CustomParamKind.Int, 1, 5, 2),
                    new CustomParam("block", CustomParamKind.Int, 0, 30, 6),
                    new CustomParam("damage", CustomParamKind.Int, 0, 40, 6),
                    new CustomParam("perCharge", CustomParamKind.Int, 0, 10, 3),
                },
            }, new ChargeUp());
        }

        sealed class EchoStrike : ICustomCardEffect
        {
            public void Use(ICustomCardContext context)
            {
                context.Damage(CustomEffectTarget.Target, context.Param("damage"));
                int uses = context.OwnerState.Get("uses") + 1;
                context.OwnerState.Set("uses", uses);
                int extra = uses * context.Param("perUse");
                if (extra > 0) context.Damage(CustomEffectTarget.Target, extra);
            }
        }

        sealed class TallyStone : ICustomRelicEffect
        {
            public void Run(ICustomRelicContext context)
            {
                int count = context.OwnerState.Get("count") + 1;
                if (count < context.Param("every")) { context.OwnerState.Set("count", count); return; }
                context.OwnerState.Set("count", 0);
                context.GainEnergy(context.Param("energy"));
            }
        }

        sealed class ChargeUp : ICustomEnemyAction
        {
            public void Act(ICustomEnemyContext context)
            {
                int charge = context.OwnerState.Get("charge");
                if (charge < context.Param("charges"))
                {
                    context.OwnerState.Set("charge", charge + 1);
                    context.GainBlock(context.Param("block") + context.Rng.NextInt(2));
                    return;
                }
                context.OwnerState.Set("charge", 0);
                context.AttackPlayer(Hit(context.Param("damage"), charge, context.Param("perCharge")), 2);
            }

            public CustomIntent Preview(ICustomEnemyIntentContext context)
            {
                int charge = context.OwnerState.Get("charge");
                return charge < context.Param("charges")
                    ? new CustomIntent("DEFEND", -1)
                    : new CustomIntent("ATTACK", Hit(context.Param("damage"), charge, context.Param("perCharge")), 2);
            }

            static int Hit(int damage, int charge, int perCharge) => damage + charge * perCharge;
        }
    }
}
```

## Echo Strike (card effect)

- `Target = CustomTarget.Enemy`: a card that uses this rule needs an enemy target.
- Two value fields: **damage** (0 to 99, default 6) and **perUse** (0 to 20, default 1).
- It hits the chosen enemy for **damage**, adds 1 to `uses` in `OwnerState`, then hits again for `uses × perUse`.
- For a card in the deck, `OwnerState` belongs to that card for the whole run and is saved with it, so the count grows from combat to combat and survives **Save & quit** and **Continue**. A copy created during a combat starts from 0.

## Tally Stone (relic effect)

- Use it with the relic trigger **After you play a card of type**.
- Two value fields: **every** (2 to 10, default 3) and **energy** (1 to 3, default 1).
- It counts cards in the relic's own `OwnerState` and gives energy on every Nth card, then resets the count. The count is kept for the whole run and saved.

## Charge Up (enemy action)

- Four value fields: **charges**, **block**, **damage** and **perCharge**.
- While its charge is below **charges**, `Act` adds one charge and gains **block** plus 0 to 2 extra block. The extra block comes from `context.Rng.NextInt(2)`, the enemy random stream, so a seed replays it.
- When fully charged, it attacks twice for **damage** + charge × **perCharge** and resets the charge.
- `Preview` reads the same `OwnerState` and returns the matching intent: `DEFEND` while charging, `ATTACK` with the damage and 2 hits when it will strike. It only reads state, as a preview must.

## Try it in a project

1. Open [Project Overview](../authoring/project-overview.md) for your project.
2. Under **Custom rule modules (C#)**, drag `Samples/CustomRules/SampleCustomRules.asset` into **Add module**. The rule table lists `sample.echo-strike`, `sample.tally-stone` and `sample.charge-up`.
3. In the [Card Editor](../authoring/cards.md), add a step **Run a custom rule (C#)** to an attack card and pick **Echo Strike (sample.echo-strike)** in **Custom rule**.
4. In the [Relic Editor](../authoring/relics.md), give a relic the trigger **After you play a card of type**, add the step **Run a custom rule (C#)** and pick **Tally Stone**.
5. In the [Enemy Editor](../authoring/enemies.md), add a move whose effect is **Run a custom rule (C#)** with **Charge Up**.
6. Play a run in [Play Preview](../playtesting/play-preview.md) or [Game Screen](../playtesting/game-screen.md) and fight the enemy.

<!-- figure: example-module-card-step | Card Editor step "Run a custom rule (C#)" with Echo Strike selected and the damage and perUse fields -->

## Check your result

- Echo Strike's second hit grows by **perUse** each time the card is played, also after **Save & quit** and **Continue**.
- With Tally Stone, every third card played gives energy.
- The enemy shows a defend intent while charging and an attack intent with ×2 before it strikes.

To remove the module later, first remove the steps that use its rules, then press **Remove** on Project Overview.

## Related pages

- [Custom rule modules](custom-rule-modules.md)
- [Cards](../authoring/cards.md), [Relics](../authoring/relics.md), [Enemies](../authoring/enemies.md)

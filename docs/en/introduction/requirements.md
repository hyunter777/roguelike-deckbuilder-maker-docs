# Requirements

This page lists what your Unity project needs before you import Roguelike Deckbuilder Maker.

## Unity version

| Item | Requirement |
|---|---|
| Unity | 6000.4 or later |
| Tested with | 6000.4.1f1 |
| Platform for authoring | Unity Editor on any platform Unity 6 supports |

## Packages

| Package | Why it is needed |
|---|---|
| Universal Render Pipeline (`com.unity.render-pipelines.universal`) | The play screen's render settings and materials are URP assets |
| Unity UI (`com.unity.ugui`, includes TextMesh Pro) | The play screen is built with uGUI and TextMesh Pro text |
| Input System (`com.unity.inputsystem`) | The play screen's event system uses the Input System UI input module |

All three are part of the Unity 6 Universal (URP) project template. Start from that template, or add the packages through **Window > Package Manager**.

The package has no other dependencies. It does not need any third-party package, and its save code does not use an external JSON library.

## TextMesh Pro essential resources

The play screen's fonts need the TextMesh Pro essential resources (the SDF shaders and the TMP Settings asset). You do not need to import them yourself. The first time the Editor loads the package, the editor script `MakerEditor/Common/MakerTmpEssentials.cs` checks for them and, if they are missing, imports them from the installed uGUI package without a dialog. It runs once per Editor session and does nothing in a project that already has them.

If the automatic import cannot find the uGUI package, the Console shows a warning. Then import them manually with **Window > TextMeshPro > Import TMP Essential Resources**.

!!! note
    The automatic import runs when the Editor opens normally. A project opened only in batch mode does not run it.

## Project settings

- **Active Input Handling** (Edit > Project Settings > Player > Other Settings) must allow the Input System: **Input System Package (New)** or **Both**.
- The project must use URP as its render pipeline, as the URP template does.

## Check your setup

1. Open **Window > Package Manager > In Project** and confirm Universal RP, Unity UI and Input System are listed.
2. After importing the package, confirm the folder `Assets/TextMesh Pro` exists.
3. Confirm the Console has no compile errors and the menu **Tools > Roguelike Deckbuilder Maker** appears.

## Related pages

[Installation](../getting-started/installation.md) · [Feature overview](features.md) · [Troubleshooting](../help/troubleshooting.md)

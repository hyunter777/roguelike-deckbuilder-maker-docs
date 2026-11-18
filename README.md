# Roguelike Deckbuilder Maker documentation

[Read the manual](https://hyunter777.github.io/roguelike-deckbuilder-maker-docs/)

English user guide for Roguelike Deckbuilder Maker, a Unity Editor toolkit for making single-player roguelike deck-building games.

## Build

Use Python 3.12.

```sh
python -m pip install --user -r requirements.txt
python scripts/build.py
```

Preview the manual with `python -m mkdocs serve`. The build writes the site to `site/`. GitHub Actions builds and deploys the same site to GitHub Pages.

## Add a language

English pages live in `docs/en/`. Add translated folders such as `docs/ko/`, then add their locale entries to the i18n plugin in `mkdocs.yml`.

## Contribute

Use direct instructions and factual present-tense sentences. Keep menu paths, field names and examples aligned with the package. Send documentation corrections through issues or pull requests.

Documentation copyright © FlyCat. The purchased package carries its own distribution license. Support: hyunter@flycat.co.kr.

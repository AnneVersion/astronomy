# Astronomy - Claude Code Instructies

## Project
Interactieve astronomie en astrologie visualisatie-app.
Locatie: `E:\scripts\webscraper\CBSbuurt\astronomy\`

## Starten
```bash
npx serve -p 8765
# → http://localhost:8765
```
Of open `index.html` direct in de browser.

## Branch-strategie
- **main** = stabiel/productie
- **develop** = dagelijkse ontwikkeling (standaard werkbranch)
- **feature/*** = nieuwe features, maak aan vanuit develop

Werk op `develop`. Alleen mergen naar `main` als het stabiel is.

## Architectuur
- `index.html` - Volledige app in 1 bestand (~104KB)
- Gebruikt Canvas/CSS voor astronomische visualisaties
- Geen backend nodig, volledig client-side

## Waar gebleven (maart 2026)
- Zwarte gaten, nevels, sterrenhopen toegevoegd
- Twinkel-animatie en vallende sterren
- Geboortehoroscoop met ascendant, natal chart, compatibiliteit
- Uitgebreide tooltips met planeetinfo

## Let op
- Alles zit in 1 HTML bestand - kan groot worden
- Geen dependencies, geen build stap

# Astronomy - Claude Code Instructies

## Project
Interactieve astronomie visualisatie-app met 9 pagina's en NASA API integratie.
Locatie: `E:\scripts\webscraper\CBSbuurt\astronomy\`
GitHub: AnneVersion/astronomy
GitHub Pages: anneversion.github.io/astronomy

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

## Pagina's (9)
| Pagina | Beschrijving |
|--------|-------------|
| `index.html` | Dashboard: sterrenbeelden, zwarte gaten, hemelposities op geboortedatum |
| `explorer.html` | Space Explorer: zoombaar zonnestelsel, N-Body sim, lichtsnelheid reis, exoplaneten, Mars rover, asteroiden |
| `observatory.html` | Observatorium: NASA APOD, Hubble/Webb, zon-activiteit, sterrenhemel, melkwegen, schaal universum, gravitatiegolven, spectroscopie, kosmische tijdlijn |
| `equinox.html` | Equinox tracker, dag/nacht, aardas kanteling, countdown zonnewenden |
| `hemel.html` | Live hemel boven Nederland, maanfase, planeetposities |
| `zonnestelsel.html` | Planeten in orbit |
| `fotos.html` | NASA foto van de dag |
| `missies.html` | Webb, Voyager, Perseverance |
| `donkerehemel.html` | Lichtvervuiling, donkere hemel wereldkaart, beste sterrenkijkplekken NL |

## Architectuur
- Pure HTML/CSS/JS + Canvas, geen frameworks
- Geen backend nodig, volledig client-side
- Wetenschappelijk: geen emoji's, Material Icons, tooltips voor alle begrippen
- Horoscoop omgebouwd naar astronomische hemelposities (precessie uitleg)

## NASA API's
- NASA APOD (DEMO_KEY)
- NASA NEO (Near Earth Objects)
- NASA DONKI (Space Weather)
- NASA Mars Photos
- HubbleSite
- Open Notify (ISS)
- Solar System OpenData

## Features (maart 2026)
- Zwarte gaten, nevels, sterrenhopen visualisaties
- Twinkel-animatie en vallende sterren
- Geboortehoroscoop met ascendant, natal chart, compatibiliteit (astronomisch, niet astrologisch)
- Uitgebreide tooltips met planeetinfo
- Donkere hemel wereldkaart met lichtvervuiling data
- Eigenaar verjaardag: 5 mei (Eta Aquariden meteorenzwerm = Halley brokstukken!)

## Let op
- Geen dependencies, geen build stap
- Port 8765
- Alle pagina's zijn standalone HTML bestanden

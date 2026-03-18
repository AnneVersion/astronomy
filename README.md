# Astronomy

Interactieve astronomie en astrologie visualisatie-app. Toont het zonnestelsel, sterrenbeelden, zwarte gaten, nevels en sterrenhopen met animaties.

## Features

- Interactief zonnestelsel met planeetinfo (diameter, temperatuur, feitjes)
- Sterrenbeelden en sterrenhemel visualisatie
- Zwarte gaten, nevels en sterrenhopen
- Twinkel-animatie en vallende sterren effecten
- Geboortehoroscoop met ascendant en natal chart
- Compatibiliteitsberekeningen
- Uitgebreide tooltips per hemellichaam

## Starten

Open `index.html` in de browser, of:
```bash
npx serve -p 8765
# → http://localhost:8765
```

## Projectstructuur

| Bestand | Functie |
|---------|---------|
| `index.html` | Volledige applicatie (alles-in-een, ~104KB) |

## Branch-strategie

| Branch | Doel |
|--------|------|
| `main` | Stabiele versie |
| `develop` | Actieve ontwikkeling |
| `feature/*` | Nieuwe functionaliteit (vanuit develop) |

Werk altijd op `develop` of een `feature/*` branch. Merge naar `main` als het stabiel is.

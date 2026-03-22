# Astronomy - Claude Code Instructies

## Project Overzicht

Interactieve astronomie visualisatie-app met 9 pagina's en NASA API integratie.
Wetenschappelijk platform: astronomie, niet astrologie. Horoscoop is omgebouwd naar
astronomische hemelposities met precessie-uitleg.

- **Locatie**: `E:\scripts\webscraper\CBSbuurt\astronomy\`
- **URL**: `http://localhost:8765`
- **GitHub**: AnneVersion/astronomy
- **GitHub Pages**: anneversion.github.io/astronomy

## Starten

```bash
# Optie 1: Python serve.py (met CORS headers)
python serve.py
# -> http://localhost:8765

# Optie 2: npx serve
npx serve -p 8765

# Optie 3: open index.html direct in de browser
```

`serve.py` is een eenvoudige Python HTTP server met CORS headers en cache-control.
Geen dependencies, geen build stap, geen node_modules nodig.

## Branch-strategie

- **main** = stabiel / productie (GitHub Pages)
- **develop** = dagelijkse ontwikkeling (standaard werkbranch)
- **feature/*** = nieuwe features, maak aan vanuit develop

Werk op `develop`. Alleen mergen naar `main` als het stabiel is.

## Architectuur

- **Pure HTML/CSS/JS + Canvas** - geen frameworks, geen bundler
- **Geen backend** - volledig client-side, alle API calls direct vanuit de browser
- **Standalone pagina's** - elke HTML pagina werkt zelfstandig (geen shared JS/CSS bestanden)
- **Externe libraries**:
  - `astronomy-engine` (v2.1.19 via CDN) - astronomische berekeningen (alleen in index.html)
  - Google Fonts: DM Sans + Space Mono
  - Material Icons Round
- **Design systeem**: CSS custom properties in elke pagina (:root variabelen)
  - Donkere achtergrond (#06080f / #0a0b1a), glasmorfisme cards
  - Accentkleuren: gold (#fbbf24), blue (#3b82f6), purple (#a855f7), cyan (#06b6d4)
  - Elke pagina heeft een eigen kleuraccent (gold, neon/indigo, purple, etc.)

## Pagina's (9)

### 1. `index.html` - Astronomie Dashboard (113 KB)
Hoofdpagina met drie tabs/panels:
- **Sterrenhemel** (`panelSky`): Interactieve sterrenkaart op Canvas, sterrenbeelden tekenen, zoom/pan, magnitude filter
- **Hemelposities** (`panelHoroscope`): Geboortehoroscoop omgebouwd naar astronomische hemelposities. Ascendant, natal chart (Canvas), compatibiliteit, precessie-uitleg. Invoer: geboortedatum, -tijd, -plaats
- **Planeten** (`panelPlaneten`): Zwarte gaten, nevels, sterrenhopen visualisaties met Canvas animaties, twinkel-effect en vallende sterren
- Gebruikt `astronomy-engine` library voor astronomische berekeningen

### 2. `explorer.html` - Space Explorer (74 KB)
Zes secties met sub-navigatie:
- **Zonnestelsel** (`sec-solar`): Zoombaar 2D zonnestelsel op Canvas, planeetinfo (diameter, temperatuur), klikbare planeten met info-panel
- **N-Body Simulatie** (`sec-nbody`): Zwaartekracht simulatie met meerdere lichamen, presets (binair systeem, drie-lichamen probleem, etc.)
- **Lichtsnelheid Reis** (`sec-lightspeed`): Visualisatie van reistijd met lichtsnelheid tussen hemellichamen
- **Exoplaneten** (`sec-exoplanets`): Catalogus met bekende exoplaneten, habitable zone berekening
- **Mars Rover** (`sec-mars`): Laatste foto's van Perseverance rover (NASA Mars Photos API)
- **Asteroiden** (`sec-asteroids`): Near Earth Objects feed (NASA NEO API), afstand en grootte

### 3. `observatory.html` - Virtueel Observatorium (78 KB)
Negen secties met sub-navigatie:
- **NASA APOD** (`sec-apod`): Astronomy Picture of the Day met navigatie en galerij
- **Deep Space** (`sec-deepspace`): Hubble/Webb beelden zoeken (HubbleSite API)
- **Zon-activiteit** (`sec-solar`): Zonnevlammen, CME's, geomagnetische stormen (NASA DONKI API)
- **Sterrenhemel** (`sec-constellations`): Sterrenbeelden informatie en visualisatie
- **Melkwegen** (`sec-galaxies`): Typen melkwegen, classificatie, visualisatie
- **Schaal Universum** (`sec-scale`): Interactieve schaalvergelijking van atoom tot heelal
- **Gravitatiegolven** (`sec-waves`): Uitleg en visualisatie van gravitatiegolven
- **Spectroscopie** (`sec-spectroscopy`): Lichtspectrum analyse, absorptielijnen, elementen herkennen
- **Kosmische Tijdlijn** (`sec-timeline`): Van Big Bang tot nu, tijdlijn van het universum

### 4. `equinox.html` - Equinox & Zonnewende (35 KB)
- Astronomische seizoenen met countdown naar volgende equinox/zonnewende
- Aardas kanteling (23,5 graden) visualisatie
- Dag/nacht verdeling voor vandaag
- Daglengte grafiek door het jaar
- Golden hour berekening voor vandaag
- Zonpositie door het jaar (analemma)

### 5. `hemel.html` - Live Hemelkaart (79 KB)
- Live hemel boven Nederland met sterren en planeetposities
- Maanfase berekening en visualisatie
- ISS positie tracking (Open Notify API)
- NASA EPIC foto's van de aarde (epic.gsfc.nasa.gov API)
- WMS/WFS diensten informatie
- Sneltoetsen overzicht

### 6. `zonnestelsel.html` - Zonnestelsel Simulator (25 KB)
- Geanimeerd zonnestelsel met planeten in orbit (Canvas)
- Baansnelheid vergelijking
- Zonnestelsel feiten en statistieken

### 7. `fotos.html` - NASA Foto van de Dag (14 KB)
- NASA APOD viewer met datum-navigatie (vorige/volgende/vandaag)
- Datumkiezer voor specifieke datum
- Galerij met recente foto's (batch laden)
- HD versie openen bij klik op afbeelding
- Cache voor eerder geladen foto's

### 8. `missies.html` - Ruimtemissies (19 KB)
- Voyager 1 tracker: afstand tot aarde (real-time berekening), snelheid, reistijd
- Overzicht actieve ruimtemissies (Webb, Voyager 1 & 2, Perseverance, etc.)
- Missie details: lanceerdatum, status, locatie, ontdekkingen

### 9. `donkerehemel.html` - Donkere Hemel Wereldkaart (58 KB)
- Lichtvervuiling wereldkaart (interactief)
- Bortle-schaal uitleg en visualisatie
- Beste Dark Sky locaties ter wereld
- Beste sterrenkijkplekken in Nederland
- Tips voor sterrenkijken
- Aanbevolen uitrusting per Bortle-klasse
- Beste maanden per astronomisch object

## NASA API's & Externe Bronnen

| API | Gebruik | Pagina's | Key |
|-----|---------|----------|-----|
| **NASA APOD** | Astronomy Picture of the Day | fotos.html, observatory.html | DEMO_KEY |
| **NASA NEO** | Near Earth Objects feed | explorer.html | DEMO_KEY |
| **NASA DONKI** | Space Weather (FLR, CME, GST) | observatory.html | DEMO_KEY |
| **NASA Mars Photos** | Perseverance rover foto's | explorer.html | DEMO_KEY |
| **NASA EPIC** | Aarde foto's vanaf DSCOVR | hemel.html | geen |
| **HubbleSite API** | Hubble/Webb beelden zoeken | observatory.html | geen |
| **Open Notify** | ISS huidige positie | hemel.html | geen |
| **astronomy-engine** | Astronomische berekeningen (JS lib) | index.html | n.v.t. |

Alle NASA API's gebruiken `DEMO_KEY`. Rate limit: 30 requests/uur, 50/dag per IP.

## Design Richtlijnen

- **Wetenschappelijk**: Alle informatie is astronomisch correct, geen astrologie-claims
- **Geen emoji's**: Gebruik Material Icons Round voor alle iconen
- **Tooltips**: Elk vaktechnisch begrip heeft een tooltip met uitleg
- **Taal**: Nederlands (NL)
- **Responsive**: Alle pagina's werken op desktop en mobiel
- **Glasmorfisme**: Semi-transparante cards met backdrop-filter blur
- **Canvas animaties**: Sterrenhemel, zonnestelsel, natal chart, N-body sim
- **Navigatie**: Elke pagina heeft een top bar met tabs naar alle 9 pagina's

## Startup Checklist

### Server starten
```bash
cd E:\scripts\webscraper\CBSbuurt\astronomy
python serve.py
# Verwacht: "Astronomy app: http://localhost:8765"
```

### Pagina's testen

1. **Dashboard** (`http://localhost:8765/`)
   - [ ] Sterrenhemel canvas laadt en toont sterren
   - [ ] Tab "Hemelposities" opent en geboortedatum formulier werkt
   - [ ] Tab "Planeten" toont animaties (zwarte gaten, nevels)
   - [ ] Navigatie tabs bovenaan linken naar alle pagina's

2. **Space Explorer** (`http://localhost:8765/explorer.html`)
   - [ ] Zonnestelsel canvas laadt met draaiende planeten
   - [ ] N-Body simulatie start met preset
   - [ ] Lichtsnelheid reis visualisatie werkt
   - [ ] Mars Rover sectie laadt foto's (NASA API)
   - [ ] Asteroiden sectie laadt NEO data (NASA API)

3. **Observatorium** (`http://localhost:8765/observatory.html`)
   - [ ] APOD foto van vandaag laadt (NASA API)
   - [ ] Deep Space: Hubble zoekfunctie werkt
   - [ ] Zon-activiteit: DONKI data laadt (zonnevlammen, CME's)
   - [ ] Alle 9 secties bereikbaar via sub-navigatie
   - [ ] Spectroscopie visualisatie werkt

4. **Equinox** (`http://localhost:8765/equinox.html`)
   - [ ] Countdown naar volgende equinox/zonnewende toont
   - [ ] Aardas kanteling animatie werkt
   - [ ] Daglengte grafiek rendert correct
   - [ ] Golden hour tijden kloppen

5. **Hemelkaart** (`http://localhost:8765/hemel.html`)
   - [ ] Live sterrenhemel rendert boven Nederland
   - [ ] Maanfase klopt met huidige datum
   - [ ] ISS positie laadt (Open Notify API)
   - [ ] NASA EPIC aarde foto's laden

6. **Zonnestelsel** (`http://localhost:8765/zonnestelsel.html`)
   - [ ] Planeten draaien in orbit animatie
   - [ ] Baansnelheid vergelijking zichtbaar
   - [ ] Planeet info correct weergegeven

7. **Foto's** (`http://localhost:8765/fotos.html`)
   - [ ] APOD van vandaag laadt automatisch
   - [ ] Navigatie (vorige/volgende) werkt
   - [ ] Datumkiezer werkt
   - [ ] Galerij laadt meerdere foto's

8. **Missies** (`http://localhost:8765/missies.html`)
   - [ ] Voyager 1 afstand berekening draait (real-time counter)
   - [ ] Missie overzicht toont alle actieve missies
   - [ ] Links en details correct

9. **Donkere Hemel** (`http://localhost:8765/donkerehemel.html`)
   - [ ] Lichtvervuiling kaart laadt en is interactief
   - [ ] Bortle-schaal uitleg zichtbaar
   - [ ] NL sterrenkijkplekken getoond
   - [ ] Tips en uitrusting secties compleet

### API Health Check
- [ ] NASA APOD: open fotos.html, foto moet laden (DEMO_KEY rate limit: 30/uur)
- [ ] NASA NEO: open explorer.html > Asteroiden
- [ ] NASA DONKI: open observatory.html > Zon-activiteit
- [ ] NASA Mars: open explorer.html > Mars Rover
- [ ] HubbleSite: open observatory.html > Deep Space > zoek iets
- [ ] Open Notify ISS: open hemel.html, ISS positie moet laden
- [ ] NASA EPIC: open hemel.html, aarde foto's moeten laden

## TODO

- [ ] Eigen NASA API key aanvragen (ter vervanging van DEMO_KEY, hogere rate limits)
- [ ] Shared CSS/JS extraheren (nu duplicatie tussen 9 standalone HTML bestanden)
- [ ] Service Worker toevoegen voor offline gebruik
- [ ] Performance: lazy loading voor Canvas animaties die niet in beeld zijn
- [ ] Meer melkweg-types in observatory.html
- [ ] GBIF integratie (biodiversiteit data koppelen aan lichtvervuiling)
- [ ] Webb telescope recente ontdekkingen feed

## Belangrijke Notities

- **Eigenaar verjaardag**: 5 mei - Eta Aquariden meteorenzwerm (brokstukken van komeet Halley!)
- **Horoscoop = astronomie**: De horoscoop-functie toont echte hemelposities op geboortedatum, inclusief precessie-uitleg. Geen astrologische claims.
- **Port 8765**: Vast poortnummer, niet wijzigen
- **DEMO_KEY**: Alle NASA API's gebruiken DEMO_KEY. Bij rate limiting (HTTP 429) even wachten.
- **Geen dependencies**: Geen npm install, geen build, geen node_modules. Alles draait puur op HTML/CSS/JS.
- **Bestanden zijn groot**: Elke HTML pagina bevat alle CSS en JS inline (14-114 KB per bestand).
- **GitHub Pages**: Draait direct vanaf main branch, geen build stap nodig.

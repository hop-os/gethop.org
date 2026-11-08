# gethop.org bijwerken

Het draaiboek om de site gelijk te trekken met HopOS, HOP en SURF. Volg het
van boven naar beneden; elke stap zegt waar de waarheid staat. De site is
Engels, dit draaiboek en de commits zijn Nederlands.

## 0. Wat er op de site staat, en waar het vandaan komt

| Pagina | Wat | Bron |
| --- | --- | --- |
| `/index.html` | de drie projecten naast elkaar | de drie README's |
| `/hopos/` | HopOS: model, flip, Rust, Go, netwerk, metingen, apps, borden, downloads | `hop-os/HopOS` |
| `/hop/` | HOP: drivers, verkiezing en herstel, CLI, downloads | `hop-os/hop` |
| `/surf/` | SURF: desktop, protocollen, apps | `hop-os/HopOS-surf` |
| `/hopos/docs/`, `/hop/docs/` | de docs-viewer (`viewer.js`): leest Markdown van `main` op GitHub | `data-repo` en `data-docs` op de `<body>` |

De docs-pagina's hoef je niet bij te werken: die lezen live van GitHub. Wel
moeten de links ernaartoe (`/hopos/docs/#pagina:kop`) nog bestaan; stap 4
toetst dat.

Lokaal staan de bronnen naast deze repo:

```
../hop-os        github.com/hop-os/HopOS   (HopOS, de kern)
../hop/hop       github.com/hop-os/hop     (HOP, de orchestrator)
../hop-os-surf   github.com/hop-os/HopOS-surf
../hop-imager    github.com/hop-os/hop-imager
../stulp         github.com/haas-software/stulp
```

Lees de bronnen zoals ze op GitHub `main` staan (`git fetch` en dan
`origin/main`), niet een lokale werkboom met ongepushte commits: de site
belooft wat iedereen kan downloaden en lezen.

## 1. Wat is er veranderd sinds de vorige update

De vorige update staat bovenaan [PROPOSAL.md](PROPOSAL.md) (het logboek van
de site), met datum. Vanaf die datum:

```sh
cd ../hop-os && git fetch -q && git log --since=<datum> --format='%h %cs %s' origin/main | cut -c1-200
cd ../hop/hop && git fetch -q && git log --since=<datum> --format='%h %cs %s' origin/main | cut -c1-200
gh release list -R hop-os/HopOS -L 5; gh release list -R hop-os/hop -L 5; gh release list -R hop-os/hop-imager -L 3
```

Let vooral op commits met een versie (`3.x.y`, `-rcN`), en op woorden als
*weg*, *altijd*, *geen ... meer*, *naar een eigen repo*: dat zijn de
veranderingen die een zin op de site onwaar maken.

## 2. De bronnen per bewering

Loop de site per sectie langs met deze bronnen ernaast. Een bewering die je
niet in een bron terugvindt, gaat eruit of wordt zwakker.

**HopOS** (`../hop-os`):

- Model, kern als mechanisme, HOP als eerste bewoner: `README.md`.
- Wat er nog niet werkt, per bord: `ALLES.md` (de tabel kan achterlopen;
  de commits en `docs/boards-*.md` zijn nieuwer).
- Interrupts, borden, wat op ijzer gezien is: `docs/boards.md` (UEFI: O6N,
  Altra), `docs/boards-pi.md`, `docs/boards-radxa.md`,
  `docs/boards-riscv.md`, `docs/boards-apple.md` (M4). Zoek op
  *op ijzer*, *NOG NIET*, *ONGETOETST*.
- De flip: `docs/flip.md`. Go-apps: `docs/go-apps.md`.
- Metingen: `docs/measurements.md`, kolom *Hoogste v3* met stempel en
  datum. Een getal op de site komt daar letterlijk vandaan, met de opzet in
  het uitklapblok "What these numbers include".
- Rust-regels: `../rustdoc/README.md` en `[workspace.lints]` in `Cargo.toml`.
- Apps in de boom: `apps/` en `go/`; de releasebestanden:
  `gh release view -R hop-os/HopOS --json assets -q '.assets[].name'`.

**HOP** (`../hop/hop`):

- Indeling, CLI, artifacts, herstart onder de apps, cluster: `README.md`.
- CLI-voorbeelden: `cli/src/main.rs` (de usage-tekst en de tabelkoppen).
- Update-strategieën: `types/src/job.rs`.
- De apps die HOP meelevert: `apps/` en de releasebestanden
  (`gh release view -R hop-os/hop --json assets -q '.assets[].name'`).
- Het herstelgetal (17,3 s, 126 jobs) is van de Go-generatie; vervang het
  pas als er een meting van de Rust-generatie is.

**SURF**: `../hop-os-surf/README.md`. SURF is nog Go (de vorige generatie);
verander alleen wat daar verandert.

**Overig**: Stulp is Rust (`../stulp/ARCHITECTURE.md`); het Go-voorbeeld op
HopOS is cloudflared via TamaGo. De Imager: welke smaken en
bestandsnamen hij kent staat in `../hop-imager/internal/release/release.go`;
de site linkt naar `releases/latest` van de Imager, dus nieuwe
Imager-functies tellen pas na een Imager-release.

## 3. Schrijven

- Engels, kort, zonder voorbehoud dat de bron niet heeft. Geen "coming
  soon", geen tussenstand van een onderzoek: wat af is staat erop, wat niet
  af is staat er niet op of als beperking.
- Getallen met hun bron en datum in het uitklapblok, niet in de kop.
- Versienummers alleen waar het niet anders kan (het `hop agents`-voorbeeld);
  downloadlinks via `releases/latest/download/<naam>`, zodat ze meegaan.
- Download-bestandsnamen: neem ze over uit de laatste release, niet uit je
  hoofd. HopOS v3 heet `hopos-<bord>-headless.img.gz` en
  `hopos-<bord>-headfull.img.gz`, met de borden `rpi5`, `rpi4`, `radxa`,
  `o6n`, `altra`, `licheerv` en `apple`.
- Verander je `style.css` of `viewer.js`, verhoog dan het `?v=` in **alle**
  pagina's (ook `*/docs/index.html`), anders houden browsers de oude.

## 4. Controleren

Vanuit de root van deze repo:

```sh
python3 tools/check.py          # elke link, elk anker, elke docs-route; moet "groen" zeggen
node --check viewer.js
git diff --check
```

`tools/check.py` haalt elke externe link op (ook de downloads), toetst elk
anker en elke `/hopos/docs/#pagina:kop` tegen de Markdown op GitHub `main`.

Dan de pagina's zelf:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`, `/hopos/`, `/hop/`, `/surf/`, `/hopos/docs/`
en `/hop/docs/` op 1440 px en op 390 px (devtools, of Chrome headless). Op
390 px mag niets horizontaal scrollen: in de console moet
`document.documentElement.scrollWidth` gelijk zijn aan `clientWidth`.

## 5. Vastleggen

1. Zet bovenaan [PROPOSAL.md](PROPOSAL.md) een sectie
   `# Update — <datum>: <onderwerp>` met: welke versies de site nu beschrijft,
   per bewering die veranderde de bron, en wat de controle gaf.
2. Commit in het Nederlands, zoals de geschiedenis. GitHub Pages publiceert
   `main` vanzelf; `CNAME` kiest gethop.org.
3. Kijk na het pushen op https://gethop.org of de pagina's de nieuwe tekst
   tonen (Pages heeft een minuut nodig).

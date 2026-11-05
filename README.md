# Katarína Ostrožlíková: portfolio

Kompletní statický web v podobě retro televize. Součástí jsou projekty, textové CV, kontakty, pohyblivé lesní pozadí, přepínání stránek se zrněním a tři hudební smyčky. Na mobilu jsou dole Previous, Next a kolečko Music. Hudba se spouští až po kliknutí.

## Nahrání na GitHub

1. Rozbalte ZIP do počítače.
2. Do svého repozitáře nahrajte obsah rozbalené složky. `index.html` a `portfolio.json` mají být přímo v kořeni repozitáře, vedle složky `assets/`.
3. Zachovejte všechny soubory a podsložky včetně `.nojekyll`. Web nepotřebuje instalaci balíčků, databázi ani build.

Pro GitHub Pages otevřete **Settings → Pages → Build and deployment → Deploy from a branch**, vyberte větev s webem, složku **/(root)** a uložte. Po zveřejnění použijte skutečnou adresu, kterou zobrazí GitHub. Cesty k obrázkům, hudbě a profilovému JSONu jsou relativní, takže web funguje také v podadresáři projektu.

Oficiální postup: [GitHub Pages: publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [static files and .nojekyll](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Připojení ke galerii FMK

Profil je v `portfolio.json`. Má přesně osm polí požadovaných zadáním. Použité údaje:

| Pole | Hodnota |
| --- | --- |
| `name` | Katarína Ostrožlíková |
| `studyProgram` | Marketingové komunikace |
| `bio` | Krátký český popis vycházející z portfolia, do 180 znaků |
| `countryCode` | SK, výslovně potvrzeno pro tento profil |
| `portfolioUrl` | Zatím `null`, veřejná adresa ještě není známá |
| `photoOriginal` | `assets/cv-portrait.webp`, skutečná fotografie autorky |
| `photoStamp` | `assets/fmk/portrait-stamp.png`, vytvořený razítkový portrét |

**Po veřejném zveřejnění doplňte do `portfolioUrl` skutečnou HTTPS adresu webu včetně případného podadresáře a koncového `/`.** Následně předejte organizátorovi adresu souboru `portfolio.json` na tomto webu. Soubor musí být dostupný bez přihlášení a vracet JSON, nikoli HTML. Dosavadní soukromý náhled není veřejnou adresou pro galerii.

Vzhled hlavního webu nepřebírá kartičku galerie. Razítkový portrét je pouze podkladem pro galerii; nenahrazuje úvodní ilustraci ani fotografii v CV. Automatické stahování a schvalování profilů řeší společná galerie, tento web pouze poskytuje data a obrázky. V galerii není třeba určovat pořadové číslo.

## Úprava profilu

`portfolio.json` je hlavní zdroj profilových dat. Stránka jej načítá při otevření a používá jeho jméno na úvodu, v CV, kontaktech a titulku stránky, obor v úvodu a CV a `photoOriginal` pro fotografii v CV. Název současného oboru se pro anglické rozhraní překládá v malé mapě v `index.html`. Český galerijní popisek nenahrazuje delší anglické úvodní texty.

V HTML je také automaticky připravená záložní kopie profilu pro práci bez sítě. Po změně JSONu ji společně s HTML metadaty obnovíte:

```sh
python3 scripts/sync-profile.py
python3 scripts/validate-profile.py
```

Tyto dva pomocné skripty používají jen standardní knihovnu Pythonu. Nejsou podmínkou hostování. Při změně jména, oboru nebo fotografie upravujte JSON, nikoli vygenerovanou kopii v HTML. Kontakty, delší životopis a projektové texty zůstávají samostatným obsahem `index.html`.

## Lokální náhled

Ve složce s `index.html` spusťte:

```sh
python3 -m http.server 8000
```

Otevřete `http://localhost:8000/`. Server zastavíte Ctrl+C. Při otevření HTML přímo jako souboru prohlížeč nemusí povolit načtení JSONu; použije se jeho záložní kopie.

## Soubory a obrázky

`index.html` obsahuje styly a skripty webu. `assets/` obsahuje všechny dodané vizuály, skutečný portrét, původní obrázek CV, lesní pozadí, hudbu a lokální font s licencí. `scripts/generate-soundtracks.py` uchovává zdroj pro již vytvořené hudební soubory; pro provoz webu jej není třeba spouštět. `docs/` dokumentuje vzhled a vytvoření razítkového portrétu.

Razítkový PNG má skutečnou průhlednost a rozměry **1122 × 1402 px**. Generátor dodal poměr velmi blízký 4:5, nikoli přesných 1200 × 1500 px ani matematicky přesné 4:5. Soubor nebyl natahován. Původní fotografie a ostatní obrázky zůstaly zachované. Pro novou razítkovou variantu použijte jiné jméno, například `portrait-stamp-v2.png`, a změňte pouze `photoStamp`.

Export neobsahuje `.git/`, přístupové údaje ani konfiguraci původního hostingu. Na GitHub nebyl z tohoto prostředí nahrán a na nové veřejné adrese zatím nebyl ověřen.

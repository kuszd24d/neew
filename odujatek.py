import random
import time

def lassu_szoveg(szoveg, kesleltetes=0.04):
    """Szöveg lassú kiírása drámai hatás kedvéért."""
    for karakter in szoveg:
        print(karakter, end='', flush=True)
        time.sleep(kesleltetes)
    print()

def bevezetes():
    """Bevezetés a játékhoz."""
    lassu_szoveg("Üdvözöllek, hős, az Odüsszeia kalandjában!\n")
    lassu_szoveg("Te vagy Odüsszeusz, Ithaka ravasz királya, akit bátorságáról és furfangjáról ismernek.\n")
    lassu_szoveg("Trója bukása után hosszú és veszélyes úton kell hazatérned Ithakába.\n")
    lassu_szoveg("Útközben istenek próbára tesznek, szörnyekkel és viharokkal kell szembenézned.\n")
    lassu_szoveg("A célod: túléld az utazást, és térj haza családodhoz.\n")
    lassu_szoveg("Készen állsz az epikus kalandra? (igen/nem)\n")

    while True:
        valasz = input("> ").lower()
        if valasz == "igen":
            lassu_szoveg("Az istenek mosolyognak rád. Kezdődjék az utazás!\n")
            break
        elif valasz == "nem":
            lassu_szoveg("Az istenek haragra gerjednek gyávaságod miatt. Viszlát, halandó!\n")
            exit()
        else:
            lassu_szoveg("Kérlek, válaszolj 'igen' vagy 'nem'.\n")

def talalkozasi_opciok(talalkozas_tipusa):
    """Találkozás-specifikus lehetőségek felajánlása."""
    if talalkozas_tipusa == "Küklopsz":
        lassu_szoveg("1. Harcolsz a Küklopsszal.\n2. Elbújsz a Küklopsz elől.\n3. Becsapod a Küklopszot egy ravasz hazugsággal.")
    elif talalkozas_tipusa == "Vihar":
        lassu_szoveg("1. Áthajózol a viharon.\n2. Imádkozol Poszeidónhoz kegyelemért.\n3. Lehorgonyzol és kivárod, míg elcsitul.")
    elif talalkozas_tipusa == "Szirének":
        lassu_szoveg("1. Bedugod a füled viasszal, és elhajózol mellettük.\n2. Dalpárbajra hívod a Sziréneket.\n3. Engedsz a daluk csábításának.")
    elif talalkozas_tipusa == "Szkülla és Kharübdisz":
        lassu_szoveg("1. Közelebb hajózol Szküllához (a hatfejű szörnyhöz).\n2. Közelebb hajózol Kharübdiszhez (az örvényhez).\n3. Megpróbálsz középen áthaladni.")
    elif talalkozas_tipusa == "Kirké":
        lassu_szoveg("1. Támadásba lendülsz Kirké ellen.\n2. Óvatosan kéred a segítségét.\n3. Elfogadod a lakomáját, és bízol benne.")

def valasztas_megoldasa(talalkozas_tipusa, valasztas, egeszseg):
    """A játékos választásának feldolgozása."""
    eredmenyek = {
        "Küklopsz": {
            1: (-30, "A Küklopsz túl erős! Alig menekülsz meg élve."),
            2: (-10, "Sikeresen elbújsz, de a Küklopsz elpusztítja a készleteidet."),
            3: (10, "Becsapod a Küklopszot azzal, hogy 'Senki'-nek nevezed magad, és sértetlenül elmenekülsz."),
        },
        "Vihar": {
            1: (-20, "A vihar megrongálja a hajódat, de túléled."),
            2: (-10, "Poszeidón meghallgatja imáidat, de csak részben enyhít a viharon."),
            3: (0, "Kivárod a vihart, és sértetlenül folytathatod az utat."),
        },
        "Szirének": {
            1: (0, "Bedugod a füled, és biztonságban elhajózol mellettük."),
            2: (10, "Megnyered a dalpárbajt, és a Szirének tisztelettel távoznak."),
            3: (-30, "A daluk csábításának engedsz, és alig menekülsz meg élve."),
        },
        "Szkülla és Kharübdisz": {
            1: (-20, "Szkülla hat emberedet felfalja, de a hajód megmenekül."),
            2: (-30, "Kharübdisz szinte elnyeli a hajódat, alig menekülsz meg."),
            3: (-10, "Középen próbálsz átkelni, kisebb károkat szenvedve."),
        },
        "Kirké": {
            1: (-20, "Támadást indítasz Kirké ellen, de embereid egy részét disznóvá változtatja."),
            2: (10, "Óvatosan kéred a segítségét, és tanácsokat ad az utadhoz."),
            3: (-10, "Túl könnyen megbízol benne, csapdába ejt, de végül megmenekülsz."),
        },
    }
    egeszseg_valtozas, eredmeny = eredmenyek[talalkozas_tipusa][valasztas]
    lassu_szoveg(eredmeny + f" (Egészség változás: {egeszseg_valtozas})\n")
    return egeszseg + egeszseg_valtozas

def veletlen_talalkozas():
    """Véletlenszerű találkozás generálása."""
    talalkozasok = ["Küklopsz", "Vihar", "Szirének", "Szkülla és Kharübdisz", "Kirké"]
    return random.choice(talalkozasok)

def jatek():
    """A játék fő ciklusa."""
    egeszseg = 100
    utazas_hossza = 5
    bevezetes()
    
    for lepes in range(1, utazas_hossza + 1):
        lassu_szoveg(f"\nUtazás {lepes}. szakasza a(z) {utazas_hossza}-ból...\n")
        talalkozas_tipusa = veletlen_talalkozas()
        lassu_szoveg(f"Találkozol: {talalkozas_tipusa}!\n")
        
        talalkozasi_opciok(talalkozas_tipusa)
        
        while True:
            try:
                valasztas = int(input("\nVálassz egy lehetőséget (1/2/3): "))
                if valasztas in [1, 2, 3]:
                    break
                else:
                    lassu_szoveg("Kérlek, válassz egy érvényes opciót: 1, 2 vagy 3.\n")
            except ValueError:
                lassu_szoveg("Hibás bemenet. Kérlek, írj be 1-et, 2-t vagy 3-at.\n")
        
        egeszseg = valasztas_megoldasa(talalkozas_tipusa, valasztas, egeszseg)
        lassu_szoveg(f"Jelenlegi egészséged: {egeszseg}/100\n")
        
        if egeszseg <= 0:
            lassu_szoveg("Belebuktál az utazásba. Az istenek szomorúan néznek rád.\n")
            lassu_szoveg("JÁTÉK VÉGE.\n")
            return

    lassu_szoveg("🏠 Végül, minden próba után, elérsz Ithakába!\n")
    lassu_szoveg("Penelopé és Télemakhosz örömmel fogadnak otthon. Az istenek tisztelik kitartásodat.\n")
    lassu_szoveg("Gratulálok, hős! Sikeresen befejezted az odüsszeiádat. 🎉\n")

if __name__ == "__main__":
    jatek()
igen

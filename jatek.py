import random
import time
from os import system

def lassu_szoveg(szoveg, kesleltetes=0.04):
    """Szöveg lassú kiírása drámai hatás kedvéért."""
    for karakter in szoveg:
        print(karakter, end='', flush=True)
        time.sleep(kesleltetes)
    print()

def tiszta_kepernyo():
    """Képernyő törlése a háttér kialakításához."""
    system('cls' if system == 'nt' else 'clear')

def bevezetes():
    """Bevezetés a játékhoz."""
    tiszta_kepernyo()
    lassu_szoveg("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      🏛️  ODÜSSZEIA  🏛️
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Az epikus kaland története alapján, melyben Te, Odüsszeusz,
    megpróbálsz hazatérni Ithakába Trója bukása után.

    Isteni próbák, szörnyek és hatalmas veszélyek várnak rád!
    Célod: túlélni és hazatérni Penelopéhoz és Télemakhoszhoz.

    Készen állsz az utazásra? (igen/nem)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    while True:
        valasz = input("> ").lower()
        if valasz == "igen":
            lassu_szoveg("\nAz istenek rád mosolyognak. Kezdjük!\n")
            break
        elif valasz == "nem":
            lassu_szoveg("\nAz istenek haragra gerjednek gyávaságod miatt. Viszlát!\n")
            exit()
        else:
            lassu_szoveg("Kérlek, válaszolj 'igen' vagy 'nem'.\n")

def talalkozasi_opciok(talalkozas_tipusa):
    """Találkozás-specifikus lehetőségek."""
    if talalkozas_tipusa == "Küklopsz":
        lassu_szoveg("1. Harcolsz a Küklopsszal.\n2. Elbújsz előle.\n3. Becsapod őt egy hazugsággal.")
    elif talalkozas_tipusa == "Vihar":
        lassu_szoveg("1. Áthajózol a viharon.\n2. Imádkozol Poszeidónhoz.\n3. Kivárod, míg elcsendesedik.")
    elif talalkozas_tipusa == "Szirének":
        lassu_szoveg("1. Viasszal bedugod a füled.\n2. Dalpárbajt kezdeményezel.\n3. Engedsz a csábításnak.")
    elif talalkozas_tipusa == "Szkülla és Kharübdisz":
        lassu_szoveg("1. Közelebb mész Szküllához.\n2. Közelebb mész Kharübdiszhez.\n3. Középen próbálsz áthaladni.")
    elif talalkozas_tipusa == "Kirké":
        lassu_szoveg("1. Támadsz.\n2. Óvatosan segítséget kérsz.\n3. Elfogadod a lakomáját.")

def valasztas_megoldasa(talalkozas_tipusa, valasztas, egeszseg):
    """A játékos választásának feldolgozása."""
    eredmenyek = {
        "Küklopsz": {
            1: (-30, "A Küklopsz túl erős, alig menekülsz!"),
            2: (-10, "Sikerül elbújnod, de elveszíted néhány készletedet."),
            3: (10, "Becsapod, és biztonságban elmenekülsz."),
        },
        "Vihar": {
            1: (-20, "A vihar megrongálja a hajódat, de túléled."),
            2: (-10, "Az ima enyhíti a vihart, de a károk jelentősek."),
            3: (0, "Biztonságban kivárod a vihart."),
        },
        "Szirének": {
            1: (0, "Viasszal bedugod a füled, és sértetlenül elhaladsz."),
            2: (10, "Megnyered a dalpárbajt, és továbbutazhatsz."),
            3: (-30, "Engedsz a daluknak, és alig menekülsz meg."),
        },
        "Szkülla és Kharübdisz": {
            1: (-20, "Szkülla hat embert elragad, de a hajód megmenekül."),
            2: (-30, "Kharübdisz szinte elnyeli a hajót!"),
            3: (-10, "Kisebb károkat szenvedsz, de átvészelsz mindent."),
        },
        "Kirké": {
            1: (-20, "Támadásod miatt átkot szór rád."),
            2: (10, "Óvatos vagy, és tanácsokat kapsz tőle."),
            3: (-10, "Túl könnyen bízol benne, majdnem csapdába esel."),
        },
    }
    egeszseg_valtozas, eredmeny = eredmenyek[talalkozas_tipusa][valasztas]
    lassu_szoveg(eredmeny + f" (Egészség változás: {egeszseg_valtozas})\n")
    return egeszseg + egeszseg_valtozas

def jatek():
    """A játék fő ciklusa."""
    egeszseg = 100
    talalkozasok = ["Küklopsz", "Vihar", "Szirének", "Szkülla és Kharübdisz", "Kirké"]
    veletlen_talalkozasok = random.sample(talalkozasok, len(talalkozasok))

    bevezetes()

    for talalkozas_tipusa in veletlen_talalkozasok:
        tiszta_kepernyo()
        lassu_szoveg(f"Új szakasz! Találkozol: {talalkozas_tipusa}!\n")
        talalkozasi_opciok(talalkozas_tipusa)

        while True:
            try:
                valasztas = int(input("\nVálassz egy lehetőséget (1/2/3): "))
                if valasztas in [1, 2, 3]:
                    break
                else:
                    lassu_szoveg("Kérlek, válassz egy érvényes opciót: 1, 2 vagy 3.\n")
            except ValueError:
                lassu_szoveg("Hibás bemenet. Kérlek, írj be egy számot (1/2/3).\n")

        egeszseg = valasztas_megoldasa(talalkozas_tipusa, valasztas, egeszseg)
        lassu_szoveg(f"Jelenlegi egészséged: {egeszseg}/100\n")

        if egeszseg <= 0:
            lassu_szoveg("\nElbuktál az utazásban. Az istenek szomorúan néznek rád.\n")
            lassu_szoveg("JÁTÉK VÉGE.\n")
            return

    lassu_szoveg("\n🏠 Ithaka szigetére érkezel, és Penelopé örömmel fogad!\n")
    lassu_szoveg("Gratulálok, hős! Sikeresen teljesítetted az Odüsszeiát! 🎉\n")

if __name__ == "__main__":
    jatek()

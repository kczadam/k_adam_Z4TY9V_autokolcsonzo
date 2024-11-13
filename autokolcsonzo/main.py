from datetime import datetime
from classes import Autokolcsonzo, Szemelyauto, Teherauto


def main():
    # Autókölcsönző példányosítása és autók hozzáadása
    kolcsonzo = Autokolcsonzo("Bérautók kft.")
    auto1 = Szemelyauto("QWE-123", "Opel Vectra", 5000, "benzin")
    auto2 = Teherauto("ASD-123", "Renault Traffic", 10000, "zárt/dobozos")
    auto3 = Szemelyauto("YXC-123", "Skoda Octavia", 7000, "dízel")

    kolcsonzo.autok_hozzaadasa(auto1)
    kolcsonzo.autok_hozzaadasa(auto2)
    kolcsonzo.autok_hozzaadasa(auto3)

    # Előre definiált bérlések
    kolcsonzo.berles_hozzaadasa(auto1, datetime(2024, 12, 1).date())
    kolcsonzo.berles_hozzaadasa(auto2, datetime(2024, 12, 5).date())
    kolcsonzo.berles_hozzaadasa(auto3, datetime(2024, 12, 15).date())
    kolcsonzo.berles_hozzaadasa(auto1, datetime(2024, 12, 20).date())

    # Felhasználói interfész
    while True:
        print("\n1. Autó bérlése\n2. Bérlés lemondása\n3. Bérlések listázása\n4. Kilépés")
        valasztas = input("Válasszon egy menüpontot: ")

        # Autó bérlése
        if valasztas == "1":
            rendszam = input("Adja meg a rendszámot: ")
            datum_str = input("Adja meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            except ValueError:
                print("Hiba: A dátum formátuma nem megfelelő. A helyes formátum: (ÉÉÉÉ-HH-NN)")
                continue

            auto = next((a for a in kolcsonzo.autok if a.rendszam == rendszam), None)
            if auto:
                kolcsonzo.berles_hozzaadasa(auto, datum)
            else:
                print("Ilyen rendszámú autó nem található a rendszerben.")

        # Bérlés lemondása
        elif valasztas == "2":
            rendszam = input("Adja meg a rendszámot: ")
            datum_str = input("Adja meg a lemondás dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            except ValueError:
                print("Hiba: A dátum formátuma nem megfelelő. A helyes formátum: (ÉÉÉÉ-HH-NN)")
                continue

            kolcsonzo.berles_lemondasa(rendszam, datum)

        # Bérlések listázása
        elif valasztas == "3":
            kolcsonzo.berlesek_listazasa()

        # Kilépés
        elif valasztas == "4":
            print("A kilépés sikeresen megtörtént.")
            break

        # Érvénytelen menüpont
        else:
            print("Érvénytelen menüpont. Elérhető menüpontok: 1, 2, 3, 4")

if __name__ == "__main__":
    main()
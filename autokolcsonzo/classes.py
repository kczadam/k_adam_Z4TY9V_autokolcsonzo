from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt autó osztály
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass

# Személyautó osztály
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, uzemanyag):
        super().__init__(rendszam, tipus, berleti_dij)
        self.uzemanyag = uzemanyag

    def __str__(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Üzemanyag: {self.uzemanyag}"

# Teherautó osztály
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, felepitmeny):
        super().__init__(rendszam, tipus, berleti_dij)
        self.felepitmeny = felepitmeny

    def __str__(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Felépítmény: {self.felepitmeny}"

# Bérlés osztály
class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        # Bérlés adatainak megjelenítése típus-specifikus információkkal
        if isinstance(self.auto, Szemelyauto):
            return f"Regisztrált bérlés - Rendszám: {self.auto.rendszam}, Dátum: {self.datum}"
        elif isinstance(self.auto, Teherauto):
            return f"Regisztrált bérlés - Rendszám: {self.auto.rendszam}, Dátum: {self.datum}"
        else:
            return f"Regisztrált bérlés - Rendszám: {self.auto.rendszam}, Dátum: {self.datum}"
# Autókölcsönző osztály
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    def berles_hozzaadasa(self, auto, datum):
        ma = datetime.now().date()
        if datum < ma:
            print("Hiba: A bérlés dátuma nem lehet az aktuális dátumnál korábbi.")
            return None

        if any(b.auto.rendszam == auto.rendszam for b in self.berlesek if b.datum == datum):
            print(f"Hiba: {auto.rendszam} rendszámú autó/teherautó már foglalt ezen a napon: {datum}")
            return None

        berles = Berles(auto, datum)
        self.berlesek.append(berles)

        # Sikeres bérlés üzenet
        if isinstance(auto, Szemelyauto):
            print(f"Sikeres bérlés: Rendszám: {auto.rendszam} - Típus: {auto.tipus} - Bérleti díj: {auto.berleti_dij} Ft/nap - Bérlés dátuma: {datum} - Üzemanyag: {auto.uzemanyag}")
        elif isinstance(auto, Teherauto):
            print(f"Sikeres bérlés: Rendszám: {auto.rendszam} - Típus: {auto.tipus} - Bérleti díj: {auto.berleti_dij} Ft/nap - Bérlés dátuma: {datum} - Felépítmény: {auto.felepitmeny}")
        else:
            print(f"Sikeres bérlés: Rendszám: {auto.rendszam} - Típus: {auto.tipus} - Bérleti díj: {auto.berleti_dij} Ft/nap - Bérlés dátuma: {datum}")

        return berles

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print(f"Bérlés törölve: {rendszam} - {datum}")
                return
        print("Ilyen bérlés nem található a rendszerben.")

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincs egyetlen bérlés sem a rendszerben.")
        for berles in self.berlesek:
            print(berles)

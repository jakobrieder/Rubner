from enum import Enum


class Geschlecht(Enum):
    MAENNLICH = "Männlich"
    WEIBLICH = "Weiblich"


class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht):
        super().__init__(name, geschlecht)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht):
        super().__init__(name, geschlecht)


class Abteilung:
    def __init__(self, name, leiter):
        if not isinstance(leiter, Abteilungsleiter):
            raise ValueError("Leiter muss Abteilungsleiter sein.")
        self.name = name
        self.leiter = leiter
        self.mitarbeiter_liste = [leiter]

    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        if isinstance(mitarbeiter, Mitarbeiter):
            self.mitarbeiter_liste.append(mitarbeiter)

    def get_anzahl_mitarbeiter(self):
        return len(self.mitarbeiter_liste)

    def get_geschlechter_statistik(self):
        m = sum(1 for p in self.mitarbeiter_liste if p.geschlecht == Geschlecht.MAENNLICH)
        f = sum(1 for p in self.mitarbeiter_liste if p.geschlecht == Geschlecht.WEIBLICH)
        return m, f


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufuegen(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_anzahl_abteilungen(self):
        return len(self.abteilungen)

    def get_gesamt_mitarbeiter_anzahl(self):
        return sum(abt.get_anzahl_mitarbeiter() for abt in self.abteilungen)

    def get_anzahl_abteilungsleiter(self):
        return len(self.abteilungen)

    def get_groesste_abteilung(self):
        if not self.abteilungen:
            return None
        return max(self.abteilungen, key=lambda abt: abt.get_anzahl_mitarbeiter())

    def get_geschlechter_verteilung(self):
        gesamt_m = 0
        gesamt_f = 0
        for abt in self.abteilungen:
            m, f = abt.get_geschlechter_statistik()
            gesamt_m += m
            gesamt_f += f

        total = gesamt_m + gesamt_f
        if total == 0:
            return 0.0, 0.0

        return (gesamt_m / total) * 100, (gesamt_f / total) * 100


meine_firma = Firma("Tech Solutions")

leiter_it = Abteilungsleiter("Alice", Geschlecht.WEIBLICH)
leiter_hr = Abteilungsleiter("Bob", Geschlecht.MAENNLICH)

it = Abteilung("IT", leiter_it)
hr = Abteilung("HR", leiter_hr)

it.mitarbeiter_hinzufuegen(Mitarbeiter("Charlie", Geschlecht.MAENNLICH))
it.mitarbeiter_hinzufuegen(Mitarbeiter("Diana", Geschlecht.WEIBLICH))
it.mitarbeiter_hinzufuegen(Mitarbeiter("Erik", Geschlecht.MAENNLICH))
hr.mitarbeiter_hinzufuegen(Mitarbeiter("Fiona", Geschlecht.WEIBLICH))

meine_firma.abteilung_hinzufuegen(it)
meine_firma.abteilung_hinzufuegen(hr)

print(f"Firma: {meine_firma.name}")
print(f"Abteilungen: {meine_firma.get_anzahl_abteilungen()}")
print(f"Mitarbeiter gesamt: {meine_firma.get_gesamt_mitarbeiter_anzahl()}")
print(f"Abteilungsleiter: {meine_firma.get_anzahl_abteilungsleiter()}")

groesste = meine_firma.get_groesste_abteilung()
if groesste:
    print(f"Größte Abteilung: {groesste.name} ({groesste.get_anzahl_mitarbeiter()} Personen)")

m_prozent, f_prozent = meine_firma.get_geschlechter_verteilung()
print(f"Verteilung: Männer {m_prozent:.1f}% / Frauen {f_prozent:.1f}%")
names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

# 1. ZIP: Daten zusammenfügen
# Erzeugt Tupel wie: ("Anna", 23, 88)
gezippte_daten = zip(names, ages, scores)

# 2. FILTER: Bedingungen prüfen (Alter >= 18 UND Score >= 80)
# Wir greifen auf Index 1 (Alter) und Index 2 (Score) zu
gefilterte_daten = filter(lambda x: x[1] >= 18 and x[2] >= 80, gezippte_daten)

# 3. MAP: In Dictionary umwandeln
# Wir bauen aus dem Tupel x ein Dictionary
ergebnis_iterator = map(lambda x: {"name": x[0], "age": x[1], "score": x[2]}, gefilterte_daten)

# Um das Ergebnis sehen zu können, müssen wir es in eine Liste umwandeln
ergebnis_liste = list(ergebnis_iterator)

# Ausgabe
import pprint # Nur für schöne Ausgabe untereinander
pprint.pprint(ergebnis_liste)
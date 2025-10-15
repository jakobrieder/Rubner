
# Beispielhafte Temperaturwerte (z. B. aus Sensor gelesen)
temperaturen = [5, 12, 25, 28, 33, 8, 25, 33, 40]

# LIST COMPREHENSION: Bewertung der Temperatur
# kalt, angenehm oder heiß
statusListe = [
  "kalt" if t < 10 else "angenehm" if t > 30 else "heiß"
  for t in temperaturen
]

print("Temperaturstatus:", statusListe)


# SET COMPREHENSION: Eindeutige, auffällige Werte filtern - unique Werte
# (Temperaturen über 25 °C)
wichtigeWerte = {t for t in temperaturen if t > 25}

print("Wichtige (heiße) Werte:", wichtigeWerte)

# DICT COMPREHENSION: LEDs den Helligkeiten zuordnen
# Beispiel: je heißer der Wert, desto heller die LED
# Werte werden auf 0–255 normiert
ledHelligkeit = {
  i: int((t / max(temperaturen)) * 255)
  for i, t in enumerate(temperaturen)
}
print("LED-Helligkeiten:", ledHelligkeit)


import random
from collections import defaultdict


# ==============================================================
# Methode: Eine einzelne Zahl aus dem Pool ziehen
# Zweck: Wählt eine zufällige Zahl aus dem Pool und entfernt sie
# Eingabe:
#   rng - Zufallsgenerator
#   pool - aktuelle Liste mit noch verfügbaren Zahlen
#   remaining - wie viele Zahlen noch im Pool übrig sind
# Rückgabe:
#   gezogene Zahl
# ==============================================================

def draw_one_number(rng, pool, remaining):
    idx = rng.randrange(remaining)   # zufälliger Index aus den noch übrig gebliebenen
    number = pool.pop(idx)           # Zahl aus dem Pool entfernen
    return number


# ==============================================================
# Methode: Eine komplette Lottoziehung
# Zweck: Zieht 'pick' verschiedene Zahlen aus 'numbers_total'
# Eingabe:
#   rng - Zufallsgenerator
#   numbers_total - wie viele Zahlen gibt es insgesamt (z.B. 45)
#   pick - wie viele Zahlen sollen gezogen werden (z.B. 6)
# Rückgabe:
#   Liste mit gezogenen Zahlen
# ==============================================================

def draw_one_lotto(rng, numbers_total, pick):
    pool = list(range(1, numbers_total + 1))  # Zahlen 1 bis numbers_total
    result = []
    remaining = numbers_total

    for _ in range(pick):
        number = draw_one_number(rng, pool, remaining)  # einzelne Zahl ziehen
        result.append(number)                           # speichern
        remaining -= 1                                  # eine Zahl weniger im Pool

    return result


# ==============================================================
# Methode: Simulation vieler Ziehungen
# Zweck: Führt mehrere Ziehungen durch und zählt, wie oft jede Zahl vorkommt
# Eingabe:
#   num_draws - Anzahl der Ziehungen (z.B. 1000)
#   rng - Zufallsgenerator
#   numbers_total - Gesamtanzahl möglicher Zahlen (z.B. 45)
#   pick - Anzahl gezogener Zahlen pro Ziehung (z.B. 6)
# Rückgabe:
#   Dictionary mit Zahlen als Schlüssel und Häufigkeit als Wert
# ==============================================================

def run_simulation(num_draws, rng, numbers_total, pick):
    stats = defaultdict(int)  # Dictionary: Zahl -> Häufigkeit

    for _ in range(num_draws):
        draw = draw_one_lotto(rng, numbers_total, pick)
        for n in draw:
            stats[n] += 1  # Zähler hochsetzen

    return stats


# ==============================================================
# Hauptprogramm
# Zweck: Führt die Simulation aus und gibt die Ergebnisse aus
# ==============================================================

def main():
    rng = random.Random()    # Zufallsgenerator
    numbers_total = 45       # Anzahl möglicher Zahlen
    pick = 6                 # Wie viele pro Ziehung
    num_draws = 1000         # Anzahl der Ziehungen

    stats = run_simulation(num_draws, rng, numbers_total, pick)

    print(f"Häufigkeiten nach {num_draws} Ziehungen:")
    for n in range(1, numbers_total + 1):
        print(f"Zahl {n:2d}: {stats[n]:4d} mal")


# Starte Hauptprogramm
if __name__ == "__main__":
    main()

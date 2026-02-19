import time
import Poker

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Hochleistungs-Stoppuhr
        result = func(*args, **kwargs)  # Die eigentliche Funktion ausführen
        end_time = time.perf_counter()  # Endzeit merken

        print(f"\n Ein einzelner Aufruf von '{func.__name__}' dauerte {end_time - start_time:.8f} Sekunden.")
        return result
    return wrapper


Poker.shuffleAndDraw = timer_decorator(Poker.shuffleAndDraw)

if __name__ == "__main__":
    print("Messe nur die Zeit von shuffleAndDraw()")

    gezogene_karten = Poker.shuffleAndDraw()

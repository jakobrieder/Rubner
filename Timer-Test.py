import time
import Poker

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ergebnis = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"\n Ein einzelner Aufruf von '{func.__name__}' dauerte {end_time - start_time:.8f} Sekunden.")
        return ergebnis
    return wrapper


Poker.shuffleAndDraw = timer_decorator(Poker.shuffleAndDraw)

if __name__ == "__main__":
    gezogene_karten = Poker.shuffleAndDraw()

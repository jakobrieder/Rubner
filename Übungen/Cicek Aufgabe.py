import sys


def temp(temperaturen):
    count = 0
    tempListe = [] # Liste parsen wenn andere Werte etc. mit try-except

    for j in temperaturen:
        if -60 <= j <= 60:
            tempListe.append(j)
        else:
            count = count + 1

    return count, tempListe


def avg(numbers):
    if len(numbers) == 0:
        return None
    avgValue = sum(numbers) / len(numbers)
    return avgValue


def main():
    temperaturen = [30, 60, 72, -123, -43]

    count, temp1 = temp(temperaturen)
    print(count)
    print(temp1)

    numbers1 = avg(temp1)
    print(numbers1)

if __name__ == '__main__':
    try:
        main()
    except:
        print("Fehler")
        sys.exit(1) # damit wir nich mit einem 0 terminieren

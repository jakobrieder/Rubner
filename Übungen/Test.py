def auswertung(list_zahlen, wunsch_summe):
    paare = []
    for i in range(len(list_zahlen)):
        for j in range(len(list_zahlen)):
            if list_zahlen[i] + list_zahlen[j] == wunsch_summe:
                paare.sort()
                paare.append((list_zahlen[i], list_zahlen[j]))

    if paare:
        return set(paare)
    return None


def ausgabe():
    pass


def main():
    list_zahlen = [12, 3, 5, 7, 2, 13, 0, 8, 4, 6, 10, 11, 1, 9]
    wunschsumme = 12
    liste_auswertung = auswertung(list_zahlen, wunschsumme)
    print(liste_auswertung)


if __name__ == "__main__":
    main()

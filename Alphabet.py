# Diese Methode erzeugt eine Dictionary es wird in letters die Liste mit den Buchstaben übergeben und es wird das Dictionary returned
def createAlphabetDict(letters):
    return {letter: index + 1 for index, letter in enumerate(letters)} # enumerate liefert den Index und das Element; +1 damit es nicht bei 0 losgeht


#Ausgabe des Dictionarys
def printDictionary(dictionary):
    for key, value in dictionary.items(): # dictionary.items() - liefert die Werte als Iterable dict_items([('a', 1), ('b', 2)])
        print(f"{key}: {value}")


#Main
def main():
    #Liste mit Buchstaben
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    #Dictionary erstellen mit der Liste aus Buchstaben
    alphabetDict = createAlphabetDict(letters)
    #Ausgabe der Liste
    printDictionary(alphabetDict)

if __name__ == "__main__":
    main()


def createUniqueSet(items):
    return {item for item in items} # Set-Comprehension



def printSet(uniqueItems):
    for element in uniqueItems:
        print(element)

def main():
    sampleList = [1, 2, 2, 3, 4, 4, 5]
    #Ausführung uniqueSet
    uniqueItems = createUniqueSet(sampleList)
    #Ausgeben der uniquen Liste
    printSet(uniqueItems)


if __name__ == "__main__":
    main()

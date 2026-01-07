# Basisklasse
class Mensch:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def atmen(self):
        print(f"{self.name} atmet ruhig.")

# Erbt von Mensch
class Person(Mensch):
    def __init__(self, name, alter, wohnort):
        super().__init__(name, alter)
        self.wohnort = wohnort

    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}, {self.alter} Jahre alt und komme aus {self.wohnort}.")

# Erbt von Person
class Schueler(Person):
    def __init__(self, name, alter, wohnort, klasse):
        super().__init__(name, alter, wohnort)
        self.klasse = klasse

    def lernen(self):
        print(f"{self.name} lernt gerade für die {self.klasse}.")




max_mustermann = Schueler("Max", 16, "Berlin", "10b")


max_mustermann.atmen()
max_mustermann.vorstellen()
max_mustermann.lernen()
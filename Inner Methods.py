class Schildermaschine:
# Idee des Codes ist von KI

    def __init__(self, macher):
        self.macher = macher  # Global Namespace

    def schilder_drucken(self, *woerter, **einstellungen):
        def verschönern(text): # innere Methode
            symbol = einstellungen.get("deko", ">")
            return symbol + " " + str(text)
        print("Maschine von " + self.macher + " läuft")
        fertige_schilder = []
        for einzelwort in woerter:
            neues_schild = verschönern(einzelwort)
            fertige_schilder.append(neues_schild)
            print("Drucke: " + neues_schild)
        return fertige_schilder


if __name__ == "__main__":
    meine_maschine = Schildermaschine("Hannes")
    meine_maschine.schilder_drucken("Küche", "Bad", "Ausgang")
    meine_maschine.schilder_drucken(
        "Vorsicht", "Stopp",
        deko="!!!"
    )
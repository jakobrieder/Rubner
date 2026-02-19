class Schildermaschine:


    def __init__(self, macher):
        self.macher = macher  # Globaler Namespace

    def schilder_drucken(self, *woerter, **einstellungen):


        def verschönern(text): # innere Methode
            symbol = einstellungen.get("deko", ">") # wenn nichts übergeben dann standard zeichen
            return symbol + " " + str(text)

        print("Maschine von " + self.macher + " läuft")

        # Verarbeitung der args
        fertige_schilder = []
        for einzelwort in woerter:
            neues_schild = verschönern(einzelwort)
            fertige_schilder.append(neues_schild)
            print("Drucke: " + neues_schild)

        return fertige_schilder


# --- Demonstration der Verwendung ---
if __name__ == "__main__":
    meine_maschine = Schildermaschine("Hannes")
    #args
    meine_maschine.schilder_drucken("Küche", "Bad", "Ausgang")

    print("\n" + "-" * 20 + "\n")
    #kwargs
    meine_maschine.schilder_drucken(
        "Vorsicht", "Stopp",
        deko="!!!"
    )
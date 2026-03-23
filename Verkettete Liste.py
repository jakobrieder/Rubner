class Knoten:
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.naechster = None

    def setze_naechsten(self, naechster):
        self.naechster = naechster

    def hole_naechsten(self):
        return self.naechster

    def hole_wert(self):
        return self.inhalt

class MeineListe:
    def __init__(self):
        self.kopf_knoten = Knoten("Kopf")
        self.anzahl = 0

    def hole_erstes(self):
        return self.kopf_knoten

    def anhaengen(self, inhalt):
        neuer_knoten = Knoten(inhalt)
        letztes = self.hole_letztes()
        letztes.setze_naechsten(neuer_knoten)
        self.anzahl += 1

    def hole_letztes(self):
        zeiger = self.kopf_knoten
        while zeiger.hole_naechsten() is not None:
            zeiger = zeiger.hole_naechsten()
        return zeiger

    def einfuegen_nach(self, vorheriger_wert, neuer_wert):
        such_zeiger = self.kopf_knoten.hole_naechsten()
        while such_zeiger is not None and such_zeiger.hole_wert() is not vorheriger_wert:
            such_zeiger = such_zeiger.hole_naechsten()

        neuer_knoten = Knoten(neuer_wert)
        folge_knoten = such_zeiger.hole_naechsten()
        such_zeiger.setze_naechsten(neuer_knoten)
        neuer_knoten.setze_naechsten(folge_knoten)
        self.anzahl += 1

    def entferne(self, inhalt):
        zeiger = self.kopf_knoten
        while zeiger.hole_naechsten() is not None and zeiger.hole_wert() is not inhalt:
            if zeiger.hole_naechsten().hole_wert() is inhalt:
                if zeiger.hole_naechsten().hole_naechsten() is not None:
                    zeiger.setze_naechsten(zeiger.hole_naechsten().hole_naechsten())
                else:
                    zeiger.setze_naechsten(None)
                self.anzahl -= 1
                break
            zeiger = zeiger.hole_naechsten()

    def existiert(self, inhalt):
        zeiger = self.kopf_knoten
        while zeiger is not None:
            if zeiger.hole_wert() is inhalt:
                return True
            zeiger = zeiger.hole_naechsten()
        return False

    def suche(self, inhalt):
        zeiger = self.kopf_knoten
        while zeiger is not None:
            if zeiger.hole_wert() is inhalt:
                return zeiger
            zeiger = zeiger.hole_naechsten()
        return None

    def ausgeben(self):
        zeiger = self.kopf_knoten
        while zeiger is not None:
            print(zeiger.hole_wert())
            zeiger = zeiger.hole_naechsten()

    def hole_laenge(self):
        return self.anzahl

def main():
    meine_liste = MeineListe()
    meine_liste.anhaengen("1")
    meine_liste.anhaengen("2")
    meine_liste.anhaengen("3")
    meine_liste.anhaengen("4")
    meine_liste.anhaengen("5")
    meine_liste.einfuegen_nach("2","neu")
    meine_liste.ausgeben()
    meine_liste.entferne("3")
    meine_liste.ausgeben()

    print("count of elements:", meine_liste.hole_laenge())
    print("erstes Element: "+ meine_liste.hole_erstes().hole_wert())
    print("ist '3' enthalten?" + str(meine_liste.existiert("3")))
    print("ist '5' enthalten?" + str(meine_liste.existiert("5")))
    print("ist '5' enthalten?" + meine_liste.suche("5").hole_wert())
    print("letztes Element: " + meine_liste.hole_letztes().hole_wert())

if __name__ == "__main__":
    try:
        main()
    except:
        print("fehler")
class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        try:
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] += cantitate
            else:
                self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost adăugat cu succes.")
        except ValueError as e:
            print(f"Eroare: {e}")

    def cauta_produs(self, nume):
        try:
            if nume in self.produse:
                return f"Produs: {nume}, Cantitate: {self.produse[nume]}"
            else:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
        except KeyError as e:
            return f"Eroare: {e}"

    def actualizeaza_cantitatea(self, nume, cantitate):
        try:
            if nume not in self.produse:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            self.produse[nume] = cantitate
            print(f"Cantitatea produsului '{nume}' a fost actualizată cu succes.")
        except (KeyError, ValueError) as e:
            print(f"Eroare: {e}")

# Testare
inventar = Inventar()
inventar.adauga_produs("Mere", 10)
inventar.adauga_produs("Banane", 5)
print(inventar.cauta_produs("Mere"))
inventar.actualizeaza_cantitatea("Mere", 15)
print(inventar.cauta_produs("Mere"))
print(inventar.cauta_produs("Pere"))
inventar.adauga_produs("Pere", -5)

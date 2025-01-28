def suma_din_fisier(numere):
    try:
        suma = 0
        with open(numere, 'r') as fisier:
            for linie in fisier:
                try:
                    suma += float(linie.strip())
                except ValueError:
                    print(f"Eroare: Linia '{linie.strip()}' nu este un număr valid.")
        return suma
    except FileNotFoundError:
        return "Eroare: Fișierul nu există."
    except IOError:
        return "Eroare: Nu se poate citi fișierul."

# Testare
numere = "numere.txt"
print(suma_din_fisier(numere))

def imparte_numere(numar1, numar2):
    try:
        rezultat = numar1 / numar2
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă."
    except TypeError:
        return "Eroare: Trebuie să introduceți numere valide."

# Testare
print(imparte_numere(10, 2))  # Output: 5.0
print(imparte_numere(10, 0))  # Output: Eroare: Împărțirea la zero nu este permisă.
print(imparte_numere(10, "a"))  # Output: Eroare: Trebuie să introduceți numere valide.

# math_operations.py

def adunare(a, b):
    """Returnează suma a două numere."""
    return a + b

def scadere(a, b):
    """Returnează diferența dintre două numere."""
    return a - b

def inmultire(a, b):
    """Returnează produsul a două numere."""
    return a * b

def impartire(a, b):
    """Returnează câtul împărțirii a două numere. Dacă b este 0, returnează un mesaj de eroare."""
    if b == 0:
        return "Eroare: Împărțirea la zero nu este permisă."
    return a / b

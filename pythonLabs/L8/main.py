# main.py

# Importarea modulului math_operations
import mathOperation

# Citire de la utilizator a două numere
num1 = float(input("Introduceți primul număr: "))
num2 = float(input("Introduceți al doilea număr: "))

# Apelarea funcțiilor din math_operations
suma = mathOperation.adunare(num1, num2)
diferenta = mathOperation.scadere(num1, num2)
produs = mathOperation.inmultire(num1, num2)
catul = mathOperation.impartire(num1, num2)

# Afișarea rezultatelor
print(f"Adunarea: {num1} + {num2} = {suma}")
print(f"Scăderea: {num1} - {num2} = {diferenta}")
print(f"Înmulțirea: {num1} * {num2} = {produs}")
print(f"Împărțirea: {num1} / {num2} = {catul}")

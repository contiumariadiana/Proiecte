import math

# Citire număr pentru calcularea rădăcinii pătrate și factorialului
num = int(input("Introduceți un număr întreg pentru calcularea rădăcinii pătrate și factorialului: "))

# Calcularea rădăcinii pătrate
radacina_patrata = math.sqrt(num)
print(f"Rădăcina pătrată a {num} este {radacina_patrata}")

# Calcularea factorialului
factorial = math.factorial(num)
print(f"Factorialul lui {num} este {factorial}")

# Citire unghi pentru calcularea sinusului
angle = float(input("Introduceți un unghi în grade pentru calcularea sinusului: "))

# Calcularea sinusului unghiului (convertit în radiani)
sinus = math.sin(math.radians(angle))25
print(f"Sinusul unghiului de {angle} grade este {sinus}")

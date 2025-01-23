# main.py

# Importarea funcțiilor din pachetul geometry
from geometryCircle import aria_cerc, circumferinta_cerc
from geometryRectangle import aria_dreptunghi, perimetru_dreptunghi

# Calcul pentru cerc
raza = float(input("Introduceți raza cercului: "))
print(f"Aria cercului este: {aria_cerc(raza):.2f}")
print(f"Circumferința cercului este: {circumferinta_cerc(raza):.2f}")

# Calcul pentru dreptunghi
latime = float(input("Introduceți lățimea dreptunghiului: "))
lungime = float(input("Introduceți lungimea dreptunghiului: "))
print(f"Aria dreptunghiului este: {aria_dreptunghi(latime, lungime):.2f}")
print(f"Perimetrul dreptunghiului este: {perimetru_dreptunghi(latime, lungime):.2f}")

def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            # Citim linie cu linie din fișierul de intrare
            for line in infile:
                # Verificăm dacă cuvântul cheie este prezent în linie
                if keyword in line:
                    outfile.write(line)  # Scriem linia în fișierul de ieșire
        print(f"Fișierul {output_file} a fost creat cu succes.")
    except FileNotFoundError:
        print("Fișierul de intrare nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

# Exemplu de utilizare:
input_file = "text.txt"  # Numele fișierului de intrare
output_file = "filtered.txt"  # Numele fișierului de ieșire
keyword = "Python"  # Cuvântul cheie de filtrare

filter_lines(input_file, output_file, keyword)

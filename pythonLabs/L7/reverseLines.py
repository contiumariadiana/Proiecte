def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            # Citim linie cu linie din fișierul de intrare
            for line in infile:
                # Inversăm caracterele din linie și scriem în fișierul de ieșire
                reversed_line = line.strip()[::-1]  # strip() elimină spațiile sau newline-uri la capete
                outfile.write(reversed_line + '\n')
        print(f"Fișierul {output_file} a fost creat cu succes.")
    except FileNotFoundError:
        print("Fișierul de intrare nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

# Exemplu de utilizare:
input_file = "input.txt"  # Înlocuiește cu numele fișierului tău de intrare
output_file = "output.txt"  # Numele fișierului de ieșire
reverse_lines(input_file, output_file)

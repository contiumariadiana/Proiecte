def count_words_in_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            # Spargem textul în cuvinte folosind split()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "Fișierul nu a fost găsit."
    except Exception as e:
        return f"A apărut o eroare: {e}"

# Exemplo de utilizare:
file_name = "example.txt"  # Înlocuiește cu numele fișierului tău
result = count_words_in_file(file_name)
print(f"Numărul total de cuvinte: {result}")

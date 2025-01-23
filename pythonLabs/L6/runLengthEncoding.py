def run_length_encoding(text):
    # Inițializăm șirul rezultat și variabilele necesare
    encoded = ""
    count = 1

    # Parcurgem șirul de la al doilea caracter
    for i in range(1, len(text)):
        # Dacă caracterul curent este același cu precedentul, incrementăm contorul
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Dacă este diferit, adăugăm caracterul și numărul său la rezultat
            encoded += text[i - 1] + str(count)
            # Resetăm contorul
            count = 1

    # Adăugăm ultimul caracter și numărul său
    if text:
        encoded += text[-1] + str(count)

    return encoded

# Citim șirul de la utilizator
input_text = input("Introdu șirul de caractere: ")
# Apelăm funcția și afișăm rezultatul
output_text = run_length_encoding(input_text)
print("Rezultatul codificării RLE este:", output_text)

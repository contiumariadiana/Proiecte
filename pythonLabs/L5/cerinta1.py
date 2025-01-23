import string


def word_frequency():
    # Solicităm utilizatorului să introducă textul
    text = input("Introdu un text: ")

    # Eliminăm majusculele și semnele de punctuație
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Împărțim textul în cuvinte
    words = text.split()

    # Calculăm frecvența fiecărui cuvânt
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Returnăm dicționarul cu frecvențe
    return frequency


# Testare
if __name__ == "__main__":
    result = word_frequency()
    print("Frecvența cuvintelor în text:", result)


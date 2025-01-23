def reverse_words(sentence):
    # Împărțim propoziția în cuvinte folosind split(), care elimină automat spațiile suplimentare
    words = sentence.split()
    # Inversăm ordinea cuvintelor
    reversed_words = words[::-1]
    # Reasambăm cuvintele într-o propoziție cu spații între ele
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

# Citim propoziția de la utilizator
input_sentence = input("Introdu propoziția: ")
# Apelăm funcția și afișăm rezultatul
output_sentence = reverse_words(input_sentence)
print("Propoziția inversată este:", output_sentence)

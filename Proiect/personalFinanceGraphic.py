import matplotlib
matplotlib.use('Agg')  # Utilizează un backend non-interactiv pentru a evita erori
import matplotlib.pyplot as plt
import numpy as np

# Categoriile și bugetele lor inițiale
categories = ["Alimentație", "Transport", "Locuință", "Divertisment", "Educație", "Sănătate"]
budgets = [1000, 500, 1500, 300, 400, 600]  # Valori inițiale ale bugetului

def plot_budget(categories, budgets):
    plt.figure(figsize=(10, 6))
    y_pos = np.arange(len(categories))

    # Crearea unui grafic bară
    plt.barh(y_pos, budgets, color='skyblue')
    plt.yticks(y_pos, categories)
    plt.xlabel('Buget alocat (RON)')
    plt.title('Distribuția bugetului personal')

    # Salvarea graficului ca imagine
    plt.tight_layout()
    plt.savefig('budget_distribution.png')
    print("Graficul a fost salvat ca 'budget_distribution.png'.")

def update_budget():
    global budgets
    while True:
        print("\nCategorii disponibile:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category} (Buget curent: {budgets[i]} RON)")

        print("\nAlege o categorie pentru actualizare sau tastează 0 pentru a ieși.")
        choice = input("Numărul categoriei: ")

        if choice == "0":
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(categories):
                new_budget = float(input(f"Introduceți noul buget pentru {categories[index]}: "))
                budgets[index] = new_budget
                print(f"Bugetul pentru {categories[index]} a fost actualizat la {new_budget} RON.")
                plot_budget(categories, budgets)
            else:
                print("Număr invalid. Alegeți o categorie validă.")
        except ValueError:
            print("Vă rugăm să introduceți un număr valid.")

if __name__ == "__main__":
    print("Bun venit la aplicația de gestionare financiară personală!")
    plot_budget(categories, budgets)
    update_budget()
    print("La revedere! Bugetul dumneavoastră a fost salvat.")

import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import json
from PIL import Image, ImageTk


class FinancialManager:
    def __init__(self):
        self.income = 0
        self.budget = {}

    def set_income(self, income):
        self.income = income
        savings = income * 0.20
        self.add_category("Economii", savings)

    def add_category(self, category, amount):
        if category in self.budget:
            self.budget[category] += amount
        else:
            self.budget[category] = amount

    def remove_category(self, category):
        if category in self.budget:
            del self.budget[category]

    def get_remaining_balance(self):
        return self.income - sum(self.budget.values())

    def add_extra_income(self, extra_income):
        self.income += extra_income
        savings = self.income * 0.20
        self.add_category("Economii", savings)

class BudgetApp:
    def __init__(self, root):
        self.manager = FinancialManager()
        self.root = root
        self.root.title("Gestionare Financiară")
        self.category_colors = {}
        self.create_widgets()
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_title("Distribuția Bugetului")
        self.ax.set_xlabel("Categorii")
        self.ax.set_ylabel("Sume alocate (RON)")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=10, padx=10, pady=10)

    def create_widgets(self):
        tk.Label(self.root, text="Introduceți Venitul Total (RON):", font=("Arial", 12)).grid(row=0, column=0,
                                                                                              sticky="w", padx=10,
                                                                                              pady=5)
        self.income_entry = tk.Entry(self.root, font=("Arial", 12))
        self.income_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Setează Venitul", command=self.set_income, bg="blue", fg="white").grid(row=0,
                                                                                                          column=2,
                                                                                                          padx=10,
                                                                                                          pady=5)
        # Adăugare categorie
        tk.Label(self.root, text="Introduceți Numele Categorie:", font=("Arial", 12)).grid(row=1, column=0, sticky="w",
                                                                                           padx=10, pady=5)
        self.category_entry = tk.Entry(self.root, font=("Arial", 12))
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Introduceți suma alocată pentru categorie (RON):", font=("Arial", 12)).grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky="w",
                                                                                                              padx=10,
                                                                                                              pady=5)
        self.amount_entry = tk.Entry(self.root, font=("Arial", 12))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # Etichetă pentru afișarea sumei rămase
        self.remaining_label = tk.Label(self.root, text="", font=("Arial", 16), fg="red")
        self.remaining_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        tk.Button(self.root, text="Adaugă Categorie", command=self.add_category, bg="purple", fg="white").grid(row=2,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=5)

        # Ștergere categorie
        tk.Label(self.root, text="Șterge Categorie:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=10,
                                                                               pady=5)
        self.remove_category_entry = tk.Entry(self.root, font=("Arial", 12))
        self.remove_category_entry.grid(row=5, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Șterge Categorie", command=self.remove_category, bg="red", fg="white").grid(row=5,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=5)

        # Salvare/încărcare buget
        tk.Button(self.root, text="Salvează Bugetul (JSON)", command=self.save_to_json, bg="orange", fg="white").grid(
            row=8, column=1, padx=10, pady=5)



        # Buton pentru încărcarea bugetului
        tk.Button(self.root, text="Încarcă Bugetul (JSON)", command=self.load_from_json, bg="green", fg="white").grid(
            row=8, column=2, padx=10, pady=5)
        # Adăugare venit suplimentar
        tk.Label(self.root, text="Introduceți Venit Suplimentar (RON):", font=("Arial", 12)).grid(row=6, column=0,
                                                                                                  sticky="w", padx=10,
                                                                                                  pady=5)
        self.extra_income_entry = tk.Entry(self.root, font=("Arial", 12))
        self.extra_income_entry.grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Adaugă Venit Suplimentar", command=self.add_extra_income, bg="pink",
                  fg="white").grid(row=6, column=2, padx=10, pady=5)


    def set_income(self):
        try:
            income = float(self.income_entry.get())
            if self.manager.income != 0:
                confirm = messagebox.askyesno("Confirmare", "Graficul va fi resetat. Vrei să continui?")
                if confirm:
                    self.manager = FinancialManager()
                    self.manager.set_income(income)
                    messagebox.showinfo("Succes", f"Venitul a fost setat la {income} RON.")
                    self.update_remaining_label()
                    self.update_plot()  # Apelează update_plot pentru a actualiza graficul
            else:
                self.manager.set_income(income)
                messagebox.showinfo("Succes", f"Venitul a fost setat la {income} RON.")
                self.update_remaining_label()
                self.update_plot()  # Apelează update_plot pentru a actualiza graficul
            self.income_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Eroare", "Te rog să introduci un număr valid.")

    def add_category(self):
        category = self.category_entry.get()
        try:
            amount = float(self.amount_entry.get())
            remaining_balance = self.manager.get_remaining_balance()

            if amount > remaining_balance:
                messagebox.showerror("Eroare", f"Suma rămasă este de {remaining_balance:.2f} RON. "
                                               f"Introduceți o sumă mai mică sau egală.")
            else:
                self.manager.add_category(category, amount)
                messagebox.showinfo("Succes", f"Categoria '{category}' a fost adăugată cu suma de {amount} RON.")
                self.update_remaining_label()
                self.update_plot()  # Apelează update_plot pentru a actualiza graficul
                self.category_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Eroare", "Te rog să introduci o sumă validă.")

    def remove_category(self):
        category_to_remove = self.remove_category_entry.get()
        if category_to_remove in self.manager.budget:
            del self.manager.budget[category_to_remove]
            messagebox.showinfo("Succes", f"Categoria '{category_to_remove}' a fost ștearsă.")
            self.update_remaining_label()
            self.update_plot()
        else:
            messagebox.showerror("Eroare", "Categoria nu a fost găsită.")
        self.remove_category_entry.delete(0, tk.END)

    def add_extra_income(self):
        try:
            extra_income = float(self.extra_income_entry.get())
            if extra_income > 0:
                # Adăugăm venit suplimentar
                self.manager.add_extra_income(extra_income)

                # Calculăm 20% din venitul suplimentar pentru economii
                savings_from_extra_income = extra_income * 0.20
                self.manager.add_category("Economii",
                                          savings_from_extra_income)  # Adăugăm economiile separate de venitul total

                messagebox.showinfo("Succes", f"Venitul suplimentar de {extra_income} RON a fost adăugat. "
                                              f"Din această sumă, {savings_from_extra_income:.2f} RON au fost adăugați la economii.")
                self.update_remaining_label()
                self.update_plot()  # Apelează update_plot pentru a actualiza graficul
                self.extra_income_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Eroare", "Te rog să introduci un venit suplimentar pozitiv.")
        except ValueError:
            messagebox.showerror("Eroare", "Te rog să introduci un număr valid pentru venit suplimentar.")

    def update_remaining_label(self):
        remaining_balance = self.manager.get_remaining_balance()
        self.remaining_label.config(text=f"Suma rămasă: {remaining_balance:.2f} RON")
        if remaining_balance == 0:
            self.show_zero_balance_image()

    def update_plot(self):
        self.ax.clear()
        self.ax.set_title("Distribuția Bugetului", fontsize=16, pad=20)
        categories = list(self.manager.budget.keys())
        amounts = list(self.manager.budget.values())
        remaining_balance = self.manager.get_remaining_balance()
        categories.append("Suma Rămasă")
        amounts.append(max(remaining_balance, 0))
        for category in categories:
            if category not in self.category_colors:
                self.category_colors[category] = f"#{random.randint(0, 0xFFFFFF):06x}"
        colors = [self.category_colors[category] for category in categories]
        bars = self.ax.bar(categories, amounts, color=colors)
        for bar, amount in zip(bars, amounts):
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05 * max(amounts),
                         f"{amount:.2f} RON", ha="center", va="bottom", fontsize=8)
        self.ax.tick_params(axis="x", labelsize=10)
        self.ax.set_xticklabels(categories, rotation=30, ha="right")
        self.fig.tight_layout()
        self.canvas.draw()

    def show_zero_balance_image(self):
        image_window = tk.Toplevel(self.root)
        image_window.title("Buget utilizat complet")

        # Calea către fișierul imagine
        file_path = "venit_terminat.png"
        print("Calea fișierului:", file_path)  # Debugging: verifică calea fișierului

        try:
            # Deschide imaginea
            image = Image.open(file_path)
            image = image.resize((500, 500), Image.Resampling.LANCZOS)  # Mărim imaginea
            img = ImageTk.PhotoImage(image)

            # Creează un label pentru a afișa imaginea
            label = tk.Label(image_window, image=img)
            label.image = img
            label.pack(pady=20)  # Adăugăm padding pentru a alinia la centru

            # Text suplimentar
            tk.Label(image_window, text="Ai folosit tot venitul disponibil!", font=("Arial", 14), fg="red").pack(
                pady=10)

            # Buton de închidere
            tk.Button(image_window, text="Închide", command=image_window.destroy, bg="red", fg="white").pack(pady=10)

            # Centrarea ferestrei pe ecran
            window_width = 500  # Lățimea ferestrei
            window_height = 500  # Înălțimea ferestrei

            screen_width = self.root.winfo_screenwidth()  # Lățimea ecranului
            screen_height = self.root.winfo_screenheight()  # Înălțimea ecranului

            # Calculăm poziția pentru a centra fereastra
            position_top = int((screen_height / 2) - (window_height / 2))
            position_right = int((screen_width / 2) - (window_width / 2))

            # Setăm geometria ferestrei
            image_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        except Exception as e:
            messagebox.showerror("Eroare", f"Nu s-a putut încărca imaginea: {str(e)}")

    def save_to_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                data = {
                    "income": self.manager.income,
                    "budget": self.manager.budget
                }
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=4)
                self.json_file_path = file_path  # Salvăm calea fișierului
                messagebox.showinfo("Succes", "Bugetul a fost salvat cu succes!")
            except Exception as e:
                messagebox.showerror("Eroare", f"Nu s-a putut salva fișierul: {str(e)}")

    def load_from_json(self):
        file_path = filedialog.askopenfilename(defaultextension=".json",
                                               filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                self.manager.set_income(data['income'])
                self.manager.budget = data['budget']
                messagebox.showinfo("Succes", "Bugetul a fost încărcat cu succes!")
                self.update_remaining_label()
                self.update_plot()  # Apelează update_plot pentru a actualiza graficul
            except Exception as e:
                messagebox.showerror("Eroare", f"Nu s-a putut încărca fișierul: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
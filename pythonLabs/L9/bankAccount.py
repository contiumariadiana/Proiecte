class BankAccount:
    def __init__(self):
        # Atribut privat pentru soldul contului
        self._balance = 0.0

    def deposit(self, amount):
        """
        Adaugă bani în cont.
        :param amount: Suma de adăugat (trebuie să fie pozitivă).
        """
        if amount > 0:
            self._balance += amount
            print(f"S-au depus {amount} unități. Sold actual: {self._balance}")
        else:
            print("Suma trebuie să fie pozitivă.")

    def withdraw(self, amount):
        """
        Retrage bani din cont, dacă există suficient sold.
        :param amount: Suma de retras (trebuie să fie pozitivă și <= soldului disponibil).
        """
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"S-au retras {amount} unități. Sold actual: {self._balance}")
            else:
                print("Fonduri insuficiente.")
        else:
            print("Suma trebuie să fie pozitivă.")

    def get_balance(self):
        """
        Returnează soldul actual al contului.
        """
        return self._balance

# Exemplu de utilizare:
cont = BankAccount()
cont.deposit(100)
cont.withdraw(50)
print("Soldul final este:", cont.get_balance())

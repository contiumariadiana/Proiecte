class Employee:
    def __init__(self, name, salary):
        """
        Inițializează un angajat cu un nume și un salariu.
        :param name: Numele angajatului.
        :param salary: Salariul angajatului.
        """
        self.name = name
        self.salary = salary

    def get_details(self):
        """
        Returnează detalii despre angajat.
        """
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        """
        Inițializează un manager cu nume, salariu și departament.
        :param name: Numele managerului.
        :param salary: Salariul managerului.
        :param department: Departamentul managerului.
        """
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        """
        Returnează detalii despre manager, incluzând departamentul.
        """
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Exemplu de utilizare:
emp = Employee("John", 3000)
mgr = Manager("Alice", 5000, "IT")

print(emp.get_details())  # "Employee: John, Salary: 3000"
print(mgr.get_details())  # "Manager: Alice, Salary: 5000, Department: IT"

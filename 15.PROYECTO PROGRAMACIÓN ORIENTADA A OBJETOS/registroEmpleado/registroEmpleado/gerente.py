from empleado import Employee
from valida_input import validar

class EmployeesManager:
    def __init__(self):
        self.employess = []

    def add_employee(self):
        print('\nIngrese los datos del empleado:')
        name = input("Ingrese el nombre: ")
        age = input("Ingrese la edad: ")
        salary = input("Ingrese el salario: ")

        self.employess.append(Employee(name, age, salary))



    def list_employees(self):
        if len(self.employess) == 0:
            print("\nNo hay empleados en este momento!")
            return

        print("\n**Lista de Empleados**")
        for emp in self.employess:
            print(emp)


    def delete_employees_with_age(self, age_from, age_to):
         for idx in range(len(self.employess)-1,-1,-1):
             emp = self.employess[idx]
             if age_from <= emp.age <= age_to:
                print("\tEliminado", emp.name)
                self.employess.pop(idx)

    def find_employee_by_name(self, name):
        for emp in self.employess:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self,name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print("Error: Ningun empleado con ese nombre")
        else:
            emp.salary = salary
        










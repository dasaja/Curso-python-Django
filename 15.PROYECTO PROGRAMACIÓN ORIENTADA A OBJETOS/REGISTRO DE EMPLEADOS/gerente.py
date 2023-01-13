from empleado import Employee


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nIngrese los datos del empleado: ')
        name = input("Ingrese el nombre: ")
        age = input("Ingrese la edad: ")
        salary = input("Ingrese el salario: ")
        self.employees.append(Employee(name, age, salary))


    def list_employee(self):
        if len(self.employees) == 0:
            print("\n No hay empleados en este momento¡")
            return

        print("\nLista de Empleados")
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print("\tEliminado", emp.name)


    def find_employee_by_name(self, name):
         for emp in self.employees:
             if emp.name == name:
                 return emp
         return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print("Error: Ningun empleado con ese nombre")
        else:
            emp.salary == salary






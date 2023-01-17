import valida_input
from gerente import EmployeesManager
from valida_input import validar

class FrontendManager:
    def __init__(self):
        self.empledo = EmployeesManager()

    def print_menu(self):
        print('\n Opciones del programa:')
        messages = [
            '1) Agregar nuevo Empleado',
            '2) Listar Empleados',
            '3) Eliminar por rango de edad',
            '4) Actualizar salario por nombre',
            '5) Salir'
        ]
        print('\n'.join(messages))
        msg = "Ingrese la opcion: "
        return validar.input_valid_int(msg,"","")


    def run(self):
        while True:

            choice = self.print_menu()

            if choice == 1:
                self.empledo.add_employee()
            elif choice == 2:
                self.empledo.list_employees()
            elif choice == 3:
                 age_from = input('Ingrese la edad desde: ')
                 age_to = input('Ingrese la edad hasta: ')
                 self.empledo.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                 name = input("Ingrese el nombre: ")
                 salary = input("Ingrese nuevo salario:")
                 self.empledo.update_salary_by_name(name, salary)
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()



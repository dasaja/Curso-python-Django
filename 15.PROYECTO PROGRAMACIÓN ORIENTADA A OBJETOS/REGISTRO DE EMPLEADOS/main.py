from gerente import EmployeesManager
from valido_input import validar

class FrontendManager:
    def __init__(self):
        self.empleado = EmployeesManager()

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

        msg = "Ingrese la opción: "
        return validar.input_valid_int(msg, "", "")

    def run(self):
        while True:

            choice = self.print_menu()

            if choice == 1:
                self.empleado.add_employee()
            elif choice == 2:

                self.empleado.list_employee()
            elif choice == 3:
                age_from = input('Ingrese la edad desde: ')
                age_to = input('Ingrese la edad hasta: ')
                self.empleado.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input("Ingrese el nombre: ")
                salary = input("Ingrese nuevo salario:")
                self.empleado.update_salary_by_name(name, salary)
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()

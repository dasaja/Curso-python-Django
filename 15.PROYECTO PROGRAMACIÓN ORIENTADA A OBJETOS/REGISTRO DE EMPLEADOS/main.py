from gerente import EmployeesManager


class FrontendManager:
    def __init__(self):
        self.employees_manger = EmployeesManager()

    def print_menu(self):
        print('\n Opciones del programa:')
        messages = [
            '1) Agregar nuevo Empleado',
            '2) Listar Empleados',
            '3) Eliminar por rango de edad',
            '4) Actualizar salario por nombre',
            '5) Salir',
        ]

        print('\n'.join(messages))

        msg = f'Ingrese la opcion (desde 1 - {len(messages)}):'
        return input("")

    def run(self):
        while True:

            choice = self.print_menu()

            if choice == 1:
                self.employees_manger.add_employee()
            elif choice == 2:

                self.employees_manger.list_employees()
            elif choice == 3:
                age_from = input('Ingrese la edad desde: ')
                age_to = input('Ingrese la edad hasta: ')
                self.employees_manger.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input("Ingrese el nombre: ")
                salary = input("Ingrese nuevo salario:")
            elif choice == 5:
                choice = False
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()

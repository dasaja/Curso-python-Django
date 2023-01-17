class Employee:

    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary

    def __str__(self):
        return f'Empleado: {self.name} con edad {self.age} y salario {self.salary}'

    def __repr__(self):
        return f'Empleado(name="{self.name}", age="{self.age}", salary="{self.salary}")'


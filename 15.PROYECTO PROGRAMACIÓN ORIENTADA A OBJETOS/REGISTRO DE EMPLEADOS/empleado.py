class Employee:
    def __int__(self, name, age, salary):
        #Declaración de variables en una sola línea
        self.name, self.age, self.salary = name, age, salary

    def __str__(self):
        return f"Empleado {self.name} con edad {self.age} y salario {self.salary}"

    def __repr__(self):
        return f'Empleado (name="{self.name}", edad="{self.age}", salario ="{self.salary}"))'
    
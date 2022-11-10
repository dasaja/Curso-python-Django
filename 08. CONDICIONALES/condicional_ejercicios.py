num1 = input("Insertar horas de trabajo")
num2 = input("Insertar costo por horas")
resultado = (int(num1) * float(num2))

if resultado > 10:
   print(f"{resultado} del trabajo es gratificante")
else:
    print("Conseguir nuevo trabajo")

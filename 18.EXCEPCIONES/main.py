c = 0
suma = 0
while c < 3:
    try:
        n = int(input("Ingrese un número {c + 1}:   "))
        suma += n
        c += 1
    except:
        print("Erro : Ingreso solo número enteros")
    else:
        print("Todo a funcionado correctamente")
    finally:
        print("fin de la ejecución")
print("La suma total es:", suma)



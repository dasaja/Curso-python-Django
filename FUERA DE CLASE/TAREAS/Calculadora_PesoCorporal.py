def IMC(estatura, peso):
    return peso / estatura ** 2


estatura = float(input("Escribe tu estatura en metros: "))
peso = float(input("Escribe su peso en Kg: "))

i = IMC(estatura, peso)

print("Su IMC es: {} ".format(i))

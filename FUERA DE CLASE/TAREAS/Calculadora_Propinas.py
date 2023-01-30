def Calcular_propina (porcentaja_propina, monto_cuenta, cantidad_personas):
    monto_cuenta = input(float("Coloca el monto de la cuenta: "))
    cantidad_personas = input(float("Coloca la cantidad de personas: "))
    porcentaja_propina = input(int("Elige una de las siguientes opciones de porcentaja a)7%,  b)12%, c)10%,d)15%: "))

    if porcentaja_propina == 7:
        resultado = monto_cuenta*7/100
        print(resultado/cantidad_personas)

    elif porcentaja_propina == 10:
        resultado = monto_cuenta*10/ 100
        print(resultado / cantidad_personas)

    elif porcentaja_propina == 12:
        resultado = monto_cuenta*12/ 100
        print(resultado / cantidad_personas)

    elif porcentaja_propina == 15
        resultado = monto_cuenta*15/ 100
        print(resultado / cantidad_personas)

    else:
        print("El valor colocado es incorrecto vuelva a intentarlo")









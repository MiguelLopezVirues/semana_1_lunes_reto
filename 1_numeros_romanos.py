def numero_romano():
    numero = int(input("Ingrese un numero entre 1 y 3000: "))
    if numero < 1 or numero > 3000:
        print("El numero ingresado no es correcto ")
    else:
        numero_romano = ""
        # Convertir a millares
        if numero >= 1000:
            m = numero // 1000
            numero_romano += "M" * m
            numero %= 1000
        # Convertir a centenas
        if numero >= 100:
            c = numero // 100
            if c == 9:
                numero_romano += "CM"
            elif c >= 5:
                numero_romano += "D" + "C" * (c - 5)
            elif c == 4:
                numero_romano += "CD"
            else:
                numero_romano += "C" * c
            numero %= 100
        # Convertir a decenas
        if numero >= 10:
            d = numero // 10
            if d == 9:
                numero_romano += "XC"
            elif d >= 5:
                numero_romano += "L" + "X" * (d - 5)
            elif d == 4:
                numero_romano += "XL"
            else:
                numero_romano += "X" * d
            numero %= 10
        # Convertir a unidades
        if numero > 0:
            if numero == 9:
                numero_romano += "IX"
            elif numero >= 5:
                numero_romano += "V" + "I" * (numero - 5)
            elif numero == 4:
                numero_romano += "IV"
            else:
                numero_romano += "I" * numero

        print("El numero romano es:", numero_romano)
        return numero_romano
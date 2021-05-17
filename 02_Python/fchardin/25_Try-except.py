try:
    #avalue = 10 / 0
    number = int(input("Ingrese un número: "))
    print(number)
# devuelve el error de división por cero por defecto en py
except ZeroDivisionError as err:
    print(err)
except ValueError: 
    print("Entrada incorrecta. Ingrese un número.")
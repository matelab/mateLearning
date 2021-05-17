n1 = float(input("Ingrese número 1: "))
op = input("Tipo de cálculo: ")
n2 = float(input("Ingrese número 2: "))

if op  == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    print(n1 / n2)
elif op == "*":
    print(n1 * n2)
else:
    print("Operador inválido. Ingrese un operador: + - / *")

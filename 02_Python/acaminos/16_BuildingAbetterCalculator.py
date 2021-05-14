num1 = float(input("Enter first number:\t"))
op = input("ENter operator:\t")
num2 = float(input("Enter second number:\t"))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*' or op == 'x' or op == 'X':
    print(num1*num2)
else:
    print("invalid operator")
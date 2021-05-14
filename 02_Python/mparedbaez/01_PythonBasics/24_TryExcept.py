
try:
    value = 10/0
except ZeroDivisionError:
    print('Divided by zero')

try:
    number = int(input("Enter a Number: "))
    print(number)
except:
    print("Invalid Input")


try:
    number = int(input("Enter a Number: "))
    value2 = 50/0
    print(number)
except ZeroDivisionError:
    print('Divided by zero')
except ValueError:
    print("Invalid Input")


try:
    value = 10/0
except ZeroDivisionError as arr:
    print(arr)
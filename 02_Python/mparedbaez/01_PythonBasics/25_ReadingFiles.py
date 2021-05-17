#r w a  r+w
# employeeFile = open("/home/baubyte/Devs/mateLab/mateLearning/02_Python/mparedbaez/01_PythonBasics/employees.txt", "r")

# for employee in employeeFile.readlines():
#     print(employee)

# print(employeeFile.read())

# employeeFile.close()


employeeFile = open("/home/baubyte/Devs/mateLab/mateLearning/02_Python/mparedbaez/01_PythonBasics/employees.txt", "a")

#employeeFile.write("BAUBYTE")
employeeFile.write("\nBAUBYTE - BAUBYTE")


employeeFile.close()
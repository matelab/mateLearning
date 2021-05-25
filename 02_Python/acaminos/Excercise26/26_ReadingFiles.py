employee_file = open("./02_Python/acaminos/Excercise26/26_ReadingFiles.txt", "r")

#r (read) only read - No se modifica
#w (write) se puede escribir, modificar, editar informacion, crear. Borra contenido anterior y sobreescribe
#a (append) append information into the end of the file, you can't change any information but you can add new information

for employee in employee_file.readlines():
    print(employee)


employee_file.close()
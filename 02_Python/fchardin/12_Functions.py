#definimos la función. Es importante indentar bien en Python
def saluda():
    print("2 Saludos!")
#para que se ejecute la función tenemos que llamarla
print("Orden de ejecución:")
print("1 principio")
saluda()  
print("3 final")

def saluda_con_parametros(nombre, edad):
    print("Hola " + nombre + ". Tenés " + str(edad) + " años.")
saluda_con_parametros("Pinini", 4)

#es buena práctica separar las funciones por usos particulares y desarmar
#los problemas en partes pequeñas
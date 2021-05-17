# opern abre un archivo en la ruta dada
# el segundo parámetro es el modo de apertura
# r = leer
# w = escribir
# a = append, agregar información al final, no se puede medificar sino agregar
# r+ = leer y escribir

archivo_ejemplo = open("/media/fran/01D68EB31CA9AB607/MateLab/mateLearning/02_Python/fchardin/ejemplo.txt", "r")

# Es posible leer el archivo? 
print(archivo_ejemplo.readable())

# lee el archivo
#print(archivo_ejemplo.read())

# lee una linea del archivo
#print(archivo_ejemplo.readline())
# y otra
#print(archivo_ejemplo.readline())

# Arma un array con la data y lo recorre
for line in archivo_ejemplo.readlines():
    print(line)

# Siempre hay que cerrar el archivo una vez que terminamos de usarlo
archivo_ejemplo.close()

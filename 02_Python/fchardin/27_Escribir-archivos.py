# Escribiendo en archivos
#archivo_ejemplo = open("/media/fran/01D68EB31CA9AB607/MateLab/mateLearning/02_Python/fchardin/ejemplo.txt", "a")
#Si usamos w en vez de a sobreescribe todo el archivo
#También se puede usar w para crear un archivo nuevo con el nombre y ubicación que elijamos
#archivo_ejemplo = open("/media/fran/01D68EB31CA9AB607/MateLab/mateLearning/02_Python/fchardin/ejemplo.txt", "a")
archivo_ejemplo = open("/media/fran/01D68EB31CA9AB607/MateLab/mateLearning/02_Python/fchardin/ejemplo.txt", "r")
#Ya usé la linea siguiente
#archivo_ejemplo.write("\nOtra linea nueva editada desde python.")
print(archivo_ejemplo.read())
archivo_ejemplo.close()

html_ejemplo = open("/media/fran/01D68EB31CA9AB607/MateLab/mateLearning/02_Python/fchardin/index.html", "w")
html_ejemplo.write("<p>Archivo Html creado desde Python</p>")
html_ejemplo.close()
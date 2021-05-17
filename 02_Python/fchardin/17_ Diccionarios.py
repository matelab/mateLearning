# Funcionan parecido a un diccionario común. Hay palabras y definiciones. 
# Son combinaciones de llave y valor

# Vamos a programar un sistema que transforme nombres de meses resumidos de 3 letras en nombres de meses completos

transformaMeses = {
    "Ene": "Enero",
    "Feb": "Febrero",
    "Mar": "Marzo",
    "Abr": "Abril",
    "May": "Mayo",
    "Jun": "Junio",
    "Jul": "Julio",
    "Ago": "Agosto",
    "Sep": "Septiembre",
    "Oct": "Octubre",
    "Nov": "Noviembre",
    "Dic": "Diciembre"
}

print(transformaMeses["Nov"])
# Si pedimos algo que no está en el diccionario devuelve none. 
print(transformaMeses["Nwq"])
# Podemos pasar un segundo parámetro para modificar el mensaje de error por defecto
print(transformaMeses["Nwq", "No es un valor de mes válido"])

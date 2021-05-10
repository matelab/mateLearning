#Lo usamos cuando necesitamos que la función retorne algún valor
#EJ: Hacemos una funcion que eleve al cubo un número y retorne el resultado
#se ejecuta pero no devuelve nada
def cubo(num):
    num * num * num

print(cubo(3))

#se ejecuta y devuelve el resultado
def cubo_con_return(num):
    return num*num*num

print("\n" + str(cubo_con_return(4)))

resultado = cubo_con_return(8)
print(resultado)
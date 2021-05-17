# 2 elevado a la potencia 3
print(2**3)

# con un for loop podemos hacer lo mismo nosotrxs mismxs
def elevar_a_potencia(base, potencia):
    resultado = 1
    for i in range(potencia):
        resultado = resultado * base
    return resultado

print(elevar_a_potencia(32, 2))
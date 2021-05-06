numeros = [2, 7, 3, 777, 923, 1982]
numeros_importantes = [2, 7, 3, 777, 923, 1982, 3, 3, 3, 3]
amigos = ["Ross", "Monica", "Rachel", "Chandler", "Joey", "Phoebe"]

print(numeros_importantes)
numeros_importantes.extend(amigos)
print(numeros_importantes)
print(amigos)
amigos.insert(1, "Richard")
print(amigos)
print(numeros)
numeros.remove(2)
print(numeros)
#saca el último item de la lista
numeros.pop()
print(numeros)
#busca un item en la lista
print(numeros.index(3))
#si no lo encuentra retorna un error ValueError: 8888 is not in list
#print(numeros.index(8888))
#cuenta cuantas veces aparece un valor en la lista
print(numeros_importantes.count(3))
#ordena la lista
#numeros_importantes.sort()
print(numeros_importantes)
amigos2 = amigos.copy()
print(amigos2)
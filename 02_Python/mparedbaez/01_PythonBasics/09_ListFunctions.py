

luckyNumbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim","Oscar","Toby"]

#agrega al final la otra lista
friends.extend(luckyNumbers)
#agrega al final
friends.append("Jim")
#recibe dos parametros
friends.insert(1,"Jim")
#saca el ultimo elemento
friends.pop()
print(friends)

#devuelve el indice la primer coincidencia
print(friends.index("Jim"))
#devuelve cuantas veces aparece la primer coincidencia
print(friends.index("Jim"))
#ordena de > a <
luckyNumbers.sort()
print(luckyNumbers)
#ordena de < a >
luckyNumbers.reverse()
print(luckyNumbers)
#copia
friends2 = friends.copy()
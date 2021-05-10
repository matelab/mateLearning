#Funcion Extend - "Fusiona" la lista con otra

lucky_numbers= [4,8,15,16,23,42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim']

friends.extend(lucky_numbers)

print(friends, '\n')

#Funcion Append - Agrega un dato mas a la lista

lucky_number= [1,2,40,5,23,100]
friend = ['Jorge', 'Carla', 'Joe', 'Omar', 'Tom']

friend.append('Ariel')

print(friend, '\n')

#Funcion Insert - Inserta un nombre en la posicion que uno establezca

numeros = [0,13,23,33,43,53]

masNombres = ['Noe', 'German', 'Sol', 'Pepe']

masNombres.insert(1, 'Santiago')

print(masNombres, '\n')

#Funcion Remove - Elimina un dato

masNombres.remove('Sol')

print(masNombres, '\n')

#Funcion Clear - Limpia todo

lucky_numbers.clear()

print(lucky_numbers, '\n')

#Funcion Pop

friend.pop()

print(friend, '\n')

#Funcion Index - Ubica la posicion de lo que se busque

print(friend.index('Carla'),'\n')

#Funcion Count - Cuenta la cantidad de veces que se repite algo

masNombres2 = ['Noe', 'German', 'Noe', 'Sol', 'Pepe', 'Noe']

print(masNombres2.count('Noe'),'\n')

#Funcion Sort

print(lucky_number.sort(), '\n')
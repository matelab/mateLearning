number_grid = [
    [1,2,3],            #Lista 0
    [4,5,6],            #Lista 1
    [7,8,9],            #Lista 2
    [0]                 #Lista 3
]

print(number_grid[1][0])    #EL primer corchete va la lista, y en el segundo corchete la posicion dentro de esa lista

print('\n\n')
for row in number_grid:
    print(row)              #Imprime todas las listas

print('\n\n')

for row in number_grid:     #Imprime todo lo que se encuentra en number_grid
    for col in row:
        print(col)
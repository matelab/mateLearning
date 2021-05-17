num_grid = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print(num_grid[0][0])
print(num_grid[0][1])
print(num_grid[1][2])
print(num_grid[1][1])

# como pasar por todos los items de las listas dentro de la lista (lista de 2 dimensiones)

# así imprime las tres filas
for row in num_grid:
    print(row)

# y así todas los campos por separado
for row in num_grid:
    for col in row:
        print(col)
        
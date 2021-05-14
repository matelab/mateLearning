numberGrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numberGrid[0][0])

for row in numberGrid:
    print(row)

for row in numberGrid:
    for col in row:
        print(col, end=', ')
    print()

for row in range(len(numberGrid)):
    for col in range(len(numberGrid[row])):
        print(numberGrid[row][col],end=', ')
    print()
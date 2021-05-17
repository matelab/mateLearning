# Bucles For

for letter in "Matelab Cooperativa":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

# range no considera el último número
for index in range(10):
    print(index)
# con dos parametros incluye el primero y uno menos que el segundo. 
for index in range(2, 11):
    print(index)
#lo mismo que con for pero con range también
for i in range(len(friends)): 
    print(friends[i])

for i in range(6):
    if i == 0: 
        print("primera iteración")
    else: 
        print("no es la primera iteración.")

print("así se hace fizzbuzz supongo, con un for")
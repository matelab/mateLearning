character_name = "George"
character_age = "70"
character_cars = 2
#con f (formato)
print(f"There once was man named {character_name},")
print(f"he was {character_age} years old. ")

#cambiando el valor de una variable
character_name = "Mike"

#sin f (formato)
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")
#es necesario formatear los números a str para concatenar
print("He had " + str(character_cars) + " cars.")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if  letter.lower() in "aeiou":         #Se fija que haya vocales en la frase
            if letter.isupper():
                translation = translation + "g"     #Reemplaza las vocales por la letra G
            else:
                translation = translation + letter
    return translation

print(translate(input("enter a phrase:\t")))
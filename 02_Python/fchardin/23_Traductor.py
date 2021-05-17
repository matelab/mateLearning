"""
Lenguaje mate
todas las vocales se transforman en mate

ej  mate -> mmatma
    perro -> pmarrma
"""

def traducir(frase):
    traduccion = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                traduccion = traduccion + "Mate"
            traduccion = traduccion + "mate"
        else:
            traduccion = traduccion + letra
    return traduccion

print(traducir(input("Ingrese una frase para traducirla a lenguaje mate \n")))

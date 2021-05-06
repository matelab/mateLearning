phrase = "Matelab cooperativa\n:)"
print(phrase + "\n:)")
print(phrase.upper())
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
#index("x") busca el/los caracter/es x en un string y retorna en que indice está el primero o donde comienza
print(phrase.index("c"))
print(phrase.index("M"))
#si no lo encuentra da un error "ValueError: substring not found"
#print(phrase.index("m"))
#recibe 2 parámetros, que quiero reemplazar y por que otra cosa
print(phrase.replace("cooperativa", "recooperativa"))
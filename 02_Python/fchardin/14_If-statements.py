""" Ejemplos de simples a más complejos
Me despierto
Si tengo hambre
    Como un desayuno

Me voy de mi casa
Si llueve
    Llevo paraguas 
Sino 
    Llevo anteojos de sol

Estoy en un restaurante
Si quiero ensalada
    Pido ensalada
Sino, si quiero pasta
    Pido fideos con pesto
Sino 
    Pido un café
"""
#Creo un booleano
is_panda = True
is_tall = False

if is_panda == True:
    print("Sos un panda")
else:
    print("No sos un panda")

if is_panda or is_tall:
    print("Sos altx y/o un panda")
else: 
    print("No sos un panda ni sos altx")

if is_panda and is_tall:
    print("Sos altx panda")
elif is_panda and not(is_tall):
    print("Sos un panda petiso")
elif not(is_panda) and is_tall:
    print("No sos un panda pero sos alto")
else: 
    print("No sos un panda ni sos alto")

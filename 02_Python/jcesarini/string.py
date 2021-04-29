phrase = "Giraffe\"Academy"
#you must use \ to show "
print(phrase.upper().isupper()) # convert string to upper and verify it

print(len(phrase))
# len -> is used to give you how much char have the phrase
print(phrase[0]) # 0 in the index, so you can access to de value of this position
print(phrase.index("ra")) # return the position where is the fisrt char between brackets
print(phrase.replace("Giraffe","Elephant"))

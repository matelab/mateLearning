is_male = True
is_tall = False
if is_male:
    print("YOU ARE A MALE")

if is_male:
    print("YOU ARE A MALE")
else:
    print("YOU ARE NOT A MALE")

### OR ###

if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("You neither male nor tall")

### AND ###
  
if is_male and is_tall:
    print("you are a tall male")
else:
    print("You are either not male or not tall or both")

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print ("You are a short male")
elif not(is_male) and is_tall:
    print ("You are not a male, but you are tall")
else:
    print("You are either not male or not tall or both")
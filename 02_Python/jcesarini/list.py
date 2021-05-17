friends = ["Kevin","Karen","Jim","Cuco"]
lucky_numbers = [45,4,8,15,16,23,42]
friends.extend(lucky_numbers) # show the union of both lists
friends.append("Caco") # add element in the last place of the list
friends.insert(0,"Ahora soy el primero")
friends.pop(2)
print(friends.index("Cuco"))
print(friends) # show the list

print(friends[0]) # show the element in the first position

print(friends[1:]) # show the elements from the element who is in position 1 to last

print(friends[2:4]) # show the the elements from position 3 at 4
lucky_numbers.sort()
print("lista ordenada:" , lucky_numbers)
# This is a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Micheal Scott"

# How to access element in a list?
print(friends[0])

# Many elements
print(friends[1:3])

# Extend
friends.extend(lucky_numbers)
print(friends)

# Append
friends.append("Creed")
print(friends)

# Insert
friends.insert(1, "Kelly")
print(friends)

# Figure out the index of an element in the list
print(friends.index("Jim"))

# Count values in a list
print(friends.count("Jim"))

# Sort the list
print(friends.sort())

# Remove
friends.remove("Jim")
print(friends)

# Pop
friends.pop()
print(friends)

# Clear list
friends.clear()
print(friends)
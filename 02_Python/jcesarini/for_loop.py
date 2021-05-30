friends = ["Jim", "Karen", "Kevin"]

for letter in "Giraffe Academy":
    print(letter)

print("-----")

for friend in friends:
    print(friend)

print("-----")

for index in range(10): # show numbers between 0 to 9
    print(index)

print("-----")

for index in range(3, 10):
    print(index)

print("-----")

for index in range(len(friends)):
    print(friends[index])

print("-----")

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")
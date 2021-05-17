isMale = False
isTall = True

# if isMale:
#     print('You are a Male')
# else:
#     print('You are not a Male')


# if isMale or isTall:
#     print('You are a Male or tall or both')
# else:
#     print('You neither Male nor tall')


# if isMale and isTall:
#     print('You are a tall Male')
# else:
#     print('You are eithger not male or not tall or both')


if isMale and isTall:
    print('You are a tall Male')
elif isMale and not(isTall):
    print('You are a short male')
elif not(isMale) and isTall:
    print('You are not male but are tall')
else:
    print('You are not a male and not tall')
import random

feetInMile = 5200
metersInKilometer = 100
beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']

def getFileExt(fileName):
    return fileName[fileName.index(".")+1:]

def rollDice(num):
    return random.randint(1,num)
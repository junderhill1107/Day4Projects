import random

"""
myRandInt = random.randint(0,1)


if myRandInt == 1:
    print("Heads")
else:
    print ("Tails")
"""

namesIn = input("Give me everybody's names, separated by a comma: ")
#print(namesIn)

splitNames = namesIn.split(", ")
# print(splitNames)

# print(splitNames.__len__())
randNameIndex = random.randint(0, len(splitNames) - 1)
print(splitNames[randNameIndex] + " will be paying for the meal.")

randChoice = random.choice(splitNames)
print("Random.choice :: " + randChoice + " will be paying for the meal.")
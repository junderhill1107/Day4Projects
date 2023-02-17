import random
myRandInt = random.randint(1,10)
myRandFloat = random.random()

names = ["Jon", "Jeremiah", "Michael", "Trei"]
fruit = ["kiwi", "apples", "bananas"]
list1 = [names, fruit]
#print(list1)
#print(list1[1][2])

r1 = [" ", " ", " "]
r2 = [" ", " ", " "]
r3 = [" ", " ", " "]
map =[r1, r2, r3]
print("*** T R E A S U R E   M A P ***")
print("*******************************")
print(f"{r1}\n{r2}\n{r3}")
print("*******************************")

validOptions = [11, 12, 13, 21, 22, 23, 31, 32, 33]

print("Where do you want to put the treasure?")
print("Valid options: 11, 12, 13, 21, 22, 23, 31, 32, 33")
position = int(input("Treasure position: "))

while position not in validOptions:
    print("You entered an invalid option.")
    position = int(input("Treasure position: "))
else:
    strPosition = str(position)
    p1 = int(strPosition[0]) - 1
    p2 = int(strPosition[1]) - 1
    map[p1][p2] = "x"
    print("\n'X' marks the spot.")
    print("*******************************")
    print(f"{r1}\n{r2}\n{r3}")
    print("*******************************")

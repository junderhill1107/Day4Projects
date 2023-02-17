# Day4Projects

def whoPays():
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

    randNameIndex = random.randint(0, len(splitNames) - 1)
    print(splitNames[randNameIndex] + " will be paying for the meal.")

    randChoice = random.choice(splitNames)
    print("Random.choice :: " + randChoice + " will be paying for the meal.")


def treasureMap():
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
        map[p1][p2] = "X"
        print("\n'X' marks the spot.")
        print("*******************************")
        print(f"{r1}\n{r2}\n{r3}")
        print("*******************************")

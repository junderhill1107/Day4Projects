def printMenu():
    print("\n*** M E N U ***")
    print("********************************")
    print("1. Who's paying for the meal?")
    print("2. Treasure Map")
    print("3. Rock, Paper, Sissors")
    print("0. Exit")
    print("********************************\n")



while True:
    printMenu()
    menuChoice = int(input("Enter the MENU choice number:"))

    import Day4Projects
    if menuChoice == 1:
        Day4Projects.whoPays()
        break
    elif menuChoice == 2:
        Day4Projects.treasureMap()
        break
    elif menuChoice == 3:
        print(f"Menu Choice: {menuChoice}")
    elif 0:
        break




def printMenu():
    print("\n*** M E N U ***")
    print("********************************")
    print("1. Who's paying for the meal?")
    print("2. Treasure Map")
    print("3. Rock, Paper, Sissors")
    print("0. Exit")
    print("********************************\n")

printMenu()
menuChoice = input("Enter the MENU choice number:")

while not menuChoice == "0":

    import Day4Projects
    if menuChoice == "1":
        Day4Projects.whoPays()
        break
        
    elif menuChoice == "2":
        Day4Projects.treasureMap()
        break
     
    elif menuChoice == "3":
        print(f"Menu Choice: {menuChoice}")
        break
    
    else:
        print("You entered an invalid menu choice...\n")

    printMenu()
    menuChoice = input("Enter the MENU choice number:")
   


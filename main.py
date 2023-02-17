import Day4Projects

print("*** M E N U ***")
print("1. Who's paying for the meal?")
print("2. Treasure Map")
print("3. Rock, Paper, Sissors")
print("********************************\n")

validInput = [1, 2, 3]
menuChoice = int(input("Enter the MENU choice number:"))

while menuChoice not in validInput:
    print("You entered an invalid entry.")
    menuChoice = int(input("Enter the MENU choice number:"))

if menuChoice == 1:
    Day4Projects.whoPays()
elif menuChoice == 2:
    Day4Projects.treasureMap()
elif menuChoice == 3:
    print(f"{menuChoice}")
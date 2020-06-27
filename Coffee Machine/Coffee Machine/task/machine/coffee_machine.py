import sys

water = 400
milk = 540
beans = 120
cups = 9
money = 550

def showStatus():
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(beans, " of coffee beans")
    print(cups, " of disposable cups")
    print(money, " of money")

def makeCoffee(waterNeed, milkNeed, BeansNeed, MoneySpend): 
    global water, milk, beans, cups, money

    enoughRes = True
    if  water < waterNeed:
        print("Sorry, not enough water!")
        enoughRes = False
    
    if  milk < milkNeed:
        print("Sorry, not enough milk!")
        enoughRes = False

    if  beans < BeansNeed:
        print("Sorry, not enough coffee beans!")
        enoughRes = False

    if  cups < 1:
        print("Sorry, not enough disposable cups!")
        enoughRes = False

    if enoughRes:
        water -= waterNeed
        milk -= milkNeed
        beans -= BeansNeed
        money += MoneySpend
        cups -= 1
        print("I have enough resources, making you a coffee!")
    
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "remaining":
        showStatus()
    elif action == "buy":
        option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        #  For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        #  For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        #  And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.    
        if option == "back":
            continue
        elif option == "1":
            makeCoffee(250, 0, 16, 4)
        elif option == "2":
            makeCoffee(350, 75, 20, 7)
        elif option == "3":
            makeCoffee(200, 100, 12, 6)
    elif action == "fill":
        w = int(input("Write how many ml of water do you want to add:"))
        m = int(input("Write how many ml of milk do you want to add:"))
        b = int(input("Write how many grams of coffee beans do you want to add:"))
        c = int(input("Write how many disposable cups of coffee do you want to add:"))
        water += w
        milk += m
        beans += b
        cups += c
    elif action == "take":
        print("I gave you $" + str(money))
        money = 0
    elif action == "exit":
        exit()

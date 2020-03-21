class CoffeeMachine:

    state = 'OFF'

    def __init__(self):
        self.water = 400
        self.milk = 450
        self.beans = 120
        self.cups = 9
        self.money = 550

    def cofmach(self, user_input):
        if user_input == 'buy':
            self.drink = input(
                "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            self.state = 'choosing a type of coffee'
            if self.drink == 'back':
                return
            else:
                if self.drink == '1':
                    if self.water <= 250:
                        print("Sorry, not enough water!")
                        if self.beans <= 16:
                            print("Sorry, not enough beans!")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.beans -= 16
                        self.money += 4
                        self.cups -= 1

                elif self.drink == '2':
                    if self.water <= 350:
                        print("Sorry, not enough water!")
                        if self.milk <= 75:
                            print("Sorry, not enough milk!")
                            if self.beans <= 16:
                                print("Sorry, not enough beans!")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350
                        self.milk -= 75
                        self.beans -= 20
                        self.money += 7
                        self.cups -= 1
                elif self.drink == '3':
                    if self.water <= 200:
                        print("Sorry, not enough water!")
                        if self.milk <= 100:
                            print("Sorry, not enough milk!")
                            if self.beans <= 12:
                                print("Sorry, not enough beans!")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200
                        self.milk -= 100
                        self.beans -= 12
                        self.money += 6
                        self.cups -= 1

        elif user_input == 'fill':
            self.state = 'Refilling resources'
            self.water += abs(int(input("\nWrite how many ml of water do you want to add:\n")))
            self.milk += abs(int(input("Write how many ml of milk do you want to add:\n")))
            self.beans += abs(int(input("Write how many grams of coffee beans do you want to add:\n")))
            self.cups += abs(int(input("Write how many disposable cups of coffee do you want to add:\n")))

        elif user_input == 'take':
            self.state = 'Withdraw the money'
            print(f"\nI gave you ${self.money}")
            self.money -= self.money

        elif user_input == 'remaining':
            self.state = 'Current state of the machine'
            print('\nThe coffee machine has:')
            print(f'{self.water} of water')
            print(f'{self.milk} of milk')
            print(f'{self.beans} of coffee beans')
            print(f'{self.cups} of disposable cups')
            print(f'{self.money} of money')


obj = CoffeeMachine()
while True:
    inp = input('\nWrite action (buy, fill, take, remaining, exit):\n')
    if inp == 'exit':
        break
    else:
        obj.cofmach(inp)

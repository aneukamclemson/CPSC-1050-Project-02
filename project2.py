"""
Author:         Andrew Martin Neukamm
Date:           4/25/2024
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

This program allows the user to  go through a Star Wars RPG (role play game). When they play the game, they are able to choose a planet to land on. There, they can search around, leave the planet, 
or exit the game. If they search, they can find an item (which helps their health), they can find nothing (which does nothing), or they could find a sith chasing them down and battle them (which could kill them).
If they decide to leave the planet they can go to another planet and choose the same options there. If they no longer wish to play they can quit the game.

"""
import random

class Jedi:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = random.randint(5,25)
        self.inventory = {}  # Initialize an empty inventory dictionary

    def printname(self):
        print(f'Welcome to the Rebellion {self.name}!')

    def name(self):
        return self.name

class Sith:
    def __init__(self, name, hp=50, attack=10):
        self.name = name
        self.hp = hp
        self.attack = attack

class Planet:
    def __init__(self, planet = 'in space hiding from the Empire !!!\n'):
        self.planet = planet
        print(f'\nYou are currently {self.planet}')

    def chosen_planet(self):
        # Displays a list of planets for the player to choose from
        planet_list = ['1: Hoth', '2: Mustafar', '3: Tatooine', '4: Coruscant', '5: Alderaan']
        for i in planet_list:
            print(i)
        print()

    def explore(self, jedi):
        # Allows the player to explore different planets
        while True:
            self.chosen_planet()
            landed_planet = input('Choose a planet to land on: ').strip()
            while not landed_planet.isnumeric():
                print('Not a number')
                landed_planet = input('Choose a planet to land on (1,2,3,4,5): ').strip()
            print()
            counter = True
            if landed_planet == '1':
                self.hoth(jedi)
            elif landed_planet == '2':
                self.mustafar(jedi)
            elif landed_planet == '3':
                self.tatooine(jedi)
            elif landed_planet == '4':
                self.coruscant(jedi)
            elif landed_planet == '5':
                self.alderaan(jedi)
            elif landed_planet == 'quit':
                exit()
            else:
                print("Invalid input, please try again.")

    def hoth(self, jedi):
        # Displays information about Hoth and provides options for the player
        print ("You landed on Hoth, which is an icy planet with a snowy atmosphere and freezing temperatures. Reminder to beware of Wampas!")
        print('Here are your options:')
        self.options()
        options_choice = input().strip()
        self.options_choice(options_choice, jedi)

    def mustafar(self, jedi): 
        # Displays information about Mustafar and provides options for the player
        print ("You landed on Mustafar, which is a volcanic planet with an ashy and smoke-filled atmosphere. (Fun fact, this is the planet that Obi Wan and Anakin battled in Revenge of the Sith!)")
        print('Here are your options:')
        self.options()
        options_choice = input().strip()
        self.options_choice(options_choice, jedi)

    def tatooine(self, jedi):
        # Displays information about Tatooine and provides options for the player
        print ("You landed on Tatooine, which is a desert planet that has two suns. This is the planet where Anakin and Luke Skywalker were raised. Watch out for Tusken Raiders!")
        print('Here are your options:')
        self.options()
        options_choice = input().strip()
        self.options_choice(options_choice, jedi)

    def coruscant(self, jedi):
        # Displays information about Coruscant and provides options for the player
        print ("You landed on Coruscant, which is a city planet that has nothing but skyscrapers and buildings. This is the capital of the Republic.")
        print('Here are your options:')
        self.options()
        options_choice = input().strip()
        self.options_choice(options_choice, jedi)

    def alderaan(self, jedi):
        # Displays information about Alderaan and provides options for the player
        print ("You landed on Alderaan, which is a planet that consists of beautiful mountains, trees, and lakes. This is where Princess Leia is from.")
        print('Here are your options:')
        self.options()
        options_choice = input().strip()
        self.options_choice(options_choice, jedi)

    def options(self):
        # Displays options for the player
        print('1: Search the planet')
        print('2: Leave the planet')
        print('3: Quit the game')

    def options_choice(self, option_input, jedi):
        # Processes the player's choice and performs corresponding actions
        outcome = Outcome()
        while True:
            if option_input == '1':
                random_outcome = random.randint(1,3)
                if random_outcome == 1:
                    outcome.item(jedi)
                elif random_outcome == 2:
                    outcome.sith(jedi)
                elif random_outcome == 3:
                    outcome.nothing(jedi)
                self.options()
                option_input = input().strip()
            elif option_input == '2':
                print()
                self.explore(jedi)
            elif option_input == '3':
                exit()
            else:
                try:
                    raise ValueError("Invalid input. Please input an option (1, 2, 3): ")
                except ValueError as e:
                    print(e)
                    option_input = input().strip()

def battle(jedi, sith):
    # Initiates a battle between a Jedi and a Sith
    print(f"{sith.name} emerges from the dark!")
    while jedi.hp > 0 and sith.hp > 0:
        print(f"{jedi.name} HP: {jedi.hp}  {sith.name} HP: {sith.hp}")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter your choice: ")

        if choice == "1":
            damage = random.randint(0, jedi.attack)
            print(f"{jedi.name} attacks {sith.name} for {damage} damage!")
            sith.hp -= damage
            if sith.hp <= 0:
                print(f"{jedi.name} defeated {sith.name}!")
                break
            sith_damage = random.randint(0, sith.attack)
            print(f"{sith.name} attacks {jedi.name} for {sith_damage} damage!")
            jedi.hp -= sith_damage
            if jedi.hp <= 0:
                print(f"{sith.name} defeated {jedi.name}!")
                print("The Force has been disrupted... As your lightsaber extinguishes, the darkness overwhelms you. Your journey as a Jedi ends here. May the Force guide you in the next life. Game Over.")
                exit()
                break
        elif choice == "2":
            print(f"{jedi.name} ran away from {sith.name}!")
            run_weakness(jedi)
            break
        else:
            print("Invalid choice. Try again.")

def gain_item(jedi):
    # Gives the Jedi a random item and increases their HP
    items_dict = {'holocron': 50, 'kyber crystal': 35, 'glass of spotchka': 15}
    key, val = random.choice(list(items_dict.items()))
    print('The Force guides you to good things!')
    print(f'You found a {key} and gain {val} HP')
    if key in jedi.inventory:
        jedi.inventory[key] += 1  # Increase the amount of the existing item
    else:
        jedi.inventory[key] = 1  # Add the item to the inventory with amount 1
    jedi.hp += val
    print(f'Your current health is {jedi.hp} HP')
    print('Your inventory:')
    for item, amount in jedi.inventory.items():
        print(f'{item}: {amount}')

def run_weakness(jedi):
    # Decreases Jedi's HP for running away from a Sith
    health_list = [0,5,15,20]
    health_random = random.choice(health_list)
    print(f'You lose {health_random} hp for running away')
    jedi.hp -= health_random
    print(f'{jedi.name} HP: {jedi.hp}')

class Outcome:
    def __init__(self):
        pass
    
    def item(self, jedi):
        gain_item(jedi)

    def sith(self, jedi):
        # Initiates a battle with a Sith
        sith_dict = {'Darth Sidious': 65, 'Darth Vader': 50, 'Darth Tyrannus':35, 'Darth Maul': 20}
        key, val = random.choice(list(sith_dict.items()))
        random_attack = random.randint(15,35)
        sith = Sith(key, val, random_attack)
        battle(jedi, sith)

    def nothing(self, jedi):
        # Displays a message when nothing is found during exploration
        nothing_list = ['You searched for a while and found nothing.','You came upon some locals and they gave you no help, and you found nothing.', 'You landed in a remote spot and nothing is there.' ]
        nothing_random = random.choice(nothing_list)
        print(nothing_random)

def main():
    print("Welcome to Star Wars Adventure Galaxy!")
    jedi_name = input("Enter your Jedi name: ")
    jedi = Jedi(jedi_name)
    jedi.printname()
    planet = Planet() 
    outcome = Outcome()
    planet.explore(jedi)

if __name__ == "__main__":
    main()

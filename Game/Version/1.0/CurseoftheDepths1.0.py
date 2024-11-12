import time
import textwrap
import random
from colorama import Fore, Style

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.attack = 10
        self.defense = 0
        self.xp = 0
        self.agility = 5
        self.gold = 0
        self.inventory = []

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 2
        self.defense += 2
        self.agility += 1

    def display_stats(self):
        print(f"\n{Fore.CYAN}{self.name}'s Stats:{Style.RESET_ALL}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Agility: {self.agility}")
        print("Inventory:", self.inventory)

def fight(character, monster):
    print(f"{monster['name']} Appears!")
    monster_health = monster['health']  # Store the original health of the monster
    while character.health > 0 and monster_health > 0:
        action = input("Attack (A) or Run (R)").lower()
        if action == 'a':
            damage = max(0, character.attack - monster['defense'])
            monster_health -= damage
            print(f"The {monster['name']} takes {damage} damage!")
        
            if monster_health > 0:
                monsterdamage = max(0, monster['attack'] - character.defense)
                character.health -= monsterdamage
                print(f"You take {monsterdamage} damage!")
            else:
                print(f"You have defeated {monster['name']}!")
                character.level_up()
                return True
        elif action == 'r':
            print(f"You escaped from {monster['name']}.")
            return False

    # If player is defeated
    if character.health <= 0:
        print(f"You have been defeated by {monster['name']}!")
        character.gold //= 2  # Halve the player's gold
        character.health = 10  # Set the player's health to 10
        print(f"Your gold is now {character.gold} and your health is set to 10.")
        return False


goblin = {"name": "Goblin", "health": 30, "attack": 8, "defense": 2}

def main():
    print("Welcome to the game")
    player_name = input("Enter your character name: ")
    player = Character(player_name)

    while True:
        print("\nYou are in the village. Where would you like to go?")
        print("1. Venture into the Wilderness (Fight monsters)")
        print("2. Check your stats")
        print("3. Exit game")

        choice = input("Choose a destination :")

        if choice == '1':
            fight(player, goblin)
        elif choice == '2':
            player.display_stats()
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

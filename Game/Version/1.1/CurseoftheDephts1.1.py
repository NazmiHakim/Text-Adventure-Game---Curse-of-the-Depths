import time
import textwrap
import random
from colorama import Fore, Style

class Weapon :
    def __init__(self, name, attack_bonus, price):
        self.name = name
        self.attack_bonus = attack_bonus
        self.price = price

    def __str__(self):
        return f"{self.name} (+{self.attack_bonus} Attack) - {self.price} Gold"
    
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
        self.equipped_weapon = None
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
        print(f"Gold: {self.gold}")
        print("Inventory:", [item['name'] for item in self.inventory])
        if self.equipped_weapon:
            print(f"Equipped Weapon: {self.equipped_weapon['name']}")
        else:
            print("Equipped Weapon: None")
    
    def self_weapon(self, weapon):
        self.equipped_weapon = weapon
        self.attack += weapon['attack_bonus']

    def add_to_inventory(self, item):
        self.inventory.append(item)

#weapons 
wooden_sword = {"name" : "Wooden Sword", "attack_bonus" : 5, "price" : 15}
stone_sword = {"name" : "Stone Sword", "attack_bonus" : 12, "price" :35}
iron_sword = {"name" : "Iron Sword", "attack_bonus" : 18, "price" : 60}

def blacksmith(character):
    print("Welcome to the blacksmith, Adventurer!\nCome take a look")
    print("1. Buy a weapon")
    print("2. Upgrade your weapon")
    choice = input("What do you want to do? ")
    if choice == "1":
        print("Available weapons:")
        weapons = [wooden_sword, stone_sword, iron_sword]
        for idx, weapon in enumerate(weapons, 1):
            print(f"{idx}. {weapon['name']}, (+{weapon['attack_bonus']} Attack), {weapon['price']} gold")
        
        weapon_choice = input("Which one would you like to buy?")

        if weapon_choice in ['1','2','3']:
            weapon = weapons[int(weapon_choice) - 1]
            if character.gold >= weapon['price']:
                character.gold -= weapon['price']
                character.add_to_inventory(weapon)
                character.self_weapon(weapon)
                print(f"You bought the {weapon['name']} and equipped it!")

            else:
                print("You don't have enough gold.")
        else:
            print("Invalid choice")
    elif choice == '2':
        if character.equipped_weapon:
            print("Upgrading is currently unavailable, but stay tuned!")
        else:
            print("You have no weapon equipped to upgrade.")
    else:
        print("Invalid choice.")

def fight(character, monster):
    print(f"{monster['name']} Appears!")
    monster_health = monster['health']  # Store the original health of the monster
    while character.health > 0 and monster_health > 0:
        action = input("Attack (A) or Run (R) : ").lower()
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
                print(f"You got {monster['gold']} gold from the {monster['name']}")
                character.level_up()
                character.gold += goblin['gold']
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


goblin = {"name": "Goblin", "health": 30, "attack": 8, "defense": 2, "gold": 10}

def main():
    print("Welcome to the game")
    player_name = input("Enter your character name: ")
    player = Character(player_name)

    while True:
        print("\nYou are in the village. Where would you like to go?")
        print("1. Venture into the Wilderness (Fight monsters)")
        print("2. Check your stats")
        print("3. Visit the blacksmith")
        print("4. Exit game")

        choice = input("Choose a destination : ")

        if choice == '1':
            fight(player, goblin)
        elif choice == '2':
            player.display_stats()
        elif choice == '3':
            blacksmith(player)
        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import time
import textwrap
import random
from colorama import Fore, Style
from game_data import (
    wooden_sword, stone_sword, iron_sword,
    leather_helmet, iron_helmet, steel_helmet,
    leather_plate, iron_plate, steel_plate,
    leather_gauntlets, iron_gauntlets, steel_gauntlets,
    leather_leggings, iron_leggings, steel_leggings,
    monster_categories
)

class Armor:
    def __init__(self, name, defense_bonus, price):
        self.name = name
        self.defense_bonus = defense_bonus
        self.price = price

class Weapon:
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
        self.gold = 10
        self.equipped_weapon = None
        self.equipped_armor_helmet = None
        self.equipped_armor_plate = None
        self.equipped_armor_gauntlets = None
        self.equipped_armor_leggings = None
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
        
        # Display equipped items with checks
        equipped_items = [
            ("Weapon", self.equipped_weapon),
            ("Helmet", self.equipped_armor_helmet),
            ("Plate", self.equipped_armor_plate),
            ("Gauntlets", self.equipped_armor_gauntlets),
            ("Leggings", self.equipped_armor_leggings)
        ]
        
        for item_type, item in equipped_items:
            if item:
                print(f"Equipped {item_type}: {item['name']}")
            else:
                print(f"Equipped {item_type}: None")

    def equip_weapon(self, weapon):
        if self.equipped_weapon:
            self.attack -= self.equipped_weapon['attack_bonus']
        self.equipped_weapon = weapon
        self.attack += weapon['attack_bonus']

    def equip_armor(self, armor, armor_type):
        armor_slots = {
            'helmet': 'equipped_armor_helmet',
            'plate': 'equipped_armor_plate',
            'gauntlets': 'equipped_armor_gauntlets',
            'leggings': 'equipped_armor_leggings'
        }
        slot = armor_slots[armor_type]
        current_armor = getattr(self, slot)

        if current_armor:
            self.defense -= current_armor['defense_bonus']

        setattr(self, slot, armor)
        self.defense += armor['defense_bonus']

    def add_to_inventory(self, item):
        self.inventory.append(item)

def blacksmith(character):
    while True:
        print("Welcome to the blacksmith, Adventurer!\nCome take a look")
        print("1. Buy a weapon")
        print("2. Upgrade your weapon")
        print("3. Buy an armor")
        print("4. Upgrade your armor")
        print("5. Exit")
        choice = input("What do you want to do? ")

        if choice == "1":
            print("Available weapons:")
            weapons = [wooden_sword, stone_sword, iron_sword]
            for idx, weapon in enumerate(weapons, 1):
                print(f"{idx}. {weapon['name']}, (+{weapon['attack_bonus']} Attack), {weapon['price']} gold")
            
            weapon_choice = input("Which one would you like to buy? ")

            if weapon_choice in ['1', '2', '3']:
                weapon = weapons[int(weapon_choice) - 1]
                if character.gold >= weapon['price']:
                    character.gold -= weapon['price']
                    character.add_to_inventory(weapon)
                    character.equip_weapon(weapon)
                    print(f"You bought the {weapon['name']} and equipped it!")
                else:
                    print("You don't have enough gold.")
            else:
                print("Invalid choice.")
        
        elif choice == '3':
            print("Armor types:")
            print("1. Helmet")
            print("2. Plate")
            print("3. Gauntlets")
            print("4. Leggings")
            armor_choice = input("Select armor type: ")

            if armor_choice == '1':
                print("Available helmets:")
                helmets = [leather_helmet, iron_helmet, steel_helmet]
                for idx, helmet in enumerate(helmets, 1):
                    print(f"{idx}. {helmet['name']}, (+{helmet['defense_bonus']} Defense), {helmet['price']} gold")
                item_choice = input("Which one would you like to buy? ")
                if item_choice in ['1', '2', '3']:
                    helmet = helmets[int(item_choice) - 1]
                    if character.gold >= helmet['price']:
                        character.gold -= helmet['price']
                        character.add_to_inventory(helmet)
                        character.equip_armor(helmet, 'helmet')
                        print(f"You bought the {helmet['name']} and equipped it!")
                    else:
                        print("You don't have enough gold.")
                else:
                    print("Invalid choice.")
            
            elif armor_choice == '2':
                print("Available plates:")
                plates = [leather_plate, iron_plate, steel_plate]
                for idx, plate in enumerate(plates, 1):
                    print(f"{idx}. {plate['name']}, (+{plate['defense_bonus']} Defense), {plate['price']} gold")
                item_choice = input("Which one would you like to buy? ")
                if item_choice in ['1', '2', '3']:
                    plate = plates[int(item_choice) - 1]
                    if character.gold >= plate['price']:
                        character.gold -= plate['price']
                        character.add_to_inventory(plate)
                        character.equip_armor(plate, 'plate')
                        print(f"You bought the {plate['name']} and equipped it!")
                    else:
                        print("You don't have enough gold.")
                else:
                    print("Invalid choice.")
            
            elif armor_choice == '3':
                print("Available gauntlets:")
                gauntlets = [leather_gauntlets, iron_gauntlets, steel_gauntlets]
                for idx, gauntlet in enumerate(gauntlets, 1):
                    print(f"{idx}. {gauntlet['name']}, (+{gauntlet['defense_bonus']} Defense), {gauntlet['price']} gold")
                item_choice = input("Which one would you like to buy? ")
                if item_choice in ['1', '2', '3']:
                    gauntlet = gauntlets[int(item_choice) - 1]
                    if character.gold >= gauntlet['price']:
                        character.gold -= gauntlet['price']
                        character.add_to_inventory(gauntlet)
                        character.equip_armor(gauntlet, 'gauntlets')
                        print(f"You bought the {gauntlet['name']} and equipped it!")
                    else:
                        print("You don't have enough gold.")

            if armor_choice == '4':
                print("Available leggings:")
                leggings = [leather_leggings, iron_leggings, steel_leggings]
                for idx, legging in enumerate(leggings, 1):
                    print(f"{idx}. {legging['name']}, (+{legging['defense_bonus']} Attack), {legging['price']} gold")
                    legging_choice = input("Which one would you like to buy?")
                    if legging_choice in ['1','2','3']:
                        legging = leggings[int(weapon_choice) - 1]
                        if character.gold >= legging['price']:
                            character.gold -= legging['price']
                            character.add_to_inventory(legging)
                            character.equip_armor(legging)
                            print(f"You bought the {weapon['name']} and equipped it!")
                        else:
                            print("You don't have enough gold.")
        elif choice == '4':
            print("Under Development")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def tavern(character):
    while True:
        print("Welcome to the Tavern!")
        print("1. Rent a room and rest (50 gold)")
        print("2. Exit")

        choice = input("What do you want to do?")
        if choice == '1':
            if character.gold >= 50:
                character.health += 30
        elif choice == '2':
            break
    
def encounter_monster(location):
    if location not in monster_categories:
        return None  # Invalid location
    
    monsters = monster_categories[location]
    probabilities = [monster["probability"] for monster in monsters]
    return random.choices(monsters, weights=probabilities, k=1)[0]

def fight(character, location):
    monster = encounter_monster(location)
    if not monster:
        print("No monsters found in this area.")
        return

    print(f"\nA wild {monster['name']} appears!")
    monster_health = monster['health']

    while character.health > 0 and monster_health > 0:
        print(f"\n{monster['name']} - Health: {monster_health}")
        print(f"{character.name} - Health: {character.health}")
        action = input("Attack (A) or Run (R): ").lower()

        if action == 'a':
            damage = max(0, character.attack - monster['defense'])
            monster_health -= damage
            print(f"You deal {damage} damage to the {monster['name']}!")

            if monster_health > 0:
                monsterdamage = max(0, monster['attack'] - character.defense)
                character.health -= monsterdamage
                print(f"The {monster['name']} deals {monsterdamage} damage to you!")
            else:
                print(f"You defeated the {monster['name']}!")
                print(f"You earn {monster['gold']} gold!")
                character.gold += monster['gold']
                character.level_up()
        elif action == 'r':
            print(f"You ran away from the {monster['name']}.")
            return
        else:
            print("Invalid action!")

    if character.health <= 0:
        print("You have been defeated! You lose half your gold.")
        character.gold //= 2
        character.health = 10

def main():
    print("Welcome to the game")
    player_name = input("Enter your character name: ")
    player = Character(player_name)

    while True:
        print("\nYou are in the village. Where would you like to go?")
        print("1. Explore the wilds")
        print("2. Go to the Tavern")
        print("2. Check your stats")
        print("3. Visit the Blacksmith")
        print("4. Exit game")

        choice = input("Choose a destination: ")

        if choice == '1':
            print("1. Venture into the Forest")
            print("2. Explore the Cave")
            print("3. Climb the Mountains")
            place = input("Where do you want to go?")
            if place == '1':
                fight(player, "forest")
            elif place == '2':
                fight(player, "cave")
            elif place == '3':
                fight(player, "mountains")
        elif choice == '2':
            tavern(player)
        elif choice == '3':
            player.display_stats()
        elif choice == '4':
            blacksmith(player)
        elif choice == '5':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

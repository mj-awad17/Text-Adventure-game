# Text-based advanture game with story, map & Puzzles
# 🧙‍♂️ Text-Based Adventure Game with Story, Map & Puzzles

# instructions function for the user to understand the game

def show_instructions():
    print("""
    Welcom to Text-Based Adventure Game!
    Your quest to retrieve the 💎 Crystal of Light hidden in the tower.
    Note: Explore the map, gather items, and unlock screen chambers.

    Commands:
    - 'go [direction]': Move in a direction (north, south, east, west).
    - 'look': Look around the current location.
    - 'take [item]': Take an item from the current location.
    - 'use [item]': Use an item from your inventory.
    - 'inventory': Check your inventory.
    - 'map': Show this instructions.
    - 'quit': Exit the game.
    """)
    
# map 
def show_map():
    print("""
            [Tower]
               |
    [Hut] -- [Forest] -- [River]
               |
            [Cave]
    """)

# status of user
def show_status(current_location, inventory):
    print(f"\nYou are currently at: {current_location}")
    print(f"Your inventory: {inventory}")

# adventure game function
def adventure_game():
    rooms = {
        'Forest': {'north': 'Tower', 'east': 'River', 'south': 'Cave', 'west': 'Hut'},
        'Cave': {'north': 'Forest', 'item': 'Sword', 'locked': True},
        'River': {'west': 'Forest', 'item': 'Shield', 'locked': True},
        'Tower': {'south': 'Forest', 'locked': True, 'item': 'Crystal'},
        'Hut': {'east': 'Forest', 'item': 'Armor', 'locked': True},
    }

    global inventory, locurrent_location

    inventory = []
    location = 'Forest'

    show_instructions()
    # show_status(current_location=location, inventory=inventory)
    # show_map()

    # user input
    while True:
        show_status(current_location=location, inventory=inventory)
        
        # user input
        move = input("\nEnter command: ").strip().lower()
        if move == 'quit':
            print("Thanks for playing! Goodbye!\n")
            return
        elif move == 'map':
            show_map()
        elif move == 'inventory':
            if not inventory:
                print("Your inventory is empty.")
            else:
                print(f"Your inventory: {inventory}")

        elif move == 'look':
            print(f"You are in the {location}.")
            if 'item' in rooms[location]:
                print(f"You see a {rooms[location]['item']}.")
            elif 'item' in rooms[location] and rooms[item] not in inventory:
                print(f"You see a {rooms[location]['item']} here.")
                take = input("Do you want to take it? (yes/no): ").strip().lower()
                if take == 'yes':
                    inventory.append(rooms[location]['item'])
                    print(f"You have taken the {rooms[location]['item']}.")
                item = move.split()[1]
                if 'item' in rooms[location] and rooms[location]['item'] == item:
                    inventory.append(item)
                    print(f"You have taken the {item}.")
                else:
                    print(f"There is no {item} here to take.")
            elif move.startswith('use '):
                item = move.split()[1]
                if item in inventory:
                    if item == 'Sword' and location == 'Cave':
                        print("You use the Sword to cut through the vines blocking the path.")
                    elif item == 'Shield' and location == 'River':
                        print("You use the Shield to block the water and cross the river.")
                    elif item == 'Armor' and location == 'Hut':
                        print("You wear the Armor to protect yourself from dangers.")
                else:
                    print(f"You don't have a {item} in your inventory.")
        elif move.startswith('go '):
            direction = move.split()[1]
            if direction in rooms[location]:
                next_location = rooms[location][direction]
                # tower is locked
                if next_location == 'Tower':
                    if rooms["Tower"].get('locked') and ("Sword" in inventory and "Shield" in inventory and "Armor" in inventory):
                        print("You have unlocked the Tower!")
                location = next_location
            else:
                print("You can't go that way.")

if __name__ == "__main__":
    adventure_game()
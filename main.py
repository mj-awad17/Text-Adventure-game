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
def show_status(location, inventory):
    print(f"\nYou are currently at: {location}")
    # print(f"Your inventory: {inventory}")

# adventure game function
def adventure_game():
    rooms = {
        'Forest': {'north': 'Tower', 'east': 'River', 'south': 'Cave', 'west': 'Hut'},
        'Cave': {'north': 'Forest', 'item': 'Sword', 'locked': True},
        'River': {'west': 'Forest', 'item': 'Shield', 'locked': True},
        'Tower': {'south': 'Forest', 'locked': True, 'item': 'Crystal'},
        'Hut': {'east': 'Forest', 'item': 'Armor', 'locked': True},
    }

    inventory = []
    location = 'Forest'

    show_instructions()
    # show_status(current_location=location, inventory=inventory)
    # show_map()

    # user input
    while True:
        show_status(location, inventory)
        
        # user input
        move = input("\nEnter command: ").strip().lower()
        if move == 'quit':
            print("Thanks for playing! Goodbye!\n")
            break

        elif move == 'map':
            show_map()
        
        elif move == 'inventory':
            print(f"Your inventory: {inventory}")

        elif move == 'look':
            print(f"You are in the {location}.")
            if 'item' in rooms[location]:
                print(f"You see a {rooms[location]['item']}.\n")
            else:
                print("There is nothing here.")
            
            if 'item' in rooms[location] and rooms[location]['item'] not in inventory:
                item = rooms[location]['item']
                # print(f"You see a {item}.")
                take = input("Do you want to take it? (yes/no): ").strip().lower()
                if take == 'yes':
                    inventory.append(item)
                    print(f"You have taken the {item}.")
                else:
                    print(f"You left {item}.")
        
        # taking item
        elif move.startswith('take '):
            item = move.split(" ", 1)[1].title()
            if 'item' in rooms[location] and rooms[location]['item'] == item:
                if item not in inventory:
                    inventory.append(item)
                    print(f"You have taken the {item}.")
                else:
                    print(f"You already have the {item}.")
            else:
                print(f"There is no {item} here.")

        # going to next location
        elif move.startswith('go '):
            direction = move.split()[1]
            if direction in rooms[location]:
                next_location = rooms[location][direction]
                # tower is locked: collect items to unlock
                if next_location == 'Tower' and rooms["Tower"].get('locked'):
                    if "Sword" in inventory and "Shield" in inventory and "Armor" in inventory:
                        print("Congratulation! You have unlocked the Tower and collected the Crystal of Light 💎!")
                        rooms["Tower"]["locked"] = False
                        location = "Tower"
                    elif rooms["Tower"]["locked"]:
                        print("The Tower is locked. You need to collect the Sword, Shield, and Armor to unlock it.")
                        continue
                    else:
                        location = "Tower"
                else:
                    location = next_location
            else:
                print("You can't go that way!")

if __name__ == "__main__":
    adventure_game()
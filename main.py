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
    show_status(current_location=location, inventory=inventory)
    show_map()

if __name__ == "__main__":
    adventure_game()
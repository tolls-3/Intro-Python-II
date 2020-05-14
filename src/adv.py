from room import Room
from player import Player
import textwrap
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# create items to room
sword = Item("sword", "cut things down")
gun = Item("gun", "dun things down")
cloak = Item("cloak", "disappearing from things")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
room['outside'].items = [sword]
room['foyer'].items = [gun]
room['narrow'].items = [cloak]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Tolu", room['outside'])
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# We want to display items in the current room a player is in


def display_items():
    if len(player.currentroom.items) > 0:
        for item in player.currentroom.items:
            print(
                f'Item in this room is- {item.name.capitalize()} : {item.description} \n')
    else:
        print('no item \n')

# This allows player in a room with items to pick an item and add to inventory


def on_take():
    if len(player.currentroom.items) > 0:
        for item in player.currentroom.items:
            player.inventory.append(item)
            player.currentroom.items.remove(item)
            print(f'Your inventory is {[i for i in player.inventory]}')
    else:
        print('no item in this room to pick \n')

# This displays all items in the players inventory as they move between rooms


def display_items_inventory():
    if len(player.inventory) > 0:
        for item in player.inventory:
            print(
                f'inventory items are - {item.name.capitalize()} : {item.description} \n')
    else:
        print('no item \n')

# drop items from an inventory back into a room


def on_drop():
    if len(player.inventory) > 0:
        for item in player.inventory:
            player.inventory.remove(item)
            player.currentroom.items.append(item)
    else:
        print('no item in inventory to drop')


selection = ''

while selection != 'q':
    print(
        f'Your location is {player.currentroom.roomname}. Description: {player.currentroom.description}.')
    display_items()
    display_items_inventory()
    selection = input(
        'Enter n, s, e or w to move to another room or q to quit: \n Enter get to add item in the room to your inventory')
    try:
        if selection == "n":
            if player.currentroom.n_to != None:
                player.currentroom = player.currentroom.n_to
            else:
                print("No way here \n")

        elif selection == 's':
            if player.currentroom.s_to != None:
                player.currentroom = player.currentroom.s_to
            else:
                print("No way here \n")
        elif selection == 'w':
            if player.currentroom.w_to != None:
                player.currentroom = player.currentroom.w_to
            else:
                print("No way here \n")
        elif selection == 'e':
            if player.currentroom.e_to != None:
                player.currentroom = player.currentroom.e_to
            else:
                print("No way here \n")
        elif selection == 'get':
            on_take()
        elif selection == 'drop':
            on_drop()
    except (ValueError, RuntimeError, TypeError, AttributeError):
        print('Oops!  That was no valid number.  Try again...\n')

# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, currentroom):
        self.name = name
        self.currentroom = currentroom
        self.inventory = []

    def __str__(self):
        # return 'Player(name='+self.name+', currentroom='+str(self.currentroom) + ')'
        output = ''
        output += self.name + '' + self.currentroom + '\n'
        for index, inventory in enumerate(self.inventory):
            output += str(inventory) + '\n'
        return output

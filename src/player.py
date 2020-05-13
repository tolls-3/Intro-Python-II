# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, currentroom):
        self.name = name
        self.currentroom = currentroom
        self.inventory = []

    def __str__(self):
        return 'Player(name='+self.name+', currentroom='+str(self.currentroom) + ')'

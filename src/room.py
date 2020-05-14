# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, roomname, description):
        self.roomname = roomname
        self.description = description
        self.items = []

    def __str__(self):
        return 'roomname='+self.roomname+', description='+str(self.description)
        # output = ''

        # output += self.roomname + '' + self.description + '\n'
        # for index, item in enumerate(self.items):
        #     output += str(item) + '\n'
        # return output

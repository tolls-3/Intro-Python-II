const prompt = require('prompt-sync')({ sigint: true });
// from room import Room
const Room = require('./room')
// Declare all the rooms
const Player = require('./player')

const room = {
    "outside": new Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": new Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': new Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness.Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow': new Room("Narrow Passage", "The narrow passage bends here from west to north.The smell of gold permeates the air."),

    'treasure': new Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers.The only exit is to the south."),
}


// Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


// Main


// Make a new player object that is currently in the 'outside' room.
const newPlayer = new Player('Tolu', room['outside'])
// Write a loop that:

// # * Prints the current room name
// # * Prints the current description(the textwrap module might be useful here).
//     # * Waits for user input and decides what to do.
//         #
// # If the user enters a cardinal direction, attempt to move to the room there.
// # Print an error message if the movement isn't allowed.
// #
// # If the user enters "q", quit the game.


var selection = ''
while (selection !== 'q') {
    console.log(`Your location is ${newPlayer.currentroom.roomname}. Description: ${newPlayer.currentroom.description}.`)
    selection = prompt("Enter n, s, e or w to move to a room or q to quit:")
    if (selection === 'n') {
        if (newPlayer.currentroom.n_to) {
            newPlayer.currentroom = newPlayer.currentroom.n_to
        }
        else {
            console.log('No bridge yet')
        }
    }
    else if (selection === 's') {
        if (newPlayer.currentroom.s_to) {
            newPlayer.currentroom = newPlayer.currentroom.s_to
        }
        else {
            console.log('No bridge yet')
        }
    }
    else if (selection === 'w') {
        if (newPlayer.currentroom.w_to) {
            newPlayer.currentroom = newPlayer.currentroom.w_to
        }
        else {
            console.log('No bridge yet')
        }
    }
    else if (selection === 'e') {
        if (newPlayer.currentroom.e_to) {
            newPlayer.currentroom = newPlayer.currentroom.e_to
        }
        else {
            console.log('No bridge yet')
        }
    }
    else {
        console.log('Come back and play again')
    }

}

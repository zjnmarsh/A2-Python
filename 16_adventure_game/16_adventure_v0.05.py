class GameEntity:
    """ GameEntity: Base class for all rooms and objects in the game. """
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description
        self._contents_dict = {}

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_name(self):
        return self._name
w
class Room(GameEntity):
    """ Room: Records details of every room you can visit, including contents and names of adjacent rooms """
    def __init__(self, roomID, name, description, north="", south="", east="", west=""):
        self.nextRoomsDict = {'n': north, 's': south, 'e': east, 'w': west}
        self.objectDict = {}
        super().__init__(roomID, name, description)

    def get_adjacent_room_id(self, direction):
        roomID = self.nextRoomsDict[direction]
        return roomID

class Game:
    """ Contains the main loop, deals with interpreting user input and contains game-wide information """
    def __init__(self, startingRoomID):
        self.roomDict = {}
        self._currentRoomID = startingRoomID
        self.commandDict = {'n': self.move, 's': self.move, 'e': self.move, 'w': self.move,
                            'jump': self.jump, 'look': self.look_room, 'take': self.take, 'drop': self.drop, 'inventory' : self.inventory}

    def get_current_room(self):
        return self.roomDict[self._currentRoomID]

    def set_current_room(self, roomID):
        self._currentRoomID = roomID

    def add_room(self, room):
        self.roomDict[room.get_id()] = room

    def main_loop(self):
        while True:
            user_input = input("\n>")
            split_input = user_input.split(maxsplit=1)
            command = split_input[0]
            if len(split_input) > 1:
                arguments = split_input[1]
            else:
                arguments = ''

            if command in self.commandDict.keys():
                self.commandDict[command](command, arguments)
            else:
                print("Huh?")

    # Commands - These are things that the player can do.

    def move(self, dir_command, arguments=''):
        next_room = self.get_current_room().get_adjacent_room_id(dir_command)
        if next_room:
            self.set_current_room(next_room)
            self.look_room()
        else:
            print("You can't go that way.")

    def jump(self, command='', arguments=''):
        print("You jump up and down")

    def look_room(self, command='', arguments=''):
        print("You look in the room")
        room = self.get_current_room()
        print(room.get_description())

    def look_object(self, command='', arguments=''):
        print("You look at the ")

    def take(self, command='', arguments=''):
        pass

    def drop(self, command='', arguments=''):
        pass

    def inventory(self, command='', arguments=''):
        pass






##### Setup Rooms and Object #####
game = Game("room1")
game.add_room(Room("room1", "A Room", "You are in a room. The door is north of here.", north="beach"))
game.add_room(Room("beach", "The beach", "You are standing on a sandy beach. The sea stretches out to the horizon the the east. A small hut stands to the south", south="room1", east="sea"))
game.add_room(Room("sea", "At Sea", "You are drifting at sea. How did this happen?", west="beach"))

### Start the loop ###
game.main_loop()

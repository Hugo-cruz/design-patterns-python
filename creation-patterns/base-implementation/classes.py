from abc import ABC, abstractmethod
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3 
    WEST = 4


class MapSite(ABC):
    @abstractmethod
    def Enter(self):
        self.enter = 0


class Room(MapSite):
    def __init__(self, roomNo) -> None:
        super().__init__()
        self.roomNo = roomNo
        self.directions = {}


    def get_side(self,direction:Direction) -> MapSite:
        return self.directions[direction]
    
    def set_side(self,direction:Direction,map_site:MapSite):
        self.directions[direction] = map_site
    
    def Enter(self):
        self.enter = 0

class Wall(MapSite):
    def __init__(self) -> None:
        super().__init__()

    def Enter(self):
        self.enter = 0

class Door(MapSite):
    def __init__(self, room_from:MapSite, room_to:MapSite) -> None:
        super().__init__()
        self.room_from = room_from
        self.room_to = room_to
        self.is_open = True

    def Enter(self):
        if(self.is_open == True):
            self.enter = 1
        else:
            self.enter = 0
    
    def set_open(self,bool_value:bool):
        self.is_open = bool_value


class Maze():
    def __init__(self) -> None:
        self.rooms = {}
        
    def addRoom(self,room:Room) -> None:
        self.rooms[room.roomNo] = room
    
    def roomNo(self,num:str) -> Room:
        return self.rooms[num]


class MazeGame():
    def __init__(self) -> None:
        self.aMaze = Maze()
        r1 = Room("1")
        r2 = Room("2")
        theDoor = Door(r1,r2)

        self.aMaze.addRoom(r1)
        self.aMaze.addRoom(r2)

        r1.set_side(Direction.NORTH,Wall())
        r1.set_side(Direction.EAST,theDoor)
        r1.set_side(Direction.SOUTH,Wall())
        r1.set_side(Direction.WEST,Wall())

        r2.set_side(Direction.NORTH,Wall())
        r2.set_side(Direction.EAST,Wall())
        r2.set_side(Direction.SOUTH,Wall())
        r2.set_side(Direction.WEST,theDoor)

    def createMaze(self):
        return self.aMaze







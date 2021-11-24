from abc import ABC, abstractmethod
from .classes import Maze,Wall,Room,Door,Direction

class MazeFactory(ABC):
    #@abstractmethod
    def MakeMaze(self):
        return Maze()

    
    #@abstractmethod
    def MakeWall(self):
        return Wall()

    #@abstractmethod
    def MakeRoom(self,n:int):
        return Room(n)
    
    
    #@abstractmethod
    def MakeDoor(self,room1:Room,room2:Room):
        return Door(room1,room2)


    

class MazeGame():
    def __init__(self,factory:MazeFactory) -> None:
        self.aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom("1")
        r2 = factory.MakeRoom("2")
        theDoor = factory.MakeDoor(r1,r2)

        self.aMaze.addRoom(r1)
        self.aMaze.addRoom(r2)

        r1.set_side(Direction.NORTH,factory.MakeWall)
        r1.set_side(Direction.EAST,theDoor)
        r1.set_side(Direction.SOUTH,factory.MakeWall())
        r1.set_side(Direction.WEST,factory.MakeWall())

        r2.set_side(Direction.NORTH,factory.MakeWall)
        r2.set_side(Direction.EAST,factory.MakeWall)
        r2.set_side(Direction.SOUTH,factory.MakeWall)
        r2.set_side(Direction.WEST,theDoor)

    def createMaze(self):
        return self.aMaze



from creationpatterns.abstractfactory import factory as fac
from creationpatterns.abstractfactory import classes as classes
#from .classes import MazeGame

def main():
    factory = fac.MazeFactory()
    maze = fac.MazeGame(factory)
    print(maze.createMaze())
    print("ok")

if __name__ == "__main__":
    main()
from creationpatterns.abstractfactory import factory
from .classes import MazeGame

def main():
    factory = fac.MazeFactory()
    maze = MazeGame(factory)
    print(maze.createMaze())
    print("ok")

if __name__ == "__main__":
    main()
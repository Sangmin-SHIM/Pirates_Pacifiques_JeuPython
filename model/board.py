from random import randint

from model.square.fond import Fond
from model.square.greensquare import GreenSquare
from model.square.redsquare import RedSquare
from model.square.square import Square
from model.square.obstacle import Obstacle
from model.square.freesquare import FreeSquare
from contract.iboard import IBoard

# Obstacle
from model.square.obstaclerock import RockObstacle
from model.square.obstaclebarrel import BarrelObstacle
from model.square.obstaclebuoy import BuoyObstacle
from model.square.obstaclerockgold import RockGoldObstacle
from model.square.obstaclepannel import PannelObstacle
# Rock
from model.square.rock import Rock
from model.square.rock2 import Rock2
from model.square.rock3 import Rock3
from model.square.rock4 import Rock4
# Sand
from model.square.sand import Sand
# Rock_pic
from model.square.rock_pic import RockPic
from model.square.rock_pic2 import RockPic2


class Board(IBoard):
    __width: int
    __height: int
    __squares = [[Square]]
    __obstacles: [Obstacle]
    __freeSquares: [FreeSquare]

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__squares = [[None] * width for _ in range(height)]
        self.__obstacles = [RedSquare(), GreenSquare(), RockObstacle(), Rock(), Sand(), Rock2(), Rock3(), Rock4(), BarrelObstacle(), BuoyObstacle(), RockObstacle(), RockGoldObstacle(), PannelObstacle()]
        self.__freeSquares = [Fond(), RockPic(), RockPic2()]
        self.__fillBoard()

    def __fillBoard(self):
        for i in range(0, self.__width):
            for j in range(0, self.__height):
                # Added (Sangmin)

                # Sand
                if ( j == 18 or j == 19 or j==0 or j == 1):
                    self.__squares[j][i] = self.__obstacles[4]
                # Rock
                elif ( j == 17):
                    self.__squares[j][i] = self.__obstacles[3]
                elif (j == 16):
                    self.__squares[j][i] = self.__obstacles[5]
                elif(j==3):
                    self.__squares[j][i] = self.__obstacles[6]
                elif(j==2):
                    self.__squares[j][i] = self.__obstacles[7]


                # RockObstacle
                elif (j==13 and i != 4 and i !=5):
                    self.__squares[j][i] = self.__obstacles[2]

                # BarrelObstacle
                elif (j==11 and i != 7 and i !=6):
                    self.__squares[j][i] = self.__obstacles[8]

                # BuoyObstacle
                elif (j==9 and i !=0 and i !=1):
                    self.__squares[j][i] = self.__obstacles[9]

                # RockGoldObstacle
                elif (j==7 and i !=3 and i !=4):
                    self.__squares[j][i] = self.__obstacles[11]

                # PannelObstacle
                elif (j == 5 and i != 10 and i != 11):
                    self.__squares[j][i] = self.__obstacles[12]


                # # Whirlwind
                # elif (i % randint(1, self.__width) == 1 and j % randint(1, self.__height) == 1):
                #     self.__squares[j][i] = self.__obstacles[3]

                # RockPic
                elif ( j == 15):
                    self.__squares[j][i] = self.__freeSquares[1]
                elif ( j == 4):
                    self.__squares[j][i] = self.__freeSquares[2]
                else:
                    self.__squares[j][i] = self.__freeSquares[0]

    def getSquares(self) -> [[Square]]:
        return self.__squares

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

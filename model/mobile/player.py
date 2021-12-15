import tkinter
from _datetime import datetime

from model.behaviormove.movebyplayer import MoveByPlayer
from model.mobile.mobile import Mobile
from model.square.sprite import Sprite


class Player(Mobile):
    __nextDirection: int
    # Added (Gaston)
    __lifePoints: int
    __invincible: bool
    __time: datetime
    #/// Added (Gaston)

    def __init__(self, x: int, y: int):
        self.__nextDirection = -1
        # Added (Gaston)
        self.__lifePoints = 3
        self.__invincible = False
        self.__time = datetime.now()
        Mobile.__init__(self, x, y, True, Sprite("image/vie3.png"), MoveByPlayer())

    def die(self) -> None:
        # Added (Gaston)
        if self.__invincible:
            ...
        else:
            self.__invincible = True
            self.__time = datetime.now()
            self.__lifePoints -= 1
            if self.__lifePoints == 2:
                self.setSprite(Sprite("image/vie2.png"))
            if self.__lifePoints == 1:
                self.setSprite(Sprite("image/vie1.png"))
            if self.__lifePoints <= 0:
                Mobile.die(self)
                self.setSprite(Sprite("image/vie0.png"))

    def setNextDirection(self, nextDirection: int) -> None:
        if 0 >= nextDirection >= 3:
            self.__nextDirection = nextDirection
        else:
            self.__nextDirection = -1

    def goUp(self) -> None:
        self.__nextDirection = 0

    def goRight(self) -> None:
        self.__nextDirection = 1

    def goDown(self) -> None:
        self.__nextDirection = 2

    def goLeft(self) -> None:
        self.__nextDirection = 3

    def getNextDirection(self) -> int:
        return self.__nextDirection

    def getInvincible(self):
        return self.__invincible

    def setInvincible(self, isInvincible: bool):
        self.__invincible = isInvincible

    def getTime(self):
        return self.__time

    def setTime(self, time: datetime):
        self.__time = time

    def getLifePoints(self) -> int:
        return self.__lifePoints
from datetime import datetime

from model.behaviormove.behaviormove import BehaviorMove
# Sprite -> Photo
from model.square.sprite import Sprite


class MoveNavireDeLigne(BehaviorMove):
    __stepX: int

    __counterMouv: int

    def __init__(self):
        self.__stepX = 1
        self.__counterMouv = 0

    def getTarget(self) -> [int]:
        if self._mobile.getX() >= self._mobile.getModel().getBoard().getWidth() - 1:
            self.__stepX = -1
            self._mobile.setSprite(Sprite("image/fregate_gauche.png"))

        if self._mobile.getX() <= 0:
            self.__stepX = 1
            self._mobile.setSprite(Sprite("image/fregate_droite.png"))

        newX = self._mobile.getX() + self.__stepX
        newY = self._mobile.getY()

        playerX = self._mobile.getModel().getPlayer().getX()
        playerY = self._mobile.getModel().getPlayer().getY()

        #CollisionFregate
        if newX == playerX and newY == playerY:
            self._mobile.getModel().getPlayer().die()

        #Invincible = False

        if self._mobile.getModel().getPlayer().getInvincible:

            if (datetime.now() - self._mobile.getModel().getPlayer().getTime()).seconds > 1:

                self._mobile.getModel().getPlayer().setInvincible(False)

        return newX, newY

    def move(self):
        if self.__counterMouv % 0.5 == 0:
           BehaviorMove.move(self)
        self.__counterMouv += 1

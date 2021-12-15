from random import randint

from contract.imodel import IModel
from contract.iplayer import IPlayer
from model.board import Board
from model.mobile.bombe import Bombe
from model.mobile.mobile import Mobile, IMobile
from model.mobile.navireDeLigne import NavireDeLigne
from model.mobile.player import Player
from model.mobile.fregate import Fregate


class Model(IModel):
    __board: Board
    __mobiles: [Mobile]
    __player: IPlayer

    def __init__(self):
        self.__board = Board(20, 20)
        self.__mobiles = []

    def getBoard(self):
        return self.__board

    def __addMobile(self, mobile: Mobile) -> None:
        self.__mobiles.append(mobile)
        mobile.setModel(self)

    def addFregate(self) -> None:
        self.__addMobile(Fregate(randint(1, self.getBoard().getWidth() - 1), 12))
        self.__addMobile(Fregate(randint(1, self.getBoard().getWidth() - 1), 10))
        self.__addMobile(Fregate(randint(1, self.getBoard().getWidth() - 1), 8))
        self.__addMobile(Fregate(randint(1, self.getBoard().getWidth() - 1), 6))
        self.__addMobile(Fregate(randint(1, self.getBoard().getWidth() - 1), 4))

    def addNavireDeLigne(self) -> None:
        self.__addMobile(NavireDeLigne(randint(1, self.getBoard().getWidth() - 1), 14))

    def addBombe(self) -> None:
        self.__addMobile(Bombe(11, 5))
        self.__addMobile(Bombe(4, 7))
        self.__addMobile(Bombe(5, 13))
        self.__addMobile(Bombe(6, 11))
        self.__addMobile(Bombe(0, 9))

    def addPlayer(self) -> None:
        self.__player = Player(randint(0,self.getBoard().getWidth()-1), 15)
        self.__addMobile(self.__player)

    def getMobiles(self) -> [IMobile]:
        return self.__mobiles

    def getPlayer(self) -> IPlayer:
        return self.__player

    def removeMobile(self, mobile: Mobile) -> None:
        self.__mobiles.remove(mobile)

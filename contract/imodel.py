from abc import ABC, abstractmethod

from contract.iboard import IBoard
from contract.iplayer import IPlayer
from contract.imobile import IMobile
from contract.isquare import ISquare
from contract.isprite import ISprite


class IModel(ABC):
    @abstractmethod
    def getBoard(self) -> IBoard:
        ...

    @abstractmethod
    def addNavireDeLigne(self) -> None:
        ...

    @abstractmethod
    def addFregate(self) -> None:
        ...

    @abstractmethod
    def addPlayer(self) -> None:
        ...

    @abstractmethod
    def getMobiles(self) -> [IMobile]:
        ...

    @abstractmethod
    def getPlayer(self) -> IPlayer:
        ...


    # Added (Gaston)
    @abstractmethod
    def addBombe(self) -> None:
        ...

from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView
from contract.action import Action
from time import sleep
# Sprite -> Change Photo
from model.square.sprite import Sprite

class Controller(IController):
    __model: IModel
    __view: IView
    __running: bool

    def __init__(self):
        self.__running = True

    def setModel(self, model: IModel):
        self.__model = model

    def setView(self, view: IView):
        self.__view = view
        self.__view.setController(self)

    def start(self):
        self.__model.addFregate()

        self.__model.addPlayer()

        # Added (Gaston)
        self.__model.addNavireDeLigne()
        self.__model.addBombe()

        while self.__running:
            self.__view.show()
            for mobile in self.__model.getMobiles():
                mobile.move()
            sleep(0.005)

    def viewIsClosed(self) -> None:
        self.__running = False

    def performAction(self, action: Action):
        if action == Action.UP:
            self.__model.getPlayer().goUp()
            if self.__model.getPlayer().getLifePoints() == 3:
                self.__model.getPlayer().setSprite(Sprite("image/vie3.png"))
            if self.__model.getPlayer().getLifePoints() == 2:
                self.__model.getPlayer().setSprite(Sprite("image/vie2.png"))
            if self.__model.getPlayer().getLifePoints() == 1:
                self.__model.getPlayer().setSprite(Sprite("image/vie1.png"))

        elif action == Action.RIGHT:
            self.__model.getPlayer().goRight()
            if self.__model.getPlayer().getLifePoints() == 3:
                self.__model.getPlayer().setSprite(Sprite("image/vie3_droite.png"))
            if self.__model.getPlayer().getLifePoints() == 2:
                self.__model.getPlayer().setSprite(Sprite("image/vie2_droite.png"))
            if self.__model.getPlayer().getLifePoints() == 1:
                self.__model.getPlayer().setSprite(Sprite("image/vie1_droite.png"))
        #elif action == Action.DOWN:
            #self.__model.getPlayer().goDown()
        elif action == Action.LEFT:
            self.__model.getPlayer().goLeft()
            if self.__model.getPlayer().getLifePoints() == 3:
                self.__model.getPlayer().setSprite(Sprite("image/vie3_gauche.png"))
            if self.__model.getPlayer().getLifePoints() == 2:
                self.__model.getPlayer().setSprite(Sprite("image/vie2_gauche.png"))
            if self.__model.getPlayer().getLifePoints() == 1:
                self.__model.getPlayer().setSprite(Sprite("image/vie1_gauche.png"))

from model.mobile.mobile import Mobile
from model.square.sprite import Sprite
from model.behaviormove.moveNavireDeLigne import MoveNavireDeLigne


class NavireDeLigne(Mobile):
    def __init__(self, x: int, y: int):
        Mobile.__init__(self, x, y, False, Sprite("image/fregate_droite.png"), MoveNavireDeLigne())

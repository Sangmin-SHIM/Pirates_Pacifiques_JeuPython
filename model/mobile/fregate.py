from model.behaviormove.moveFregate import MoveFregate
from model.mobile.mobile import Mobile
from model.square.sprite import Sprite


class Fregate(Mobile):
    def __init__(self, x: int, y: int):
        Mobile.__init__(self, x, y, False, Sprite("image/fregate_droite.png"), MoveFregate())

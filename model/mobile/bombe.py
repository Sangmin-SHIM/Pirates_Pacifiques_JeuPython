from model.behaviormove.noMove import NoMove
from model.mobile.mobile import Mobile
from model.square.sprite import Sprite


class Bombe(Mobile):
    def __init__(self, x: int, y: int):
        Mobile.__init__(self, x, y, True, Sprite("image/bombe.png"), NoMove())


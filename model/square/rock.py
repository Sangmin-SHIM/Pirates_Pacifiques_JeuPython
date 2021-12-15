from model.square.obstacle import Obstacle


class Rock(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/rocher.png")

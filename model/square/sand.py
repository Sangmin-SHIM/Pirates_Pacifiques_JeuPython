from model.square.obstacle import Obstacle


class Sand(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/sable.png")

from model.square.obstacle import Obstacle


class Rock4(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/rocher_haut.png")

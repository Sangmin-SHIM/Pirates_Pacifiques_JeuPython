from model.square.obstacle import Obstacle


class PannelObstacle(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/obstacle_pannel.png")

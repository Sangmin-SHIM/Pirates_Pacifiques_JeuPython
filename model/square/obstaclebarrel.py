from model.square.obstacle import Obstacle


class BarrelObstacle(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/obstacle_barrel.png")

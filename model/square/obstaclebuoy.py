from model.square.obstacle import Obstacle


class BuoyObstacle(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/obstacle_buoy.png")

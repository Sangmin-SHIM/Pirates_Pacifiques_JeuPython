from model.square.obstacle import Obstacle


class RockGoldObstacle(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/obstacle_rockgold.png")

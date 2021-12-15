from model.square.obstacle import Obstacle


class RockObstacle(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/obstacle_rock.png")

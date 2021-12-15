from model.behaviormove.behaviormove import BehaviorMove
from datetime import datetime


class NoMove(BehaviorMove):

    def getTarget(self) -> [int]:
        X = self._mobile.getX()
        Y = self._mobile.getY()

        playerX = self._mobile.getModel().getPlayer().getX()
        playerY = self._mobile.getModel().getPlayer().getY()

        if X == playerX and Y == playerY:
            #Tue le joueur
            self._mobile.getModel().getPlayer().die()
            # Destroy Object
            self._mobile.getModel().removeMobile(self._mobile)




        #Invincible = False

        if self._mobile.getModel().getPlayer().getInvincible:

            if (datetime.now() - self._mobile.getModel().getPlayer().getTime()).seconds > 1:

                self._mobile.getModel().getPlayer().setInvincible(False)

        return X, Y

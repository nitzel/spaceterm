from game.coordinates import Coordinates
import game.constants


class Base:

    """This object implements all the common entities methods"""

    symbol = None
    style = game.constants.STYLE_NORMAL
    color = game.constants.COLOR_WK

    def __init__(self, uid, name, x=0, y=0, z=0):
        super(Base, self).__init__()
        self.uid = uid
        self.name = name
        self.coordinates = Coordinates(x, y, z)

    def getUid(self):
        return self.uid

    def getName(self):
        return self.name

    def getCoordinates(self):
        return self.coordinates

    def __str__(self):
        return self.symbol

from game.coordinates import Coordinates


class Base:

    """This object implements all the common entities methods"""

    symbol = None

    def __init__(self, uid, name, x=0, y=0, z=0):
        super(Base, self).__init__()
        self.uid = uid
        self.name = name
        self.coordinates = Coordinates(x, y, z)

    def getUid(self):
        return self.uid

    def getName(self):
        return self.name

    def __str__(self):
    	return self.symbol

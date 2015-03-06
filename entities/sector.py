from entities.base import Base


class Sector(Base):

    """
    The Sectors objects represent a section of space
    containing one or more star systems
    """

    symbol = 'S'  # This is show on map view

    def __init__(self, uid, name, x=0, y=0, z=0):
        super(Sector, self).__init__(uid, name, x, y, z)
        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)

    def getObjects(self):
        return self.objects

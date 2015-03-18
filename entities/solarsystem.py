from entities.base import Base
import game.constants


class SolarSystem(Base):

    """
    Solar systems objects represent a collection of a Star
    and Planets orbiting around it. It is possible to have
    a binary system (two stars orbiting each other) instead
    of a single one. The proportion is roughly 1 on 3.
    """

    symbol = 'S'  # This is shown on sector view
    decoration = game.constants.STYLE_BOLD
    color = game.constants.COLOR_WK
    isCollider = True

    def __init__(self, uid, name, x=0, y=0, z=0):
        super(SolarSystem, self).__init__(uid, name, x, y, z)
        # This is the star shown also on the sector map
        self.star = None
        # The optional star for a binary system
        self.star2 = None
        # Planets of the solar system
        self.planets = []

    def addStar(self, star):
        """
        Adds a star to the solar system. If there's already
        one star present it will add it as the secondary one,
        creating a binary system
        """
        if (not self.star):
            self.star = star

            # The color of the main star defines the color shown
            # on the map
            self.color = self.star.color
        elif (not self.star2):
            self.star2 = star

    def addPlanet(self, planet):
        self.planets.append(planet)

    def getObjects(self):
        """Return a merged array of system objects"""
        objects = []
        objects.append(self.star)

        objects.extend(self.planets)
        return objects

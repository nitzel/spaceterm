import random
from game.constants import *
from entities.sector import Sector
from entities.star import Star
from entities.solarsystem import SolarSystem


class Genesis:

    """The class that randomly generates the universe!"""

    def __init__(self, sectorCount, seed=None):
        random.seed(seed)
        self.sectorCount = sectorCount
        self.sectors = []

    def generate(self):
        for i in range(self.sectorCount):
            uid = 'S' + str(i)
            name = uid
            s = Sector(uid, name, 0, 0, 0)
            self.sectors.append(s)
            self.generateSolarSystems(s)

    def generateSolarSystems(self, sector):
        """
        Generate solar systems and append them to the specified sector
        """
        usedCoords = []
        for i in range(random.randrange(1, MAX_SS_IN_SECTOR)):
            while True:
                x = random.randrange(SECTOR_W)
                y = random.randrange(SECTOR_H)
                z = random.randrange(SECTOR_Z)

                if ((x, y, z) not in usedCoords):
                    break

            usedCoords.append((x, y, z))
            uid = 'SS' + str(x) + str(y) + str(z)
            name = uid
            ss = SolarSystem(uid, name, x, y, z)
            self.generateStars(ss)
            sector.addObject(ss)

    def generateStars(self, ss):
        """
        Generate one or two stars and append them to the specified solar system
        """
        binaryCheck = random.randrange(0, 2)  # If 0 generate a binary sys

        ss.addStar(self.generateStar(ss.uid))

        if (binaryCheck == 0):
            ss.addStar(self.generateStar(ss.uid))

    def generateStar(self, uidPrefix):
        cl = random.choice(STAR_CLASSES)
        uid = cl + uidPrefix
        name = uid
        star = Star(uid, name, SS_W / 2, SS_H / 2, 0)
        star.setClass(cl)

        return star

    def getSectors(self):
        return self.sectors

    def getSector(self, i):
        return self.sectors[i]

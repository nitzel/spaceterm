import random
from game.constants import *
from entities.sector import Sector
from entities.star import Star


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
            self.generateStars(s)

    def generateStars(self, sector):
        """
        Generate stars and append them to the specified sector
        """
        usedCoords = []
        for i in range(random.randrange(1, MAX_STARS_IN_SYS)):
            while True:
                x = random.randrange(SECTOR_W)
                y = random.randrange(SECTOR_H)
                z = random.randrange(SECTOR_Z)

                if ((x, y, z) not in usedCoords):
                    break

            usedCoords.append((x, y, z))
            cl = random.choice(STAR_CLASSES)
            uid = cl + str(x) + str(y) + str(z)
            name = uid
            star = Star(uid, name, x, y, z)
            star.setClass(cl)
            sector.addObject(star)

    def getSectors(self):
        return self.sectors

    def getSector(self, i):
        return self.sectors[i]

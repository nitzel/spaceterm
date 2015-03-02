from entities.player import Player
from entities.space import Space


class Matrix:

    """Matrix that holds all the game entities"""

    def __init__(self, w, h, z):
        super(Matrix, self).__init__()
        self.w = w
        self.h = h
        self.z = z
        self.matrix = []
        self.player = Player
        self.__initialize()

    def __initialize(self):
        """Initialize the matrix with empty space"""
        self.matrix = [[[
                Space(
                    str(x) + str(y) + str(z),
                    str(x) + str(y) + str(z),
                    x, y, z
                ) for z in range(self.z)
            ] for x in range(self.w)
            ] for y in range(self.h)
            ]

    def get(self):
        return self.matrix

    def updateLevel(self):
        """Updates the current level in the matrix"""
        # Mockup, do actual level updating
        # TODO This is really slow for some reason, so it should be optimized
        for y in range(self.h):
            for x in range(self.w):
                for z in range(self.z):
                    self.matrix[y][x][z] = Space(
                        str(x) + str(y) + str(z),
                        str(x) + str(y) + str(z),
                        x, y, z
                    )

    def positionPlayer(self):
        # TODO Convert Player to a Base object and use __str__
        self.matrix[
                self.player.getCoordinates().getY()
            ][
                self.player.getCoordinates().getX()
            ][
                self.player.getCoordinates().getZ()
            ] = self.player.symbol

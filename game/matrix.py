from entities.player import Player
from entities.space import Space


class Matrix:

    """Matrix that holds all the game entities"""

    def __init__(self, w, h, z, player):
        super(Matrix, self).__init__()
        self.w = w
        self.h = h
        self.z = z
        self.matrix = []
        self.player = player
        self.objects = []
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

    def cells2d(self, z):
        for y in range(self.h):
            for x in range(self.w):
                yield (x, y, z), self.matrix[y][x][z]

    def updateLevel(self):
        """Updates the current level in the matrix"""
        # Fill matrix with Space
        for coords, cell in self.cells2d(self.player.getCoordinates().getZ()):
            self.matrix[coords[1]][coords[0]][coords[2]] = Space(
                str(coords[0]) + str(coords[1]) + str(coords[2]),
                str(coords[0]) + str(coords[1]) + str(coords[2]),
                coords[0], coords[1], coords[2]
            )

        # Position objects
        for obj in self.objects:
            coords = obj.getCoordinates().get()
            self.matrix[coords[1]][coords[0]][coords[2]] = obj

        # Position Player
        self.positionPlayer()

    def setObjects(self, objects):
        self.objects = objects

    def addObject(self, obj):
        self.objects.append(obj)

    def positionPlayer(self):
        self.matrix[
            self.player.getCoordinates().getY()
        ][
            self.player.getCoordinates().getX()
        ][
            self.player.getCoordinates().getZ()
        ] = self.player

    def checkCollision(self):
        """
        Check if player is going to collide with something
        when moving to destination coordinates
        """
        coords = self.player.getCoordinates()
        obj = self.matrix[coords.getY()][coords.getX()][coords.getZ()]

        # If the object found is a collider, then there's a collision!
        return obj.isCollider, obj

from entities.base import Base
import game.constants
import copy


class Player(Base):

    """The player object manages the current player"""

    symbol = '@'
    decoraton = game.constants.STYLE_STANDOUT
    color = game.constants.COLOR_GK

    def __init__(self, uid, name, x=0, y=0, z=0):
        super(Player, self).__init__(uid, name, x, y, z)
        self.prevCoordinates = None
        self.collidedWalls = False

    def getCoordinates(self):
        """Returns the coordinates object with player position"""
        return self.coordinates

    def getPrevCoordinates(self):
        """Returns the coordinates object with player position"""
        return self.prevCoordinates

    def moveTo(self, coordinates):
        """Moves the player to new coordinates"""
        self.prevCoordinates = copy.deepcopy(self.coordinates)
        self.coordinates = copy.deepcopy(coordinates)

    def moveToTop(self):
        self.collidedWalls = False
        if self.coordinates.getY() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)
        else:
            self.collidedWalls = 'n'

    def moveToTopRight(self):
        self.collidedWalls = False
        if (self.coordinates.getY() - 1 >= 0 and
                self.coordinates.getX() + 1 < game.constants.MATRIX_W):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)
            self.coordinates.addX(1)
        else:
            self.collidedWalls = 'ne'

    def moveToRight(self):
        self.collidedWalls = False
        if self.coordinates.getX() + 1 < game.constants.MATRIX_W:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addX(1)
        else:
            self.collidedWalls = 'e'

    def moveToBottomRight(self):
        self.collidedWalls = False
        if (self.coordinates.getY() + 1 < game.constants.MATRIX_H and
                self.coordinates.getX() + 1 < game.constants.MATRIX_W):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)
            self.coordinates.addX(1)
        else:
            self.collidedWalls = 'se'

    def moveToBottom(self):
        self.collidedWalls = False
        if self.coordinates.getY() + 1 < game.constants.MATRIX_H:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)
        else:
            self.collidedWalls = 's'

    def moveToBottomLeft(self):
        self.collidedWalls = False
        if (self.coordinates.getY() + 1 < game.constants.MATRIX_H and
                self.coordinates.getX() - 1 >= 0):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)
            self.coordinates.addX(-1)
        else:
            self.collidedWalls = 'sw'

    def moveToLeft(self):
        self.collidedWalls = False
        if self.coordinates.getX() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addX(-1)
        else:
            self.collidedWalls = 'w'

    def moveToTopLeft(self):
        self.collidedWalls = False
        if (self.coordinates.getY() - 1 >= 0 and
                self.coordinates.getX() - 1 >= 0):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)
            self.coordinates.addX(-1)
        else:
            self.collidedWalls = 'nw'

    def moveUp(self):
        self.collidedWalls = False
        if self.coordinates.getZ() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addZ(-1)

    def moveDown(self):
        self.collidedWalls = False
        if self.coordinates.getZ() + 1 < game.constants.MATRIX_Z:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addZ(1)

    def revertPosition(self):
        if self.prevCoordinates:
            self.collidedWalls = False
            self.coordinates = copy.deepcopy(self.prevCoordinates)

    def hasCollidedWithWalls(self):
        return bool(self.collidedWalls)

    def getCollidedWall(self):
        return self.collidedWalls

    def getDirection(self):
        # Check which side of the object the player has collided with
        mx = self.coordinates.getX() - self.prevCoordinates.getX()
        my = self.coordinates.getY() - self.prevCoordinates.getY()
        mz = self.coordinates.getZ() - self.prevCoordinates.getZ()

        return (mx, my, mz)

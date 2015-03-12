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

    def getCoordinates(self):
        """Returns the coordinates object with player position"""
        return self.coordinates

    def moveTo(self, coordinates):
        """Moves the player to new coordinates"""
        self.prevCoordinates = copy.deepcopy(self.coordinates)
        self.coordinates = coordinates

    def moveToTop(self):
        if self.coordinates.getY() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)

    def moveToTopRight(self):
        if (self.coordinates.getY() - 1 >= 0 and
                self.coordinates.getX() + 1 < game.constants.MATRIX_W):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)
            self.coordinates.addX(1)

    def moveToRight(self):
        if self.coordinates.getX() + 1 < game.constants.MATRIX_W:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addX(1)

    def moveToBottomRight(self):
        if (self.coordinates.getY() + 1 < game.constants.MATRIX_H and
                self.coordinates.getX() + 1 < game.constants.MATRIX_W):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)
            self.coordinates.addX(1)

    def moveToBottom(self):
        if self.coordinates.getY() + 1 < game.constants.MATRIX_H:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)

    def moveToBottomLeft(self):
        if (self.coordinates.getY() + 1 < game.constants.MATRIX_H and
                self.coordinates.getX() - 1 >= 0):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(1)
            self.coordinates.addX(-1)

    def moveToLeft(self):
        if self.coordinates.getX() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addX(-1)

    def moveToTopLeft(self):
        if (self.coordinates.getY() - 1 >= 0 and
                self.coordinates.getX() - 1 >= 0):
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addY(-1)
            self.coordinates.addX(-1)

    def moveUp(self):
        if self.coordinates.getZ() - 1 >= 0:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addZ(-1)

    def moveDown(self):
        if self.coordinates.getZ() + 1 < game.constants.MATRIX_Z:
            self.prevCoordinates = copy.deepcopy(self.coordinates)
            self.coordinates.addZ(1)

    def revertPosition(self):
        if self.prevCoordinates:
            self.coordinates = copy.deepcopy(self.prevCoordinates)

from game.coordinates import Coordinates
import game.constants


class Player:

    """The player object manages the current player

    TODO: this should really inherit from the Base object
    """

    name = ''
    symbol = '@'
    # coordinates represents the player position in the universe
    coordinates = Coordinates(0, 0, 0)

    @staticmethod
    def setName(name):
        Player.name = name

    @staticmethod
    def getName():
        return Player.name

    @staticmethod
    def getCoordinates():
        """Returns the coordinates object with player position"""
        return Player.coordinates

    @staticmethod
    def moveTo(coordinates):
        """Moves the player to new coordinates"""
        Player.coordinates = coordinates

    @staticmethod
    def moveToTop():
        if Player.coordinates.getY() - 1 >= 0:
            Player.coordinates.addY(-1)

    @staticmethod
    def moveToTopRight():
        if (Player.coordinates.getY() - 1 >= 0 and
                Player.coordinates.getX() + 1 < game.constants.MATRIX_W):
            Player.coordinates.addY(-1)
            Player.coordinates.addX(1)

    @staticmethod
    def moveToRight():
        if Player.coordinates.getX() + 1 < game.constants.MATRIX_W:
            Player.coordinates.addX(1)

    @staticmethod
    def moveToBottomRight():
        if (Player.coordinates.getY() + 1 < game.constants.MATRIX_H and
                Player.coordinates.getX() + 1 < game.constants.MATRIX_W):
            Player.coordinates.addY(1)
            Player.coordinates.addX(1)

    @staticmethod
    def moveToBottom():
        if Player.coordinates.getY() + 1 < game.constants.MATRIX_H:
            Player.coordinates.addY(1)

    @staticmethod
    def moveToBottomLeft():
        if (Player.coordinates.getY() + 1 < game.constants.MATRIX_H and
                Player.coordinates.getX() - 1 >= 0):
            Player.coordinates.addY(1)
            Player.coordinates.addX(-1)

    @staticmethod
    def moveToLeft():
        if Player.coordinates.getX() - 1 >= 0:
            Player.coordinates.addX(-1)

    @staticmethod
    def moveToTopLeft():
        if (Player.coordinates.getY() - 1 >= 0 and
                Player.coordinates.getX() - 1 >= 0):
            Player.coordinates.addY(-1)
            Player.coordinates.addX(-1)

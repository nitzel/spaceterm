import game.constants
from entities.player import Player
from entities.solarsystem import SolarSystem
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix
from game.genesis import Genesis
from game.coordinates import Coordinates
from libs import unicurses
import math


class Game:

    """The game controller"""

    def __init__(self, screen):
        super(Game, self).__init__()
        self.renderer = None
        self.inputProcessor = None
        self.gameMatrix = None
        self.screen = screen
        self.runGame = True
        self.player = None
        self.view = 0  # 0 = galaxy, 1 = sector, 2 = solar system
        self.currentSector = None
        self.currentSolarSystem = None
        self.playerHasCollided = False
        self.collisionObj = None
        # Tuple holding difference between player coords and prevCoords
        self.playerDirection = (0, 0, 0)

    def initialize(self, playerName):
        # Initialize Player
        self.player = Player('1UP', playerName, 0, 0, 0)

        # Initialize I/O
        self.renderer = Renderer(self.screen)
        self.inputProcessor = Input()
        self.gameMatrix = Matrix(
            game.constants.MATRIX_W,
            game.constants.MATRIX_H,
            game.constants.MATRIX_Z,
            self.player
        )
        self.renderer.clearScreen()

        # Bind keys to actions
        self.inputProcessor.onKey('q', self.quit)
        self.inputProcessor.onKeys(['h', unicurses.KEY_LEFT],
                                   self.player.moveToLeft)
        self.inputProcessor.onKeys(['k', unicurses.KEY_UP],
                                   self.player.moveToTop)
        self.inputProcessor.onKeys(['j', unicurses.KEY_DOWN],
                                   self.player.moveToBottom)
        self.inputProcessor.onKeys(['l', unicurses.KEY_RIGHT],
                                   self.player.moveToRight)
        self.inputProcessor.onKeys(['y', unicurses.KEY_A1],
                                   self.player.moveToTopLeft)
        self.inputProcessor.onKeys(['u', unicurses.KEY_A3],
                                   self.player.moveToTopRight)
        self.inputProcessor.onKeys(['b', unicurses.KEY_C1],
                                   self.player.moveToBottomLeft)
        self.inputProcessor.onKeys(['n', unicurses.KEY_C3],
                                   self.player.moveToBottomRight)
        self.inputProcessor.onKeys(['>'],
                                   self.player.moveDown)
        self.inputProcessor.onKeys(['<'],
                                   self.player.moveUp)
        self.inputProcessor.onKeys(['.', unicurses.KEY_B2], self.skipTurn)

        # Initialize the universe!
        genesis = Genesis(1)
        genesis.generate()

        # Get sector 0 as the one the players starts in
        self.currentSector = genesis.getSector(0)

        # Start in sector view
        self.switchToSectorView()

        # Initialize status message
        self.renderer.setStatusMsg('Welcome to SpaceTerm!')

    def loop(self):
        while (self.runGame):
            self.gameMatrix.updateLevel()
            self.renderer.setStatusMsg(self.makeStatusText())
            self.renderer.render(self.gameMatrix)
            self.inputProcessor.getPlayerInput(self.screen)
            self.playerHasCollided, self.collisionObj = \
                self.gameMatrix.checkCollision()
            self.playerDirection = self.player.getDirection()

            if self.playerHasCollided:
                self.player.revertPosition()
                self.collisionAction()

            if self.player.hasCollidedWithWalls():
                # If player is in solar system, switch to sector
                if self.view == 2:
                    self.switchToSectorView()

    def collisionAction(self):
        if isinstance(self.collisionObj, SolarSystem):
            self.switchToSolarSystemView(self.collisionObj)

    def quit(self):
        """Quits the game"""
        self.runGame = False

        # Some cleanup before exiting..
        self.renderer.clearScreen()

    def skipTurn(self):
        """Skips player turn"""
        pass

    def makeStatusText(self):
        """Builds the status text to display to the user"""
        statusText = 'CMDR ' + self.player.getName()
        statusText += ' / '
        statusText += '[%s,%s,%s]' % self.player.getCoordinates().get()
        statusText += '\n'
        statusText += 'Fuel: [##########] 100%'

        if self.playerDirection:
            statusText += ' / '
            statusText += 'Direction: ' + str(self.playerDirection)

        return statusText

    def __switchView(self, view):
        """
        Switch to the specified view.
        This is a low level method and shouldn't be used directly.
        Instead use switchToGalaxyView(), switchToSectorView() or
        switchToSolarSystemView()
        """
        if (view not in [0, 1, 2]):
            raise RuntimeError
        self.view = view

    def switchToGalaxyView(self):
        self.__switchView(0)

    def switchToSectorView(self):
        self.__switchView(1)

        # If player was in solar system, we move him to ss coords
        # modified based on exit point.
        if self.currentSolarSystem:
            wall = self.player.getCollidedWall()
            self.player.moveTo(self.currentSolarSystem.getCoordinates())

            if wall == 'n':
                self.player.moveToTop()
            elif wall == 'ne':
                self.player.moveToTopRight()
            elif wall == 'e':
                self.player.moveToRight()
            elif wall == 'se':
                self.player.moveToBottomRight()
            elif wall == 's':
                self.player.moveToBottom()
            elif wall == 'sw':
                self.player.moveToBottomLeft()
            elif wall == 'w':
                self.player.moveToLeft()
            elif wall == 'nw':
                self.player.moveToTopLeft()

        objects = self.currentSector.getObjects()

        # Add current sector objects (solar systems) to the game matrix
        self.gameMatrix.setObjects(objects)
        self.currentSolarSystem = None

    def switchToSolarSystemView(self, ss):
        self.__switchView(2)

        objects = ss.getObjects()

        # Check where player has collided with solar system to set initial pos
        newCoords = Coordinates(0, 0, 0)
        if self.playerDirection[0] == 1:  # Collided west
            if self.playerDirection[1] == 1:  # Collided north west
                newCoords.set(0, 0, 0)
            elif self.playerDirection[1] == -1:  # Collided south west
                newCoords.set(0, game.constants.SS_H - 1, 0)
            else:  # Collided west
                newCoords.set(0, math.floor((game.constants.SS_H - 1) / 2), 0)
        elif self.playerDirection[0] == -1:
            if self.playerDirection[1] == 1:  # Collided north east
                newCoords.set(game.constants.SS_W - 1, 0, 0)
            elif self.playerDirection[1] == -1:  # Collided south east
                newCoords.set(game.constants.SS_W - 1,
                              game.constants.SS_H - 1, 0)
            else:  # Collided east
                newCoords.set(game.constants.SS_W - 1,
                              math.floor((game.constants.SS_H - 1) / 2), 0)
        elif self.playerDirection[1] == 1:  # Collided north
            newCoords.set(math.floor((game.constants.SS_W - 1) / 2), 0, 0)
        elif self.playerDirection[1] == -1:  # Collided south
            newCoords.set(math.floor((game.constants.SS_W - 1) / 2),
                          game.constants.SS_H - 1, 0)
        else:  # Collided top or bottom (TODO)
            newCoords.set(10, 10, 10)  # Temporary just to spot the case

        self.player.moveTo(newCoords)

        # Add current solar sytem objects (stars, planets..) to the game matrix
        self.gameMatrix.setObjects(objects)
        self.currentSolarSystem = ss

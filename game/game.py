import game.constants
from entities.player import Player
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix
from game.genesis import Genesis
import curses


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
        self.inputProcessor.onKeys(['h', curses.KEY_LEFT],
                                   self.player.moveToLeft)
        self.inputProcessor.onKeys(['k', curses.KEY_UP],
                                   self.player.moveToTop)
        self.inputProcessor.onKeys(['j', curses.KEY_DOWN],
                                   self.player.moveToBottom)
        self.inputProcessor.onKeys(['l', curses.KEY_RIGHT],
                                   self.player.moveToRight)
        self.inputProcessor.onKeys(['y', curses.KEY_A1],
                                   self.player.moveToTopLeft)
        self.inputProcessor.onKeys(['u', curses.KEY_A3],
                                   self.player.moveToTopRight)
        self.inputProcessor.onKeys(['b', curses.KEY_C1],
                                   self.player.moveToBottomLeft)
        self.inputProcessor.onKeys(['n', curses.KEY_C3],
                                   self.player.moveToBottomRight)
        self.inputProcessor.onKeys(['>'],
                                   self.player.moveDown)
        self.inputProcessor.onKeys(['<'],
                                   self.player.moveUp)
        self.inputProcessor.onKeys(['.', curses.KEY_B2], self.skipTurn)

        # Initialize the universe!
        genesis = Genesis(1)
        genesis.generate()

        # Get sector 0 as the one the players starts in
        sector = genesis.getSector(0)
        objects = sector.getObjects()

        # Add its objects (stars, planets, etc) to the game matrix
        self.gameMatrix.setObjects(objects)

        # Initialize status message
        self.renderer.setStatusMsg('Welcome to SpaceTerm!')

    def loop(self):
        while (self.runGame):
            self.gameMatrix.updateLevel()
            self.renderer.setStatusMsg(self.makeStatusText())
            self.renderer.render(self.gameMatrix)
            self.inputProcessor.getPlayerInput(self.screen)

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

        return statusText

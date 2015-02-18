from entities.player import Player
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix
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

    def initialize(self, playerName):
        # Initialize Player
        Player.setName(playerName)

        # Initialize I/O
        self.renderer = Renderer(self.screen)
        self.inputProcessor = Input()
        self.gameMatrix = Matrix(80, 24, 10)
        self.renderer.clearScreen()

        # Bind keys to actions
        self.inputProcessor.onKey('q', self.quit)
        self.inputProcessor.onKeys(['h', curses.KEY_LEFT], Player.moveToLeft)
        self.inputProcessor.onKeys(['k', curses.KEY_UP], Player.moveToTop)
        self.inputProcessor.onKeys(['j', curses.KEY_DOWN], Player.moveToBottom)
        self.inputProcessor.onKeys(['l', curses.KEY_RIGHT], Player.moveToRight)
        self.inputProcessor.onKeys(['y', curses.KEY_A1], Player.moveToTopLeft)
        self.inputProcessor.onKeys(['u', curses.KEY_A3], Player.moveToTopRight)
        self.inputProcessor.onKeys(['b', curses.KEY_C1], Player.moveToBottomLeft)
        self.inputProcessor.onKeys(['n', curses.KEY_C3], Player.moveToBottomRight)
        self.inputProcessor.onKeys(['.', curses.KEY_B2], self.skipTurn)

        # Initialize curses screen
        self.screen.border(0, 0, 0, 0, 0, 0, 0, 0)

    def loop(self):
        self.gameMatrix.updateLevel()
        self.gameMatrix.positionPlayer()
        self.renderer.render(self.gameMatrix)

        while (self.runGame):
            self.inputProcessor.getPlayerInput(self.screen)
            self.gameMatrix.updateLevel()
            self.gameMatrix.positionPlayer()
            self.renderer.render(self.gameMatrix)

    def quit(self):
        """Quits the game"""
        self.runGame = False

        # Some cleanup before exiting..
        self.renderer.clearScreen()

    def skipTurn(self):
        """Skips player turn"""
        pass

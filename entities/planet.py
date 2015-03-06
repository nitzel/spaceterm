from entities.base import Base
import game.constants


class Planet(Base):

    """The Planet objects represent a planet"""

    symbol = 'o'
    decoration = game.constants.STYLE_BOLD
    color = game.constants.COLOR_BK  # TODO Change based on planet class

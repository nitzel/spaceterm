from entities.base import Base
import game.constants


class Space(Base):

    """Empty space object"""

    symbol = ' '
    style = game.constants.STYLE_NORMAL

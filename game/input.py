from libs import unicurses
class Input:

    """Manages player input"""

    def __init__(self):
        super(Input, self).__init__()
        self.callbacks = {}

    def getPlayerInput(self, screen):
        """Standardized method to get player input"""
        ch = unicurses.wgetch(screen)
        self.runCallbacks(ch)
        return ch

    def onKey(self, ch, callback):
        """Binds a callback to a keypress"""
        if ch not in self.callbacks:
            self.callbacks[ch] = []

        self.callbacks[ch].append(callback)

    def onKeys(self, chs, callback):
        """Wrapper on onKey to add multiple bindings in one call"""
        for ch in chs:
            self.onKey(ch, callback)

    def runCallbacks(self, ch):
        """Run callback functions after a key is pressed"""
        if ch in self.callbacks:
            for callback in self.callbacks[ch]:
                callback()

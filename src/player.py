import curses

collideables = ('#',)

class Player(object):

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

    def move(self, dy, dx):
        y = self.y + dy
        x = self.x + dx
        if self.win.inch(y, x) not in collideables:
            self.win.delch(self.y, self.x)
            self.y = y
            self.x = x

    def render(self):
        self.win.addstr(self.y, self.x, '@', curses.color_pair(1))

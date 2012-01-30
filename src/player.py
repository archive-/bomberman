import sys
import curses
import time
from entity import Entity
from bomb import Bomb

class Player(Entity):

    def __init__(self, level, y, x):
        Entity.__init__(self, level, y, x)
        self.num_bombs = 1

    def drop_bomb(self):
        # TODO at tick, get bomb or w/e
        if self.num_bombs > 0:
            Bomb(self)
            self.num_bombs -= 1

    def update(self):
        fire_time = self.level.fires[self.y][self.x]
        if fire_time and time.time() - fire_time <= 0.4:
            self.die()

    def move(self, dy, dx, win):
        y = self.y + dy
        x = self.x + dx
        if y >= len(self.level.tiles) or x >= len(self.level.tiles[0]):
            return
        if not self.level.collision(y, x):
            # TODO why do we need this to be here....
            win.stdscr.delch(self.y, self.x)
            self.y = y
            self.x = x

    def die(self):
        # TODO
        sys.exit(0)

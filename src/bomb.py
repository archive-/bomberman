import time
from entity import Entity

NUM_TICKS = 2

class Bomb(Entity):

    def __init__(self, player):
        Entity.__init__(self, player.level, player.y, player.x)
        self.player = player
        self.num_ticks = NUM_TICKS
        self.curr_tick = NUM_TICKS
        self.radius = 3
        self.created_at = time.time()

    def update(self):
        self.curr_tick = self.num_ticks - int(time.time()-self.created_at)
        if self.curr_tick == 0:
            self.explode()
        else:
            self.curr_tick -= 1

    def explode(self):
        self.level.fires = map(lambda x: False, self.level.tiles)
        # TODO
        self.level.remove(self)
        self.player.num_bombs += 1

import time
from entity import Entity

NUM_TICKS = 2.5

class Bomb(Entity):

    def __init__(self, player):
        Entity.__init__(self, player.level, player.y, player.x)
        self.player = player
        self.num_ticks = NUM_TICKS
        self.curr_tick = NUM_TICKS
        self.radius = 3
        self.created_at = time.time()

    def update(self):
        self.curr_tick = int(self.num_ticks-(time.time()-self.created_at))
        if self.curr_tick == 0:
            self.explode()
        else:
            self.curr_tick -= 1

    def explode(self):
        self.level.fires[self.y][self.x] = time.time()
        def expand(fy, fx):
            for i in xrange(self.radius):
                # TODO make this collision have side effects (ie. beak wall, kill player, etc.)
                if self.level.collision(self.y+fy*i, self.x+fx*i, fire=True):
                    return
                else:
                    self.level.fires[self.y+fy*i][self.x+fx*i] = time.time()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.level.remove(self)
        [expand(*direction) for direction in directions]
        self.player.num_bombs += 1

import os
import settings
from player import Player

collideables = ('#', '%')

class Level(set):

    def __init__(self, name):
        set.__init__(self)
        self.name = name
        self.build_from_file(name)
        self.fires = []
        for tiles in self.tiles:
            self.fires.append(map(lambda x: None, tiles))

    def build_from_file(self, name):
        f = open(os.path.join(settings.LEVEL_DIR, name + settings.LEVEL_EXT))
        self.tiles = map(lambda x: list(x), f.read().split('\n'))

    def collision(self, y, x, fire=False):
        # ecoll = any([type(entity) != Player and entity.y == y and entity.x == x for entity in self])
        if self.tiles[y][x] in collideables:
            if fire and self.tiles[y][x] == '%':
                self.tiles[y][x] = ' '
            return True
        for entity in self:
            if type(entity) != Player and entity.y == y and entity.x == x:
                entity.collided()
                return True
        return False

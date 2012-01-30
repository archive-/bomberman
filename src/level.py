import os
import settings

collideables = ('#', '%')

class Level(set):

    def __init__(self, name):
        set.__init__(self)
        self.name = name
        self.build_from_file(name)

    def build_from_file(self, name):
        f = open(os.path.join(settings.LEVEL_DIR, name + settings.LEVEL_EXT))
        self.tiles = f.read().split('\n')

    def collision(self, y, x):
        tcoll = self.tiles[y][x] in collideables
        ecoll = any([entity.y == y and entity.x == x for entity in self])
        return tcoll or ecoll

class Entity(object):

    def __init__(self, level, y, x):
        self.level = level
        self.y = y
        self.x = x
        self.level.add(self)

    def update(self):
        pass

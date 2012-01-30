#!/usr/bin/env python2.7

from windows.curses_window import CursesWindow
from player import Player
from level import Level

class Client(object):

    IN_GAME = 0

    def __init__(self):
        CursesWindow(self) # sets self.win

    def run(self):
        self.level = Level('1')
        self.player = Player(self.level, 3, 3)
        self.running = True
        while self.running:
            self.win.handle_events(self.player)
            self.win.render()
            for entity in self.level.copy():
                entity.update()

if __name__ == '__main__':
    client = Client()

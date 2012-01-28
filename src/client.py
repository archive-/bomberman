#!/usr/bin/env python2.7

import curses
from player import Player

class Client(object):

    IN_GAME = 0

    def __init__(self):
        self.window = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.noecho() # don't auto echo keys
        curses.cbreak() # instant buffer mode
        self.window.keypad(1) # return curse key enums
        curses.curs_set(0) # hides blinking cursor
        self.window.nodelay(1) # makes getch return -1 for no input
        # TODO: build map!!!  self.
        self.player = Player(self.window, 0, 0)
        self.run()

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.render()
            self.window.refresh()
        self.terminate()

    def handle_events(self):
        ch = self.window.getch()
        if ch == curses.KEY_F1:
            self.running = False
        elif ch == curses.KEY_F2:
            self.state = IN_GAME
        elif ch == curses.KEY_UP:
            self.player.move(-1, 0)
        elif ch == curses.KEY_RIGHT:
            self.player.move(0, 1)
        elif ch == curses.KEY_DOWN:
            self.player.move(1, 0)
        elif ch == curses.KEY_LEFT:
            self.player.move(0, -1)

    def render(self):
        self.player.render()

    def terminate(self):
        curses.nocbreak()
        self.window.keypad(0)
        curses.echo()
        curses.endwin()
        self.window = None

if __name__ == '__main__':
    client = Client()

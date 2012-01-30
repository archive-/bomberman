import curses
import time
from bomb import Bomb

class CursesWindow(object):

    def __init__(self, client):
        self.client = client
        self.client.win = self
        curses.wrapper(self.wrapped) # calls noecho, cbreak, etc. + signals

    def wrapped(self, stdscr):
        self.stdscr = stdscr
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.curs_set(0) # hides blinking cursor
        self.stdscr.nodelay(1) # makes getch return -1 for no input
        self.client.run()

    def render(self):
        render_time = time.time()
        stdadd = self.stdscr.addch
        for y, tiles in enumerate(self.client.level.tiles):
            for x, tile in enumerate(tiles):
                stdadd(2*y, 4*x, tile, curses.color_pair(1))
                stdadd(2*y+1, 4*x, tile, curses.color_pair(1))
                stdadd(2*y, 4*x+1, tile, curses.color_pair(1))
                stdadd(2*y+1, 4*x+1, tile, curses.color_pair(1))
                # fix aspect ratio
                stdadd(2*y, 4*x+2, tile, curses.color_pair(1))
                stdadd(2*y+1, 4*x+2, tile, curses.color_pair(1))
                stdadd(2*y, 4*x+3, tile, curses.color_pair(1))
                stdadd(2*y+1, 4*x+3, tile, curses.color_pair(1))
        stdadd(2*self.client.player.y, 4*self.client.player.x, '[', curses.color_pair(1))
        stdadd(2*self.client.player.y+1, 4*self.client.player.x, ' ', curses.color_pair(1))
        stdadd(2*self.client.player.y, 4*self.client.player.x+1, '^', curses.color_pair(1))
        stdadd(2*self.client.player.y+1, 4*self.client.player.x+1, ']', curses.color_pair(1))
        # fix aspect ratio
        stdadd(2*self.client.player.y, 4*self.client.player.x+2, '^', curses.color_pair(1))
        stdadd(2*self.client.player.y+1, 4*self.client.player.x+2, '[', curses.color_pair(1))
        stdadd(2*self.client.player.y, 4*self.client.player.x+3, ']', curses.color_pair(1))
        stdadd(2*self.client.player.y+1, 4*self.client.player.x+3, ' ', curses.color_pair(1))
        # print all other entities
        for entity in self.client.level:
            if type(entity) == Bomb:
                stdadd(2*entity.y,   4*entity.x,   '[', curses.color_pair(1))
                stdadd(2*entity.y+1, 4*entity.x,   '[', curses.color_pair(1))
                stdadd(2*entity.y,   4*entity.x+1, str(int(entity.curr_tick%10)), curses.color_pair(1))
                stdadd(2*entity.y+1, 4*entity.x+1, str(int(entity.curr_tick%10)), curses.color_pair(1))
                stdadd(2*entity.y,   4*entity.x+2, str(int(entity.curr_tick%10)), curses.color_pair(1))
                stdadd(2*entity.y+1, 4*entity.x+2, str(int(entity.curr_tick%10)), curses.color_pair(1))
                stdadd(2*entity.y,   4*entity.x+3, ']', curses.color_pair(1))
                stdadd(2*entity.y+1, 4*entity.x+3, ']', curses.color_pair(1))
        for y, fire_times in enumerate(self.client.level.fires):
            for x, fire_time in enumerate(fire_times):
                if fire_time is not None and render_time - fire_time < 0.4:
                    fire_sign = '^'
                    stdadd(2*y, 4*x, fire_sign, curses.color_pair(1))
                    stdadd(2*y+1, 4*x, fire_sign, curses.color_pair(1))
                    stdadd(2*y, 4*x+1, fire_sign, curses.color_pair(1))
                    stdadd(2*y+1, 4*x+1, fire_sign, curses.color_pair(1))
                    # fix aspect ratio
                    stdadd(2*y, 4*x+2, fire_sign, curses.color_pair(1))
                    stdadd(2*y+1, 4*x+2, fire_sign, curses.color_pair(1))
                    stdadd(2*y, 4*x+3, fire_sign, curses.color_pair(1))
                    stdadd(2*y+1, 4*x+3, fire_sign, curses.color_pair(1))
        # draw
        self.stdscr.refresh()

    def handle_events(self, player):
        ch = self.stdscr.getch()
        if ch == curses.KEY_F1:
            self.client.running = False
        elif ch == curses.KEY_F2:
            self.client.player.drop_bomb()
        elif ch == curses.KEY_UP:
            self.client.player.move(-1, 0, self)
        elif ch == curses.KEY_RIGHT:
            self.client.player.move(0, 1, self)
        elif ch == curses.KEY_DOWN:
            self.client.player.move(1, 0, self)
        elif ch == curses.KEY_LEFT:
            self.client.player.move(0, -1, self)

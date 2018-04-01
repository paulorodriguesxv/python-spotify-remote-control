import curses
import curses.panel

from .alignment import Alignment
from .panel import Panel

NEW_LINE = 10
CARRIAGE_RETURN = 13


class ErrorPanel(Panel):
    def __init__(self, title, error_text, dimensions):
        super().__init__(title, dimensions)
        self._error_text = error_text

    def update(self):
        pos_x = 2
        pos_y = 2

        self._win.addstr(
                pos_y,
                pos_x,
                self._error_text,
                curses.A_NORMAL)

        self._win.addstr(
                pos_y+10,
                pos_x,
                '<< PRESS ENTER >>',
                curses.A_NORMAL)

        self._win.refresh()




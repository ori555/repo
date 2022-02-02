
from screen_classes.ScreenObject import *


class ClickableObject(ScreenObject):
    def __init__(self, screen, x_pos, y_pos, width, height):
        super(ClickableObject, self).__init__(screen, x_pos, y_pos, width, height)

    def mouse_in_button(self, mouse_pos):
        """
        The function return True if the button was clicked. otherwise, False will be returned.
        :param mouse_pos: The position of the mouse click.
        :return: None
        """
        if ((self._x_pos <= mouse_pos[0] <= self._x_pos + self._width) and
                (self._y_pos <= mouse_pos[1] <= self._y_pos + self._height)):
            return True
        else:
            return False

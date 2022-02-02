from screen_classes.ClickableObject import *
from screen_classes.Image import *


class ImageButton(ClickableObject, Image):
    def __init__(self, screen, x_pos, y_pos, width, height, img_path):
        Image.__init__(self, screen, x_pos, y_pos, width, height, img_path)

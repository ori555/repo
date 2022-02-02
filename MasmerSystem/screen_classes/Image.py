import pygame
from screen_classes.ScreenObject import *
# from pathlib import Path


class Image(ScreenObject):
    def __init__(self, screen, x_pos, y_pos, width, height, img_path):
        super().__init__(screen, x_pos, y_pos, width, height)
        self._img_path = img_path

    def add_image_to_screen(self):
        """
        Add the image of the given size to the screen in the desired location.
        :return: None
        """
        # Add the image to the screen
        img = pygame.image.load(self._img_path)
        img = pygame.transform.scale(img, (self._width, self._height))
        self._screen.blit(img, (self._x_pos, self._y_pos))

        # Update the screen
        pygame.display.flip()

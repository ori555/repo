from screen_classes.ClickableObject import *
import pygame
from constants import *


class Textbox(ClickableObject):
    def __init__(self, screen, x_pos, y_pos, width, height, amount_of_lines=1, is_secret=False):
        """
        :param screen:
            The pygame screen.
        :param x_pos:
            The X position of the object.
        :param y_pos:
            The Y position of the object.
        :param width:
            The width of the object.
        :param height:
            The height of the object.
        :param
            amount_of_lines: The max amount of lines that this object can contain.
        :param is_secret:
            If this variable is True it means that the text can't be presented as it is. it must be writen as ****.
        """
        super().__init__(screen, x_pos, y_pos, width, height)
        self.__typing_status = False
        self.__text = ""
        self.__amount_of_lines = amount_of_lines
        self.__is_secret = is_secret

    def add_textbox_to_screen(self):
        """
        Add the given text in the given size to the screen in the
           desired location.
        :return: None
        """
        """
        # Just for debug
        color = (200, 200, 200)

        # Drawing Rectangle
        pygame.draw.rect(self._screen, color, pygame.Rect(self._x_pos, self._y_pos, self._width, self._height))
        """
        font = pygame.font.SysFont('Arial', TEXTBOX_TEXT_SIZE)
        if self.__is_secret:
            secret_text = len(self.__text) * "*"
            self._screen.blit(font.render(secret_text, True, BLACK), (self._x_pos, self._y_pos))
        else:
            if self.__amount_of_lines == 1:
                self._screen.blit(font.render(self.__text, True, BLACK), (self._x_pos, self._y_pos))
            else:
                for line in range(self.__amount_of_lines):
                    part = self.__text[line * DESCRIPTION_MAX_LENGTH_IN_LINE:
                                       (line + 1) * DESCRIPTION_MAX_LENGTH_IN_LINE]
                    self._screen.blit(font.render(part, True, BLACK),
                                      (self._x_pos, self._y_pos + ADD_NEW_TASK_TEXTBOX_HEIGHT * line))

        pygame.display.flip()

    def enable_typing(self):
        self.__typing_status = True

    def disable_typing(self):
        self.__typing_status = False

    def add_letter(self, letter):
        if self.__amount_of_lines == 1:
            if len(self.__text) < TEXT_MAX_LENGTH:
                self.__text += letter
        else:
            if len(self.__text) < DESCRIPTION_MAX_LINES * DESCRIPTION_MAX_LENGTH_IN_LINE:
                self.__text += letter

    def delete_letter(self):
        if self.__text != "":
            self.__text = self.__text[0:len(self.__text) - 1]

    def get_typing_status(self):
        return self.__typing_status

    def get_text(self):
        return self.__text

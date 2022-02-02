import time
import pygame
# from constants import *
import Database
from screen_classes.Textbox import *
from screen_classes.ImageButton import *
from screen_classes.Login import *
from employee_classes.Employee import *


class App:
    def __init__(self, screen):
        self.__screen = screen
        self.__background = None
        self.__curr_screen = "login"
        self.__object_dict = {}
        self.__employee = None
        self.__list_of_tasks = []
        self.__list_of_employees_id = []
        self.__start_display()

    def __start_display(self):
        """
        The function displays the first two screens on the screen - the loading screen and the login screen.
        :return: None
        """
        self.__display_loading_screen()
        self.__display_login_screen()

        # For lesson 14 - Cancel the remarks of the next lines
        """
        self.__curr_screen = "task_manager"
        self.__employee = Employee("rony", "cohen", "225682158", "rc22", "ym34", "e")
        self.__display_task_manager_screen()
        """

    def __set_background_image(self):
        """
        Add the image of the given size to the screen in the desired location.
        :return: None
        """
        # Add the image to the screen
        img = pygame.image.load(self.__background)
        # img = pygame.transform.scale(img, pygame.display.get_surface().get_size())  # Full screen run
        img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__screen.blit(img, (0, 0))

        # Update the screen
        pygame.display.flip()

    def __display_loading_screen(self):
        """
        Displays the loading screen (the function will wait 3 seconds).
        The current screen name will change to a loading details screen.
        :return: None
        """
        for image_number in range(AMOUNT_OF_LOADING_SCREENS):
            self.__background = LOADING_SCREEN_IMAGE_PATH + str(
                image_number + 1) + LOADING_SCREEN_PATH_EXTENSION
            self.__set_background_image()
            time.sleep(0.2)
        time.sleep(0.3)
        pygame.display.flip()

    def __display_login_screen(self):
        """
        Displays the login screen (creating the buttons, text boxes and background).
        The current screen name will change to the login screen.
        :return: None
        """
        self.__background = LOGIN_BACKGROUND_IMAGE
        self.__set_background_image()

        # If the dict is empty add the buttons
        if not self.__object_dict:
            self.__object_dict["username_textbox"] = Textbox(self.__screen,
                                                             SIGN_IN_TEXTBOX_X_POS,
                                                             USERNAME_TEXTBOX_Y_POS,
                                                             SIGN_IN_TEXTBOX_WIDTH,
                                                             SIGN_IN_TEXTBOX_HEIGHT)
            self.__object_dict["password_textbox"] = Textbox(self.__screen,
                                                             SIGN_IN_TEXTBOX_X_POS,
                                                             PASSWORD_TEXTBOX_Y_POS,
                                                             SIGN_IN_TEXTBOX_WIDTH,
                                                             SIGN_IN_TEXTBOX_HEIGHT,
                                                             is_secret=True)
            self.__object_dict["login_btn"] = ImageButton(self.__screen,
                                                          LOGIN_BTN_X_POS,
                                                          LOGIN_BTN_Y_POS,
                                                          LOGIN_BTN_WIDTH,
                                                          LOGIN_BTN_HEIGHT,
                                                          LOGIN_BTN_IMAGE)
        self.__add_objects_to_screen()

    def __display_task_manager_screen(self):
        """
        Displays the task management screen (creating the buttons, text boxes and background).
        The current screen name will change to the Task Manager screen.
        :return: None
        """
        self.__background = TASK_MANAGER_BACKGROUND_IMAGE
        self.__set_background_image()

        # Remove the old text boxes and buttons
        self.__update_dict("task_manager")

        # role = self.__employee.get_role()

        # If the dict is empty add the buttons
        if not self.__object_dict:
            if isinstance(self.__employee, Manager):
                # Only for managers
                self.__object_dict["add_new_task_btn"] = ImageButton(
                    self.__screen, ADD_NEW_TASK_BTN_X_POS,
                    ADD_NEW_TASK_BTN_Y_POS,
                    ADD_NEW_TASK_BTN_WIDTH,
                    ADD_NEW_TASK_BTN_HEIGHT,
                    ADD_NEW_TASK_BTN_IMAGE)
                self.__object_dict["delete_task_btn"] = ImageButton(
                    self.__screen, DELETE_TASK_BTN_X_POS,
                    DELETE_TASK_BTN_Y_POS,
                    DELETE_TASK_BTN_WIDTH,
                    DELETE_TASK_BTN_HEIGHT,
                    DELETE_TASK_BTN_IMAGE)
                if isinstance(self.__employee, Head):
                    # Only for the head of the Mossad
                    self.__object_dict["add_new_employee_btn"] = ImageButton(
                        self.__screen, ADD_NEW_EMPLOYEE_BTN_X_POS,
                        ADD_NEW_EMPLOYEE_BTN_Y_POS,
                        ADD_NEW_EMPLOYEE_BTN_WIDTH,
                        ADD_NEW_EMPLOYEE_BTN_HEIGHT,
                        ADD_NEW_EMPLOYEE_BTN_IMAGE)
            # For everyone
            self.__object_dict["complete_task_btn"] = ImageButton(self.__screen,
                                                                  COMPLETE_TASK_BTN_X_POS,
                                                                  COMPLETE_TASK_BTN_Y_POS,
                                                                  COMPLETE_TASK_BTN_WIDTH,
                                                                  COMPLETE_TASK_BTN_HEIGHT,
                                                                  COMPLETE_TASK_BTN_IMAGE)
            self.__create_logo()

        self.__add_objects_to_screen()
        self.__add_employee_details_to_task_screen()
        self.__add_tasks_details_to_task_screen()

    def __display_complete_task_screen(self):
        """
        Displays the task completion screen (creating the buttons, text boxes and background).
        The current screen name will change to the task completion screen.
        :return: None
        """
        self.__background = COMPLETE_TASK_SCREEN_BACKGROUND_IMAGE
        self.__set_background_image()

        # Remove the old text boxes and buttons
        self.__update_dict("complete_task")

        # If the dict is empty add the buttons
        if not self.__object_dict:
            self.__object_dict["complete_btn"] = ImageButton(self.__screen,
                                                             COMPLETE_BTN_X_POS,
                                                             COMPLETE_BTN_Y_POS,
                                                             COMPLETE_BTN_WIDTH,
                                                             COMPLETE_BTN_HEIGHT,
                                                             COMPLETE_BTN_IMAGE)
            self.__create_back_button()
            self.__create_logo()

            self.__object_dict["task_id_textbox"] = Textbox(self.__screen,
                                                            COMPLETE_TASK_TEXTBOX_X_POS,
                                                            COMPLETE_TASK_TASK_ID_TEXTBOX_Y_POS,
                                                            COMPLETE_TASK_TEXTBOX_WIDTH,
                                                            COMPLETE_TASK_TEXTBOX_HEIGHT)
            self.__object_dict["security_key_textbox"] = Textbox(self.__screen,
                                                                 COMPLETE_TASK_TEXTBOX_X_POS,
                                                                 COMPLETE_TASK_SECURITY_KEY_TEXTBOX_Y_POS,
                                                                 COMPLETE_TASK_TEXTBOX_WIDTH,
                                                                 COMPLETE_TASK_TEXTBOX_HEIGHT)

        self.__add_objects_to_screen()

    def __display_add_new_task_screen(self):
        """
        Displays the "Add New Task" screen (creating buttons, text boxes and background).
        The current screen name will change to the Add New Task screen.
        :return: None
        """
        self.__background = ADD_NEW_TASK_SCREEN_BACKGROUND_IMAGE
        self.__set_background_image()

        # Remove the old text boxes and buttons
        self.__update_dict("add_new_task")

        # If the dict is empty add the buttons
        if not self.__object_dict:
            self.__object_dict["add_new_task_btn"] = ImageButton(self.__screen,
                                                                 ADD_NEW_TASK_IN_ADD_SCREEN_BTN_X_POS,
                                                                 ADD_NEW_TASK_IN_ADD_SCREEN_BTN_Y_POS,
                                                                 ADD_NEW_TASK_IN_ADD_SCREEN_BTN_WIDTH,
                                                                 ADD_NEW_TASK_IN_ADD_SCREEN_BTN_HEIGHT,
                                                                 ADD_NEW_TASK_IN_ADD_SCREEN_BTN_IMAGE)
            self.__object_dict["employee_id_textbox"] = Textbox(self.__screen,
                                                                ADD_NEW_TASK_TEXTBOX_X_POS,
                                                                ADD_NEW_TASK_EMPLOYEE_ID_TEXTBOX_Y_POS,
                                                                ADD_NEW_TASK_TEXTBOX_WIDTH,
                                                                ADD_NEW_TASK_TEXTBOX_HEIGHT)
            self.__object_dict["task_type_textbox"] = Textbox(self.__screen,
                                                              ADD_NEW_TASK_TEXTBOX_X_POS,
                                                              ADD_NEW_TASK_TASK_TYPE_TEXTBOX_Y_POS,
                                                              ADD_NEW_TASK_TEXTBOX_WIDTH,
                                                              ADD_NEW_TASK_TEXTBOX_HEIGHT)
            self.__object_dict["description_textbox"] = Textbox(self.__screen,
                                                                ADD_NEW_TASK_DESCRIPTION_TEXTBOX_X_POS,
                                                                ADD_NEW_TASK_DESCRIPTION_TEXTBOX_Y_POS,
                                                                ADD_NEW_TASK_DESCRIPTION_TEXTBOX_WIDTH,
                                                                ADD_NEW_TASK_DESCRIPTION_TEXTBOX_HEIGHT,
                                                                DESCRIPTION_MAX_LINES)
            self.__create_back_button()
            self.__create_logo()

        self.__add_objects_to_screen()

    def __display_delete_task_screen(self):
        """
        Displays the "Delete Task" screen (creating the buttons, text boxes and background).
        The current screen name will change to the Task Delete screen.
        :return: None
        """
        self.__background = DELETE_TASK_SCREEN_BACKGROUND_IMAGE
        self.__set_background_image()

        # Remove the old text boxes and buttons
        self.__update_dict("delete_task")

        # If the dict is empty add the buttons
        if not self.__object_dict:
            self.__object_dict["delete_btn"] = ImageButton(self.__screen,
                                                           DELETE_BTN_X_POS,
                                                           DELETE_BTN_Y_POS,
                                                           DELETE_BTN_WIDTH,
                                                           DELETE_BTN_HEIGHT,
                                                           DELETE_BTN_IMAGE)
            self.__create_back_button()
            self.__create_logo()

            self.__object_dict["employee_id_textbox"] = Textbox(self.__screen,
                                                                DELETE_TASK_TEXTBOX_X_POS,
                                                                DELETE_TASK_EMPLOYEE_ID_TEXTBOX_Y_POS,
                                                                DELETE_TASK_TEXTBOX_WIDTH,
                                                                DELETE_TASK_TEXTBOX_HEIGHT)
            self.__object_dict["task_id_textbox"] = Textbox(self.__screen,
                                                            DELETE_TASK_TEXTBOX_X_POS,
                                                            DELETE_TASK_TASK_ID_TEXTBOX_Y_POS,
                                                            DELETE_TASK_TEXTBOX_WIDTH,
                                                            DELETE_TASK_TEXTBOX_HEIGHT)

        self.__add_objects_to_screen()

    def __display_add_new_employee_screen(self):
        """
        Displays the "Add New Employee" screen (creating the buttons, text boxes and background).
        The current screen name will change to the Add New Employee screen.
        :return: None
        """
        self.__background = ADD_NEW_EMPLOYEE_SCREEN_BACKGROUND_IMAGE
        self.__set_background_image()

        # Remove the old text boxes and buttons
        self.__update_dict("add_new_employee")

        # If the dict is empty add the buttons
        if not self.__object_dict:
            self.__object_dict["add_new_employee_btn"] = ImageButton(
                self.__screen,
                ADD_NEW_EMPLOYEE_IN_ADD_SCREEN_BTN_X_POS,
                ADD_NEW_EMPLOYEE_IN_ADD_SCREEN_BTN_Y_POS,
                ADD_NEW_EMPLOYEE_IN_ADD_SCREEN_BTN_WIDTH,
                ADD_NEW_EMPLOYEE_IN_ADD_SCREEN_BTN_HEIGHT,
                ADD_NEW_EMPLOYEE_IN_ADD_SCREEN_BTN_IMAGE)
            self.__create_back_button()
            self.__create_logo()

            self.__object_dict["first_name_textbox"] = Textbox(self.__screen,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_X_POS,
                                                               ADD_NEW_EMPLOYEE_FIRST_NAME_TEXTBOX_Y_POS,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_WIDTH,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_HEIGHT)
            self.__object_dict["last_name_textbox"] = Textbox(self.__screen,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_X_POS,
                                                              ADD_NEW_EMPLOYEE_LAST_NAME_TEXTBOX_Y_POS,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_WIDTH,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_HEIGHT)
            self.__object_dict["id_number_textbox"] = Textbox(self.__screen,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_X_POS,
                                                              ADD_NEW_EMPLOYEE_ID_NUMBER_TEXTBOX_Y_POS,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_WIDTH,
                                                              ADD_NEW_EMPLOYEE_TEXTBOX_HEIGHT)
            self.__object_dict["manager_id_textbox"] = Textbox(self.__screen,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_X_POS,
                                                               ADD_NEW_EMPLOYEE_MANAGER_ID_TEXTBOX_Y_POS,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_WIDTH,
                                                               ADD_NEW_EMPLOYEE_TEXTBOX_HEIGHT)
            self.__object_dict["role_textbox"] = Textbox(self.__screen,
                                                         ADD_NEW_EMPLOYEE_TEXTBOX_X_POS,
                                                         ADD_NEW_EMPLOYEE_ROLE_TEXTBOX_Y_POS,
                                                         ADD_NEW_EMPLOYEE_TEXTBOX_WIDTH,
                                                         ADD_NEW_EMPLOYEE_TEXTBOX_HEIGHT)

        self.__add_objects_to_screen()

    def __add_employee_details_to_task_screen(self):
        """
        The function adds the employee details to the screen according to the employee stored in the system.
        :return: None
        """
        font = pygame.font.SysFont('Arial', DETAILS_TEXT_SIZE)

        # Add first name to screen
        self.__screen.blit(
            font.render(self.__employee.get_first_name(), True, WHITE),
            (DETAILS_X_POS, FIRST_NAME_Y_POS))
        # Add last name to screen
        self.__screen.blit(
            font.render(self.__employee.get_last_name(), True, WHITE),
            (DETAILS_X_POS, LAST_NAME_Y_POS))
        # Add ID number to screen
        self.__screen.blit(
            font.render(str(self.__employee.get_id_number()), True, WHITE),
            (DETAILS_X_POS, ID_NUMBER_Y_POS))
        # Add employee ID to screen
        self.__screen.blit(
            font.render(str(self.__employee.get_employees_id()), True, WHITE),
            (DETAILS_X_POS, EMPLOYEE_ID_Y_POS))
        # Add manager ID to screen
        self.__screen.blit(
            font.render(str(self.__employee.get_manager_id()), True, WHITE),
            (DETAILS_X_POS, MANAGER_ID_Y_POS))
        pygame.display.flip()

    def __add_tasks_details_to_task_screen(self):
        """
        The function adds the tasks of the employee stored in the system to the task screen.
        :return: None
        """
        try:
            list_of_tasks = self.__employee.get_list_of_tasks()
            number_of_tasks = min(len(list_of_tasks), MAX_NUM_OF_TASKS)
            font = pygame.font.SysFont('Arial', DETAILS_TEXT_SIZE)

            for task_num in range(number_of_tasks):
                curr_task = list_of_tasks[task_num]
                y_pos = START_Y_POS_FOR_TASKS + task_num * SPACE_BETWEEN_TASK_LINES
                # Add task id to screen
                self.__screen.blit(
                    font.render(curr_task.get_task_id(), True, WHITE),
                    (X_POS_FOR_TASK_ID, y_pos))
                # Add description to screen
                self.__screen.blit(
                    font.render(curr_task.get_description(), True, WHITE),
                    (X_POS_FOR_DETAILS, y_pos))
                # Add status to screen
                if curr_task.get_status() == "v":
                    status_img_path = V_IMAGE
                else:
                    status_img_path = X_IMAGE
                status_img = Image(self.__screen, X_POS_FOR_STATUS, y_pos,
                                   START_IMAGE_WIDTH,
                                   START_IMAGE_HEIGHT, status_img_path)
                status_img.add_image_to_screen()

            pygame.display.flip()
        except:
            print("The get_list_of_tasks function doesn't exist yet")

    def __add_objects_to_screen(self):
        """
        The function goes over any object that is on the screen (using the dictionary that contains objects)
        and displays the objects on the screen.
        :return: None
        """
        for value in self.__object_dict.values():
            if isinstance(value, Textbox):
                value.add_textbox_to_screen()
            else:
                value.add_image_to_screen()

    def __create_back_button(self):
        """
        The function creates the back button and adds it to the dictionary that contains the objects of the screen.
        :return: None
        """
        self.__object_dict["back_btn"] = ImageButton(self.__screen,
                                                     BACK_BTN_X_POS,
                                                     BACK_BTN_Y_POS,
                                                     BACK_BTN_WIDTH,
                                                     BACK_BTN_HEIGHT,
                                                     BACK_BTN_IMAGE)

    def __create_logo(self):
        """
        The function creates the logo image and adds it to the dictionary that contains the objects of the screen.
        :return: None
        """
        self.__object_dict["logo_img"] = Image(self.__screen, LOGO_IMAGE_X_POS,
                                               LOGO_IMAGE_Y_POS,
                                               LOGO_IMAGE_WIDTH,
                                               LOGO_IMAGE_HEIGHT, LOGO_IMAGE)

    def __update_dict(self, label):
        """
        The function checks whether the new screen matches the previous screen.
        In other words did the system move to the next screen or did a refresh.
        If there was a move to the next screen, the function will reset the dictionary and change the screen label.
        :param label: The name of the new screen.
        :return:
        """
        if self.__curr_screen != label:
            self.__object_dict.clear()
            self.__curr_screen = label

    def on_click(self, mouse_pos):
        """
        Tests on the click of a button and checks which button was pressed using the 'Current Screen' variable.
        :param mouse_pos: The position of the mouse click.
        :return: None
        """
        # Handle text boxes
        for value in self.__object_dict.values():
            if isinstance(value, Textbox):
                # Disable typing
                value.disable_typing()

        for value in self.__object_dict.values():
            if isinstance(value, Textbox):
                # Check if the user clicked the textbox
                if value.mouse_in_button(mouse_pos):
                    value.enable_typing()
                    return

        if self.__curr_screen == "login":
            if self.__object_dict["login_btn"].mouse_in_button(mouse_pos):
                username = self.__object_dict["username_textbox"].get_text()
                password = self.__object_dict["password_textbox"].get_text()
                # Check if the username and the password are correct
                try:
                    ans = check_login_details(username, password)
                    if isinstance(ans, Employee):
                        self.__employee = ans
                        self.__display_task_manager_screen()
                    else:
                        self.__display_screen_error(ans)
                except:
                    print("The function check_login_details doesn't exist yet")
                    self.__display_login_screen()

                return

        elif self.__curr_screen == "task_manager":
            # Check if the user clicked the complete task button
            if self.__object_dict["complete_task_btn"].mouse_in_button(
                    mouse_pos):
                self.__display_complete_task_screen()
            elif isinstance(self.__employee, Manager):
                # Check if the user clicked the add new task button
                if self.__object_dict["add_new_task_btn"].mouse_in_button(
                        mouse_pos):
                    self.__display_add_new_task_screen()
                # Check if the user clicked the delete task button
                elif self.__object_dict["delete_task_btn"].mouse_in_button(
                        mouse_pos):
                    self.__display_delete_task_screen()
                # Check if the user clicked the add new employee button
                elif isinstance(self.__employee, Head) and \
                        self.__object_dict[
                            "add_new_employee_btn"].mouse_in_button(mouse_pos):
                    self.__display_add_new_employee_screen()
            return

        elif self.__curr_screen == "complete_task":
            # Check if the user clicked the complete task button
            if self.__object_dict["complete_btn"].mouse_in_button(mouse_pos):
                task_id = self.__object_dict["task_id_textbox"].get_text()
                security_key = self.__object_dict[
                    "security_key_textbox"].get_text()
                ans = self.__employee.complete_employees_task(task_id,
                                                              security_key)
                # Mission accomplished
                if ans == "done":
                    self.__display_task_manager_screen()
                else:
                    self.__display_screen_error(ans)

        elif self.__curr_screen == "add_new_task":
            # Check if the user clicked the complete task button
            if self.__object_dict["add_new_task_btn"].mouse_in_button(
                    mouse_pos):
                employees_id = self.__object_dict[
                    "employee_id_textbox"].get_text()
                task_type = self.__object_dict["task_type_textbox"].get_text()
                description = self.__object_dict[
                    "description_textbox"].get_text()
                ans = self.__employee.add_new_employees_task(employees_id,
                                                             task_type,
                                                             description)
                # Mission accomplished
                if ans == "done":
                    self.__display_task_manager_screen()
                else:
                    self.__display_screen_error(ans)

        elif self.__curr_screen == "delete_task":
            # Check if the user clicked the complete task button
            if self.__object_dict["delete_btn"].mouse_in_button(mouse_pos):
                employees_id = self.__object_dict[
                    "employee_id_textbox"].get_text()
                task_id = self.__object_dict["task_id_textbox"].get_text()
                ans = self.__employee.delete_employees_task(employees_id,
                                                            task_id)
                # Mission accomplished
                if ans == "done":
                    self.__display_task_manager_screen()
                else:
                    self.__display_screen_error(ans)

        elif self.__curr_screen == "add_new_employee":
            # Check if the user clicked the complete task button
            if self.__object_dict["add_new_employee_btn"].mouse_in_button(
                    mouse_pos):
                first_name = self.__object_dict["first_name_textbox"].get_text()
                last_name = self.__object_dict["last_name_textbox"].get_text()
                id_number = self.__object_dict["id_number_textbox"].get_text()
                manager_id = self.__object_dict["manager_id_textbox"].get_text()
                role = self.__object_dict["role_textbox"].get_text()
                ans = self.__employee.add_new_employee(first_name, last_name,
                                                       id_number, manager_id,
                                                       role)
                # Mission accomplished
                if ans == "done":
                    self.__display_task_manager_screen()
                else:
                    self.__display_screen_error(ans)
        # Handle the back button
        if "back_btn" in self.__object_dict and self.__object_dict[
            "back_btn"].mouse_in_button(mouse_pos):
            self.__display_task_manager_screen()

    def typing(self, ascii_val):
        """
        The function is called as soon as one of the keyboard keys is pressed.
        The function checks if the typing is active in one of the text boxes, then the character is checked.
        If it is correct the character will be added to the text box
        :param ascii_val: The key on the keyboard that was pressed by the user (Its ascii value).
        :return: None
        """
        # Check if char is a number
        if ord('0') <= ascii_val <= ord('9'):
            ascii_val = ascii_val - ord('0')
            char = str(ascii_val)
        # Handle the numbers pad
        elif ascii_val == ZERO:
            char = '0'
        # Handle the numbers pad
        elif ONE <= ascii_val <= NINE:
            char = str(ascii_val - ONE + 1)
        # Handle the small letters
        elif ord('a') <= ascii_val <= ord('z'):
            char = chr(ascii_val)
        elif ascii_val == DELETE_KEY or ascii_val == BACKSPACE_KEY:
            for value in self.__object_dict.values():
                if isinstance(value, Textbox):
                    if value.get_typing_status():
                        value.delete_letter()
            # Update the screen
            self.__display_curr_screen()
            return
        elif ascii_val == ord(','):
            char = ","
        elif ascii_val == ord(' '):
            char = " "
        else:
            return

        for value in self.__object_dict.values():
            if isinstance(value, Textbox):
                if value.get_typing_status():
                    value.add_letter(char)
        self.__display_curr_screen()

    def __display_screen_error(self, error_path):
        """
        The function gets a path to the error image and displays it on the screen.
        :param error_path: The path to the error image.
        :return: None
        """
        err = Image(self.__screen, ERROR_X_POS, ERROR_Y_POS, ERROR_WIDTH,
                    ERROR_HEIGHT, error_path)
        err.add_image_to_screen()

    def __display_curr_screen(self):
        """
        Refreshing the current screen, the function uses a variable that stores the name of the current screen
        and calls the current screen display function.
        :return: None
        """
        func_name = "__display_" + self.__curr_screen + "_screen"
        getattr(self, '_' + self.__class__.__name__ + func_name)()

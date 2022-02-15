from employee_classes.Head import *
import Database
from constants import *

def check_login_details(username, password):

    if username == None or password == None:
        return  "images/errors/empty_fields.jpg"
            # EMPTY_FIELDS_ERROR

    if len(username) != 10:
        return"images/errors/wrong_username_or_password.jpg"
               #WRONG

    if first_name or last_name or id_number or employee_id or manager_id or Role is None:
        return "images/errors/wrong_username_or_password.jpg"
            #WRONG_USERNAME_OR_PASSWORD_ERROR

    if employee[4] != username[4:8]:
        return "images/errors/wrong_username_or_password.jpg"
            #WRONG_USERNAME_OR_PASSWORD_ERROR

    if username_numbers_sum % 10 != 0:
        return "images/errors/wrong_username_or_password.jpg"
            #WRONG_USERNAME_OR_PASSWORD_ERROR

    if password_numbers_sum != username_numbers_sum:
        return "images/errors/wrong_username_or_password.jpg"
            #WRONG_USERNAME_OR_PASSWORD_ERROR





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

    if





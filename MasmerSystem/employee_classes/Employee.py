import Database
from constants import *

class Employee():
    def _init_(self, first_name, last_name, id_number, employee_id, manager_id, Role):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
        self._employee_id = employee_id
        self._manager_id = manager_id
        self._Role = Role

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_id_number(self):
        return self.__id_number

    def get_employee_id(self):
        return self._employee_id

    def get_manager_id(self):
        return self._manager_id

    def get_role(self):
        return self._Role
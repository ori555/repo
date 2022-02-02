from constants import *
from tasks_clases.FieldTask import *
from tasks_clases.OfficeTask import *
from employee_classes.Manager import *
from employee_classes.Employee import *


def get_employee_by_employees_id(employees_id):
    # open the file
    file = open(EMPLOYEES_FILE_PATH, "r")
    # Reading from file
    line = file.readline()
    while line:
        # Remove \n
        if line[len(line) - 1] == "\n":
            line = line[0:len(line) - 1]
        elements = line.split("*")
        if elements[EMPLOYEES_ID_INDEX] == employees_id:
            # close the file
            file.close()
            return elements
        # Reading from file
        line = file.readline()
    # close the file
    file.close()
    return None


def is_manager_by_employees_id(employees_id):
    # open the file
    file = open(EMPLOYEES_FILE_PATH, "r")
    # Reading from file
    line = file.readline()
    while line:
        # Remove \n
        if line[len(line) - 1] == "\n":
            line = line[0:len(line) - 1]
        elements = line.split("*")
        if elements[EMPLOYEES_ID_INDEX] == employees_id:
            if elements[ROLE_INDEX] == "m" or elements[ROLE_INDEX] == "h":
                # close the file
                file.close()
                return True
            break
        # Reading from file
        line = file.readline()
    # close the file
    file.close()
    return False


def get_list_of_employees(employees_id):
    list_of_employees_id = []
    # open the file
    file = open(EMPLOYEES_FILE_PATH, "r")
    # Reading from file
    line = file.readline()
    while line:
        # Remove \n
        if line[len(line) - 1] == "\n":
            line = line[0:len(line) - 1]
        elements = line.split("*")
        if elements[MANAGERS_ID_INDEX] == employees_id:
            list_of_employees_id.append(elements[EMPLOYEES_ID_INDEX])
        # Reading from file
        line = file.readline()
    # close the file
    file.close()

    return list_of_employees_id


def get_list_of_tasks_from_database(employees_id):
    list_of_tasks = []
    # open the file
    file = open(TASKS_FILE_PATH, "r")
    # Reading from file
    line = file.readline()
    while line:
        # Remove \n
        if line[len(line) - 1] == "\n":
            line = line[0:len(line) - 1]
        elements = line.split("*")
        if elements[TASK_FILE_EMPLOYEES_ID_INDEX] == employees_id:
            task_id = elements[TASK_FILE_TASK_ID_INDEX]
            full_description = elements[TASK_FILE_DESCRIPTION]
            splitted_description = full_description.split(",")
            status = elements[TASK_FILE_STATUS]
            if elements[TASK_FILE_TASK_TYPE] == "o":
                folder = splitted_description[0]
                file_name = splitted_description[1]
                involvement = splitted_description[2]
                try:
                    new_task = OfficeTask(task_id, employees_id, folder, file_name, involvement, status)
                    list_of_tasks.append(new_task)
                except:
                    print("The class OfficeTask doesn't exist yet")
            else:
                # The task is "F"
                country = splitted_description[0]
                city = splitted_description[1]
                target = splitted_description[2]
                try:
                    new_task = FieldTask(task_id, employees_id, country, city, target, status)
                    list_of_tasks.append(new_task)
                except:
                    print("The class FieldTask doesn't exist yet")
            # list_of_tasks.append(new_task)
        # Reading from file
        line = file.readline()
    # close the file
    file.close()
    return list_of_tasks


def update_tasks_status(task_id):
    # open the file
    file = open(TASKS_FILE_PATH, "r")
    # Reading from file
    data = file.readlines()
    number_of_line = get_line_by_task_id(data, task_id)
    if number_of_line is None:
        return
    data[number_of_line] = data[number_of_line][:-2] + "v\n"

    with open(TASKS_FILE_PATH, 'w') as file:
        file.writelines(data)

    # close the file
    file.close()


def get_line_by_task_id(data, task_id):
    number_of_line = 0
    while number_of_line < len(data):
        curr_task = data[number_of_line].split("*")
        if curr_task[0] == task_id:
            return number_of_line
        number_of_line += 1
    return None


def delete_task_from_database(employees_id, task_id):
    # open the file
    file = open(TASKS_FILE_PATH, "r")
    # Reading from file
    data = file.readlines()
    number_of_line = get_line_by_task_id(data, task_id)
    if number_of_line is None:
        return False
    if (data[number_of_line]).split("*")[TASK_FILE_EMPLOYEES_ID_INDEX] != employees_id:
        # close the file
        file.close()
        return False
    del data[number_of_line]

    with open(TASKS_FILE_PATH, 'w') as file:
        file.writelines(data)

    # close the file
    file.close()
    return True


def add_new_task_to_database(employees_id, task_type, description):
    splitted_description = description.split(",")
    task_id = get_next_task_id()

    if len(splitted_description) != 3:
        return None

    if task_type == "f":
        if not (splitted_description[2] == "enemy" or splitted_description[2] == "mossad member"):
            return None
    else:
        # task_type = "o":
        if not (splitted_description[2] == "yes" or splitted_description[2] == "no"):
            return None

    new_line = str(task_id) + "*" + employees_id + "*" + task_type + "*" + description + "*x\n"

    if task_type == "f":
        new_task = FieldTask(task_id, employees_id, splitted_description[0], splitted_description[1],
                             splitted_description[2], "x")
    else:
        new_task = OfficeTask(task_id, employees_id, splitted_description[0], splitted_description[1],
                              splitted_description[2], "x")

    # open the file
    file = open(TASKS_FILE_PATH, "r")
    # Reading from file
    data = file.readlines()

    data.append(new_line)

    with open(TASKS_FILE_PATH, 'w') as file:
        file.writelines(data)

    # close the file
    file.close()
    return new_task


def get_next_task_id():
    # open the file
    file = open(TASKS_FILE_PATH, "r")
    # Reading from file
    data = file.readlines()

    if len(data) == 0:
        last_task_id = 7000
    else:
        last_task_id = data[-1][0:4]
        last_task_id = int(last_task_id)

    # close the file
    file.close()
    return str(last_task_id + 1)


def add_new_employee_to_database(first_name, last_name, id_number, manager_id, role):
    employee_id = first_name[0] + last_name[0] + id_number[0:2]
    new_line = first_name + "*" + last_name + "*" + id_number + "*" + employee_id + "*" + manager_id + "*" + role + "\n"

    # open the file
    file = open(EMPLOYEES_FILE_PATH, "r")
    # Reading from file
    data = file.readlines()

    data.append(new_line)

    with open(EMPLOYEES_FILE_PATH, 'w') as file:
        file.writelines(data)

    # close the file
    file.close()
    return employee_id

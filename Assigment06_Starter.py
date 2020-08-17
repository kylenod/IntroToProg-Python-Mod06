# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KODonnell, 8.8.2020, Added code to complete assignment 5
# KODonnell, 8.16.2020, Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of processing functions
boolRemoved = None  # Captures status of 'removed' item

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):  # load data from file
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            list_of_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)  # save data to list of rows
            file.close()
        except: pass
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):  # add new task, priority to list
        """ Add new task to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with priority of task:
        :param (list_of_rows): (list) to add new data to:
        :return: (list) of dictionary rows
        """
        dicRow = {"Task": task, "Priority": priority}
        list_of_rows.append(dicRow)  # save new row to list of rows
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):  # remove task from list
        """ Add new task to a list of dictionary rows

        :param task: (string) with name of task:
        :param (list_of_rows): (list) to remove task from:
        :return: (list) of dictionary rows,
        :return: (bool) of removed task status
        """
        removed = False
        kept_items = []
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():  # find task in list
                removed = True
            else:
                kept_items.append(row)  # add all other tasks to new list
        return kept_items, removed, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):  # save current list to text file
        """ Write new table to file as list of dictionary rows

        :param file_name: (string) with name of file:
        :param (list_of_rows): (list) of dictionary rows:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"].capitalize() + ", " + row["Priority"].upper()+"\n")
        objFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():  # print options menu
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        count = 0
        for row in list_of_rows:
            count += 1
            print(str(count) + ". " + row["Task"].capitalize() + " | " + row["Priority"].upper())
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Prompts user for new task and priority
        :return: strings for task, priority
        """
        Task = str(input("Please enter a new To Do task:\n ")).strip().lower()
        Priority = str(input("Please enter the priority for {} (High, Medium or Low):\n ".format(Task))).strip().lower()
        return Task, Priority

    @staticmethod
    def input_task_to_remove():
        """ Prompts user for task to remove
        :return: string of task
        """
        Task = str(input("Which item would you like to remove?\n "))
        return Task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()  # Elicit new task, priority
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)  # Add new task to list/table
        IO.input_press_to_continue("{} saved to your list!".format(strTask).capitalize())
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove()  # Elicit task to remove
        lstTable, boolRemoved, strStatus = Processor.remove_data_from_list(strTask, lstTable) # 'Remove' task from list
        if boolRemoved == False:
            print("{} is not on your your list.".format(strTask).capitalize())  # Message if task found
        else:
            print("{} has been removed from your list!".format(strTask).capitalize())  # Message if task not found
        IO.input_press_to_continue("")
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # Elicit Confirmation
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)  # Write data to text file
            IO.input_press_to_continue("Your data has been saved to 'ToDoList.txt")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")  # Elicit confirmation
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)  # Load data from file
            IO.input_press_to_continue("Your list has been reloaded from ToDoList.txt!")
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit

    else:  # Return to menu
        IO.input_press_to_continue("Please select an option from the menu.")
        continue  # to show menu
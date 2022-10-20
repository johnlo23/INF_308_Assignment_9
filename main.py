# John Logiudice
# INF 308 - Fall 2022
# Assignment 9 - Inheritance
# An employee list/information manager

# Class to create employee objects
class Employee:

    # Initialize an employee object. Attributes stored in a dictionary. Employee_id is required.
    def __init__(self, employee_id):
        self.employee_details = {'employee_id': employee_id,
                                 'name_first': None,
                                 'name_last': None,
                                 'start_year': None,
                                 'address': None,
                                 'city': None,
                                 'state': None
                                 }

    # Set employee details. Update dictionary.
    def set_employee_id(self, employee_id):
        self.employee_details['employee_id'] = employee_id

    def set_name_first(self, name_first):
        self.employee_details['name_first'] = name_first

    def set_name_last(self, name_last):
        self.employee_details['name_last'] = name_last

    def set_start_year(self, start_year):
        self.employee_details['start_year'] = start_year

    def set_address(self, address):
        self.employee_details['address'] = address

    def set_city(self, city):
        self.employee_details['city'] = city

    def set_state(self, state):
        self.employee_details['state'] = state

    # Update all employee details at once.
    def add_details(self, details):
        self.set_employee_id(details[0])
        self.set_name_first(details[1])
        self.set_name_last(details[2])
        self.set_start_year(details[3])
        self.set_address(details[4])
        self.set_city(details[5])
        self.set_state(details[6])

    # Return location - City & State
    def get_location(self):
        return f"{self.employee_details['city']} {self.employee_details['state']}"

    # Return full name - First & Last
    def get_full_name(self):
        return f"{self.employee_details['name_first']} {self.employee_details['name_last']}"

    # Formatted employee details for print to screen
    def show_details(self):
        print(f"Employee: {self.employee_details['employee_id']}")
        print(f"Name: {self.get_full_name()}")
        print(f"Start Year: {self.employee_details['start_year']}")
        print(f"Address: {self.employee_details['address']}")
        print(f"Location: {self.get_location()}")


class Manager(Employee):
    def __init__(self, employee_id):
        self.title = None
        self.sub_list = None
        super().__init__(self)


# Class to create employee List objects
class EmployeeList:

    # Initialize the employee list as an empty list
    def __init__(self):
        self.employee_list = list()

    # Add a new employee object and add to the employee list
    def add_employee(self, name, details):
        # Add the employee to the employee list and create a new employee object
        self.employee_list.append({'name': name, 'details': Employee(name)})
        # For the latest employee in the employee list, add the acquired details
        self.employee_list[-1]['details'].add_details(details)

    # Find the employee's index number by name
    def find_employee(self, name):
        for i in range(0, len(self.employee_list)):
            if self.employee_list[i]['name'].lower() == name.lower():
                return i
        return None

    # sort the employee list by employee ID
    def sort_employee_list(self):
        self.employee_list.sort(key=lambda name: name['name'])

    # Get list of employee IDs
    def get_employee_list(self):
        # Get employee list with list comprehension
        return [employee['name'] for employee in self.employee_list]


# Class to create a menu with menu numbers
class PickMenu:

    # Initialize the menu with required Title and menu Items
    def __init__(self, menu_details):
        self.menu_name = menu_details['title']
        self.menu_items = menu_details['items']

    # Print each menu item with menu numbers
    def show_menu(self):
        print(self.menu_name)
        print("- - - - - - - -")
        for i in range(0, len(self.menu_items)):
            print(f"{str(i + 1)}. {self.menu_items[i]}")

    # Get and validate menu choice from user
    def get_menu_response(self):
        # loop until user gives valid menu response
        while True:
            # Ask user for menu number
            response = input("Enter the number of your menu choice: ").strip()
            # Check if response string is an integer
            if response.isdigit():
                # Check if response is a valid menu integer
                if (int(response) - 1) in range(0, len(self.menu_items)):
                    return int(response)

            # User did not enter valid integer response
            print(f"Please enter a menu choice between 1 and {len(self.menu_items)}.")
            print()


# Function to get the employee ID
def get_name():
    # Loop until a name is entered
    while True:
        name = input("Enter a new employee ID: ").strip()
        # Validate that text was entered
        if len(name) > 0:
            return name
        else:
            print("The employee ID cannot be blank.")
            print()


# Function to get new employee details from user
def get_details(name):
    # Get employee's name
    print("Name details")
    first = input("Enter the first name: ").strip()
    last = input("Enter the last name: ").strip()
    print()

    # Get personal details
    print("Personal description")
    start_year = input("Enter the start year: ").strip()
    address = input("Enter the address: ").strip()
    print()

    # Get location details
    print("Location")
    city = input("Enter the city name: ").strip()
    state = input("Enter the state abbreviation: ").strip()
    print()

    return name, first, last, start_year, address, city, state


# Function to execute user choice
def menu_action(menu_choice, employee_list):
    # 1. Add a new employee
    if menu_choice == 1:
        add_employee(employee_list, get_name())
        print()

    # 2. Show employee information
    elif menu_choice == 2:
        show_employee_list(employee_list)
        print()

    # 3. Sort employee list
    elif menu_choice == 3:
        sort_employee_list(employee_list)
        print()

    # 4. Quit
    elif menu_choice == 4:
        app_quit()


# Function to add a new employee
def add_employee(employee_list_obj, name):
    # Check if name is already in the employee list
    if not employee_list_obj.find_employee(name.lower()) is None:
        # Employee ID already exists
        print('Sorry, that name is already taken.')
    else:
        # Employee ID is available
        employee_list_obj.add_employee(name, get_details(name))


# Function to show the employee list as a menu and show employee details
def show_employee_list(employee_list_obj):
    # Employee List menu details
    # Get list of employee IDs from employee object
    employee_menu_list = employee_list_obj.get_employee_list()
    employee_menu_name = 'Employee List'
    employee_menu_details = {'title': employee_menu_name, 'items': employee_menu_list}

    # Create the Employee List menu object
    employee_menu = PickMenu(employee_menu_details)

    # Show the Employee List menu
    employee_menu.show_menu()

    # Get the employee menu choice - subtract 1 to match list index
    employee_choice = employee_menu.get_menu_response() - 1
    print()

    # Call the show employee details method
    employee_list_obj.employee_list[employee_choice]['details'].show_details()


# Function to call the employee list sort
def sort_employee_list(employee_list_obj):
    employee_list_obj.sort_employee_list()


# Function to quit the program
def app_quit():
    print("Goodbye")
    quit()


def main():
    # Create the Employee List object
    employee_list = EmployeeList()

    # Sample employee list Data
    employee_list.add_employee('ID289435',
                               ('ID289435', 'John', 'Logiudice', '2015', '134 Market Square', 'Wala Wala', 'WA'))
    employee_list.add_employee('ID279423', (
        'ID279423', 'Gandolph', 'Verspasian', '2018', '200-20 3rd Ave Apt 12B', 'Portland', 'OR'))
    employee_list.add_employee('ID280121',
                               ('ID280121', 'Jandra', 'De La Cruz', '2021', '74 Carlos Silva Dr.', 'La Jolla', 'CA'))

    # Main Menu details
    main_menu_tuple = ('Add a new employee', 'Show employee information', 'Sort employee list', 'Quit')
    main_menu_name = 'Main Menu'
    main_menu_details = {'title': main_menu_name, 'items': main_menu_tuple}

    # Create the Main Menu object
    main_menu = PickMenu(main_menu_details)

    # loop the main menu until user quits
    while True:
        # Show the main menu
        main_menu.show_menu()
        print()

        # Get user menu choice
        user_choice = main_menu.get_menu_response()
        print()

        # Execute user menu choice
        menu_action(user_choice, employee_list)


# Execute the main function
if __name__ == '__main__':
    main()

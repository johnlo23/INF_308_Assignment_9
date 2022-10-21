# John Logiudice
# INF 308 - Fall 2022
# Assignment 9 - Inheritance
# An employee list/information manager

# Class to create employee objects
class Employee:

    # Initialize an employee object. Attributes stored in a dictionary. Employee_id is required.
    def __init__(self, employee_id, name_first=None, name_last=None,
                 start_year=None, address=None, city=None,
                 state=None):
        # Initialize empty dictionary
        self.employee_details = {}

        # Set employee details with self methods
        self.set_employee_id(employee_id)
        self.set_name_first(name_first)
        self.set_name_last(name_last)
        self.set_start_year(start_year)
        self.set_address(address)
        self.set_city(city)
        self.set_state(state)

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
        print(f"Full Name: {self.get_full_name()}")
        print(f"Start Year: {self.employee_details['start_year']}")
        print(f"Address: {self.employee_details['address']}")
        print(f"Location: {self.get_location()}")


class Manager(Employee):
    def __init__(self, employee_id, title=None, sub_list=None):
        super().__init__(employee_id)

        # Ensure sub_list is a list if none is given
        if sub_list is None:
            sub_list = []

        # Set manager specific details with self methods
        self.set_title(title)
        self.set_sub_list(sub_list)

    # Set manager details. Update dictionary.
    def set_title(self, title):
        self.employee_details['title'] = title

    def set_sub_list(self, sub_list):
        self.employee_details['sub_list'] = sub_list

    # Update all employee details at once.
    def add_details(self, details):
        super().add_details(details)
        self.set_title(details[7])
        self.set_sub_list(details[8])

    def show_details(self):
        # Call super method to show employee details
        super().show_details()

        # Print manager specific details
        print(f"Title: {self.employee_details['title']}")
        print(f"Subordinate List: {self.employee_details['sub_list']}")


# Class to create employee List objects
class EmployeeList:

    # Initialize the employee list as an empty list
    def __init__(self, employee_type=0):
        self.employees_list = list()
        self.employee_type = employee_type

    # Add a new employee object and add to the employee list
    def add_employee(self, details):
        # Add the employee to the employee list and create a new employee object
        if self.employee_type == 1:
            # Manager
            self.employees_list.append({'employee_id': details[0], 'details': Manager(details[0])})
        else:
            # Employee
            self.employees_list.append({'employee_id': details[0], 'details': Employee(details[0])})
        # For the latest employee in the employee list, add the acquired details
        self.employees_list[-1]['details'].add_details(details)

    # Find the employee's index number by employee_id
    def find_employee(self, employee_id):
        for i in range(0, len(self.employees_list)):
            if self.employees_list[i]['employee_id'].lower() == employee_id.lower():
                return i
        return None

    # sort the employee list by employee ID
    def sort_employee_list(self):
        self.employees_list.sort(key=lambda employee_id: employee_id['employee_id'])

    # Get list of employee IDs
    def get_employee_list(self):
        # Get employee list with list comprehension
        return [employee['employee_id'] for employee in self.employees_list]


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
def get_employee_id():
    # Loop until a employee_id is entered
    while True:
        employee_id = input("Enter a new employee ID: ").strip()
        # Validate that text was entered
        if len(employee_id) > 0:
            return employee_id
        else:
            print("The employee ID cannot be blank.")
            print()


# Function to get new employee details from user
def get_details(employee_id):
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

    return employee_id, first, last, start_year, address, city, state


# Function to execute user choice
def main_menu_action(menu_choice):
    # 1. Add a new employee
    if menu_choice == 1:
        add_employee(employee_list, get_employee_id())
        print()

    # 2. Show employee information
    elif menu_choice == 2:
        show_employee_list(employee_list)
        print()

    # 3. Sort employee list
    elif menu_choice == 3:
        sort_employee_list(employee_list)
        print()

    # 4. Manager Menu
    elif menu_choice == 4:
        create_manager_menu()

    # 5. Quit
    elif menu_choice == 5:
        app_quit()


# Function to add a new employee
def add_employee(employee_list_obj, employee_id):
    # Check if employee ID is already in the employee list
    if not employee_list_obj.find_employee(employee_id.lower()) is None:
        # Employee ID already exists
        print('Sorry, that employee ID is already taken.')
    else:
        # Employee ID is available
        employee_list_obj.add_employee(get_details(employee_id))


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

    # Get the user menu choice - subtract 1 to match list index
    user_choice = employee_menu.get_menu_response() - 1
    print()

    # Call the show employee details method
    employee_list_obj.employees_list[user_choice]['details'].show_details()


# Function to call the employee list sort
def sort_employee_list(employee_list_obj):
    employee_list_obj.sort_employee_list()


# Function to quit the program
def app_quit():
    print("Goodbye")
    quit()


def create_manager_menu():
    manager_menu_tuple = ('Add a new manager', 'Show manager information', 'Sort manager list', 'Exit')
    manager_menu_name = 'Manager Menu'
    manager_menu_details = {'title': manager_menu_name, 'items': manager_menu_tuple}
    # Create the Main Menu object
    manager_menu = PickMenu(manager_menu_details)

    menu_return = True
    # loop the main menu until user quits
    while menu_return:
        # Show the main menu
        manager_menu.show_menu()
        print()

        # Get user menu choice
        user_choice = manager_menu.get_menu_response()
        print()

        # Execute user menu choice
        menu_return = manager_menu_action(user_choice)


# Function to execute user choice
def manager_menu_action(menu_choice):
    # 1. Add a new employee
    if menu_choice == 1:
        add_manager(manager_list, get_employee_id())
        print()

    # 2. Show employee information
    elif menu_choice == 2:
        show_employee_list(manager_list)
        print()

    # 3. Sort employee list
    elif menu_choice == 3:
        sort_employee_list(manager_list)
        print()

    # 4. Quit
    elif menu_choice == 4:
        return False

    return True


# Function to add a new employee
def add_manager(manager_list_obj, employee_id):
    # Check if employee ID is already in the employee list
    if not manager_list_obj.find_employee(employee_id.lower()) is None:
        # Employee ID already exists
        print('Sorry, that employee ID is already taken.')
    else:
        # Employee ID is available
        employee_details = get_details(employee_id)
        manager_details = get_manager_details(employee_id)
        employee_details = employee_details + manager_details
        manager_list_obj.add_employee(employee_details)


# Function to get new manager details from user
def get_manager_details(employee_id):
    # Get manager's title
    print("Manager details")
    title = input("Enter the manager's title: ").strip()

    sub_list = []
    cnt = 1
    while True:
        user_input = input(f"Enter subordinate number {cnt}: ").strip()
        if len(user_input) > 0:
            sub_list.append(user_input)
        else:
            break
        cnt += 1
    print()
    return title, sub_list


def main():

    # Sample employee list Data
    employee_list.add_employee(('ID289435', 'John', 'Logiudice', '2015', '134 Market Square', 'Wala Wala', 'WA'))
    employee_list.add_employee(('ID279423', 'Gandolph', 'Verspasian', '2018', '200-20 3rd Ave Apt 12B', 'Portland', 'OR'))
    employee_list.add_employee(('ID280121', 'Jandra', 'De La Cruz', '2021', '74 Carlos Silva Dr.', 'La Jolla', 'CA'))
    employee_list.add_employee(('ID268012', 'Liangzhao', 'Ping', '2013', '800 Liberty Way', 'Portland', 'OR'))

    manager_list.add_employee(('ID280121', 'Jandra', 'De La Cruz', '2021', '74 Carlos Silva Dr.', 'La Jolla', 'CA',
                               'Supervisor', ['ID234143', 'ID3423412', 'ID1231241', 'ID123123']))
    manager_list.add_employee(('ID268012', 'Liangzhao', 'Ping', '2013', '800 Liberty Way', 'Portland', 'OR', 'Director',
                               ['ID23241', 'ID193242', 'ID2341234', 'ID231249']))

    # Main Menu details
    main_menu_tuple = ('Add a new employee', 'Show employee information', 'Sort employee list', 'Manager Menu', 'Quit')
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
        main_menu_action(user_choice)


# Execute the main function
if __name__ == '__main__':
    # Create the Employee List object
    employee_list = EmployeeList(0)

    # Create the Manager List object
    manager_list = EmployeeList(1)
    main()

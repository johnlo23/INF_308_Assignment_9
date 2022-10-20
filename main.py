# John Logiudice
# INF 308 - Fall 2022
# Assignment 8 - Classes and Objects
# A user list/information manager

# Class to create user objects
class User:

    # Initialize a user object. Attributes stored in a dictionary. Name is required.
    def __init__(self, user_name):
        self.user_details = {'user': user_name,
                             'name_first': None,
                             'name_last': None,
                             'eyes': None,
                             'hair': None,
                             'city': None,
                             'state': None
                             }

    # Set user details. Update dictionary.
    def set_user_name(self, user_name):
        self.user_details['user'] = user_name

    def set_name_first(self, name_first):
        self.user_details['name_first'] = name_first

    def set_name_last(self, name_last):
        self.user_details['name_last'] = name_last

    def set_eyes(self, eyes):
        self.user_details['eyes'] = eyes

    def set_hair(self, hair):
        self.user_details['hair'] = hair

    def set_city(self, city):
        self.user_details['city'] = city

    def set_state(self, state):
        self.user_details['state'] = state

    # Update all user details at once.
    def add_details(self, details):
        self.set_user_name(details[0])
        self.set_name_first(details[1])
        self.set_name_last(details[2])
        self.set_eyes(details[3])
        self.set_hair(details[4])
        self.set_city(details[5])
        self.set_state(details[6])

    # Return location - City & State
    def get_location(self):
        return f"{self.user_details['city']} {self.user_details['state']}"

    # Return full name - First & Last
    def get_full_name(self):
        return f"{self.user_details['name_first']} {self.user_details['name_last']}"

    # Formatted user details for print to screen
    def show_details(self):
        print(f"User: {self.user_details['user']}")
        print(f"Name: {self.get_full_name()}")
        print(f"Eyes: {self.user_details['eyes']}")
        print(f"Hair: {self.user_details['hair']}")
        print(f"Location: {self.get_location()}")


# Class to create User List objects
class UserList:

    # Initialize the user list as an empty list
    def __init__(self):
        self.user_list = list()

    # Add a new user object and add to the user list
    def add_user(self, name, details):
        # Add the user to the user list and create a new user object
        self.user_list.append({'name': name, 'details': User(name)})
        # For the latest user in the user list, add the acquired details
        self.user_list[-1]['details'].add_details(details)

    # Find the user's index number by name
    def find_user(self, name):
        for i in range(0, len(self.user_list)):
            if self.user_list[i]['name'].lower() == name.lower():
                return i
        return None

    # sort the user list by user name
    def sort_user_list(self):
        self.user_list.sort(key=lambda name: name['name'])

    # Get list of user names
    def get_user_list(self):
        # Get user list with list comprehension
        return [user['name'] for user in self.user_list]


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


# Function to get the user name
def get_name():
    # Loop until a name is entered
    while True:
        name = input("Enter a new user name: ").strip()
        # Validate that text was entered
        if len(name) > 0:
            return name
        else:
            print("The user name cannot be blank.")
            print()


# Function to get new user details from user
def get_details(name):
    # Get user name
    print("Name details")
    first = input("Enter the first name: ").strip()
    last = input("Enter the last name: ").strip()
    print()

    # Get personal details
    print("Personal description")
    eyes = input("Enter the eye color: ").strip()
    hair = input("Enter the hair color: ").strip()
    print()

    # Get location details
    print("Location")
    city = input("Enter the city name: ").strip()
    state = input("Enter the state abbreviation: ").strip()
    print()

    return name, first, last, eyes, hair, city, state


# Function to execute user choice
def menu_action(menu_choice, user_list):

    # 1. Add a new user
    if menu_choice == 1:
        add_user(user_list, get_name())
        print()

    # 2. Show user information
    elif menu_choice == 2:
        show_user_list(user_list)
        print()

    # 3. Sort user list
    elif menu_choice == 3:
        sort_user_list(user_list)
        print()

    # 4. Quit
    elif menu_choice == 4:
        app_quit()


# Function to add a new user
def add_user(user_list_obj, name):
    # Check if name is already in the user list
    if not user_list_obj.find_user(name.lower()) is None:
        # User name already exists
        print('Sorry, that name is already taken.')
    else:
        # User name is available
        user_list_obj.add_user(name, get_details(name))


# Function to show the user list as a menu and show user details
def show_user_list(user_list_obj):
    # User List menu details
    # Get list of user names from user object
    user_menu_list = user_list_obj.get_user_list()
    user_menu_name = 'User List'
    user_menu_details = {'title': user_menu_name, 'items': user_menu_list}

    # Create the User List menu object
    user_menu = PickMenu(user_menu_details)

    # Show the User List menu
    user_menu.show_menu()

    # Get the user menu choice - subtract 1 to match list index
    user_choice = user_menu.get_menu_response() - 1
    print()

    # call the show user details method
    user_list_obj.user_list[user_choice]['details'].show_details()


# Function to call the user list sort
def sort_user_list(user_list_obj):
    user_list_obj.sort_user_list()


# Function to quit the program
def app_quit():
    print("Goodbye")
    quit()


def main():
    # Create the User List object
    user_list = UserList()

    # Sample user list Data
    user_list.add_user('John23', ('John23', 'John', 'Logiudice', 'brown', 'brown', 'Wala Wala', 'WA'))
    user_list.add_user('RollyPanda', ('RollyPanda', 'Gandolph', 'Verspasian', 'hazel', 'blonde', 'Portland', 'OR'))
    user_list.add_user('Jandra2001', ('Jandra2001', 'Jandra', 'De La Cruz', 'green', 'brown', 'La Jolla', 'CA'))

    # Main Menu details
    main_menu_tuple = ('Add a new user', 'Show user information', 'Sort user list', 'Quit')
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
        menu_action(user_choice, user_list)


# Execute the main function
if __name__ == '__main__':
    main()

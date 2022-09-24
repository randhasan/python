'''

Dictionaries practice
HCP
Demonstration of various dictionary functions
'''

import inputHelpers


# Global constants for menu choices
LOOK_UP = 1
ADD     = 2
CHANGE  = 3
DELETE  = 4
LIST    = 5
QUIT    = 6

def get_menu_choice():
    print()
    print('My Contacts')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change a contact')
    print('4. Delete a contact')
    print('5. List all contacts')
    print('6. Quit the program')
    print()

    # Get the user's choice.
    choice = inputHelpers.getIntBetween('Enter your choice ',1,6)

    # return the user's choice.
    return choice



def look_up(contacts):
    name = input("Enter name of contact: ").title()
    print(contacts.get(name,"Contact not found"))
    


def add(contacts):
    name = input("Enter name of new contact: ").title()
    phone = input("Enter the phone number of new contact: ")
    if name not in contacts: #check for duplicates
        contacts[name]=phone #adds new dictionary pair
        


def change(contacts):
    name = input("Enter name of a contact to change: ").title()
    if name in contacts:
        phone = input("Enter the new phone number of contact: ")
        contacts[name] = contacts
        print("Contact information changed for "+name+ "---------------")
    else:
        print("Invalid contact name entered.")

def showList(contacts):
    return 42

def delete(contacts):
    return 42


def main():
    
    #key:value pairs stored in dictionary
    contacts ={"Mary":"412-345-5678", 
               "John":"724-789-3456",
               "Susan":"412-555-1212", 
               "Jenny": "724-867-5309", 
               "Emergency":"911", 
               "Prhs": "724-625-4444"}  
    choice = 0
    
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()
    
        # Process the choice.
        if choice == LOOK_UP:
            look_up(contacts)
        elif choice == ADD:
            add(contacts)
        elif choice == CHANGE:
            change(contacts)
        elif choice == list:
            showList(contacts)
        elif choice == DELETE:
            delete(contacts)
    print("Program ending...")

main()

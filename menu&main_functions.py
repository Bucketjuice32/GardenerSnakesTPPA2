

# Global Constants
lookup = 1
add_info = 2
change_info = 3
delete_info = 4
quit_program = 5

# Defining main Function
def main():

    # Constant variable=
    choice = 0

    # Loop to end program depending on choice made
    while choice != quit_program:
        choice = menu_choices()

        # If choice is equal to 1 it calls the lookup function
        if choice == lookup:
            lookup_info()
        # If choice is equal to 2 it calls the add_info function
        elif choice == add_info:
            add_info()
        # If choice is equal to 3 it calls the change_info function
        elif choice == change_info:
            change_info()
        # If choice is equal to 4 it calls the delete_info function
        elif choice == delete_info:
            delete_info()
            
# Defining menu function
def menu_choices():

    # Display menu choices
    print('Menu', '\n--------------------------')
    print('1. Lookup Info')
    print('2. Add Info')
    print('3. Change Info')
    print('4. Delete Info')
    print('5. Quit', '\n--------------------------')
    
    choice = int(input('Enter your choice: '))

    # If choice isn't between paramenter error message
    while choice < lookup or choice > quit_program:

        choice = int(input('Enter a valid choice: '))

    return choice

# Defining lookup function
def lookup_info():

    lookup_choice = 0
    lookup_patient = 1
    lookup_procedure = 2

    print('1. Lookup Patient Info')
    print('2. Lookup Patient Procedure')

    lookup_choice = int(input('Enter Choice: '))

    if lookup_choice == lookup_patient:

    elif lookup_choice == lookup_procedure:
        

# Defining add info functio n 
def add_info():

    add_choice = 0
    add_patient = 1
    add_procedure = 2

    print('1. Add Patient Info')
    print('2. Add Patient Procedure')

    add_choice = int(input('Enter Choice: '))

    if add_choice == add_patient:

    elif add_choice == add_procedure:


# Defining change info function
def change_info():

    change_choice = 0
    change_patient = 1
    change_procedure = 2

    print('1. Change Patient Info')
    print('2. Change Patient Procedure Info')

    change_choice = int(input('Enter Choice: '))

    if change_choice == change_patient:

    elif change_choice == change_patient:
    
# Defining delete info function
def delete_info():

    delete_choice = 0
    delete_patient = 1
    delete_procedure = 2

    print('1. Delete Patient Info')
    print('2. Delete Patient Procedure')

    delete_choice = int(input('Enter Choice: '))

    if delete_choice == delete_patient:


    elif delete_choice == delete_procedure:


# Calling the main function
main()

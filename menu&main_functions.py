

# Global Constants

lookup = 1
add_info = 2
change_info = 3
delete_info = 4
quit_program = 5

    

def main():

    choice = 0

    while choice != quit_program:

        choice = get_menu_choice()

        if choice == lookup:

            print('1. Lookup Patient Info')
            print('2. Lookup Patient Procedure')

        elif choice == add_info:

            print('1. Add Patient Info')
            print('2. Add Patient Procedure')
            
        elif choice == change_info:

            print('1. Change Patient Info')
            print('2. Change Patient Procedure Info')

        elif choice == delete_info:

            print('1. Delete Patient Info')
            print('2. Delete Patient Procedure')

def menu_choices():

    print('Menu', '\n--------------------------')
    print('1. Lookup Info')
    print('2. Add Info')
    print('3. Change Info')
    print('4. Delete Info')
    print('5. Quit', '\n--------------------------')

    choice = int(input('Enter your choice: '))

    if choice == lookup:

        lookup_choice = 0
        lookup_patient = 1
        lookup_procedure = 2

        print('1. Lookup Patient Info')
        print('2. Lookup Patient Procedure')

        lookup_choice = int(input('Enter Choice: '))

    elif choice == add_info:

        add_choice = 0
        add_patient = 1
        add_procedure = 2

        print('1. Add Patient Info')
        print('2. Add Patient Procedure')

        add_choice = int(input('Enter Choice: '))
            
    elif choice == change_info:

        change_choice = 0
        change_patient = 1
        change_procedure = 2

        print('1. Change Patient Info')
        print('2. Change Patient Procedure Info')

        change_choice = int(input('Enter Choice: '))

    elif choice == delete_info:

        delete_choice = 0
        delete_patient = 1
        delete_procedure = 2

        print('1. Delete Patient Info')
        print('2. Delete Patient Procedure')

        delete_choice = int(input('Enter Choice: '))
    
    while choice < lookup or choice > quit_program:

        choice = int(input('Enter a valid choice: '))

    return choice

    


main()

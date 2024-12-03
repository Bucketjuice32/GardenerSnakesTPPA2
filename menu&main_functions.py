import patient_class

patient_manager = patient_class.PatientManager()

# Defining main Function
def main():
    lookup = 1
    add_choice = 2
    change_choice = 3
    delete_choice = 4
    quit_program = 5

    # Constant variable
    choice = 0

    # Loop to end program depending on choice made
    while choice != quit_program:
        choice = menu_choices()

        # If choice is equal to 1 it calls the lookup function
        if choice == lookup:
            lookup_info()
        # If choice is equal to 2 it calls the add_info function
        elif choice == add_choice:
            add_info()
        # If choice is equal to 3 it calls the change_info function
        elif choice == change_choice:
            change_info()
        # If choice is equal to 4 it calls the delete_info function
        elif choice == delete_choice:
            delete_info()
            
# Defining menu function
def menu_choices():
    lookup = 1
    quit_program = 5

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
        name = input("Enter patient's name: ")
        if name in patients:
            print(f"Patient Info for {name}: {patients[name]}")
        else:
            print("Patient not found.")
    elif lookup_choice == lookup_procedure:
        name = input("Enter patient's name to look up procedures: ")
        if name in procedures:
            print(f"Procedures for {name}: {procedures[name]}")
        else:
            print("No procedures found for this patient.")

# Defining add info function 
def add_info():

    add_choice = 0
    add_patient = 1
    add_procedure = 2

    print('1. Add Patient Info')
    print('2. Add Patient Procedure')

    add_choice = int(input('Enter Choice: '))

    if add_choice == add_patient:
        patient1 = patient_class.Patient.input_patient_info
    
    elif add_choice == add_procedure:
        name = input("Enter patient's name to add a procedure: ")
        if name in patients:
            procedure = input("Enter the procedure to add: ")
            if name in procedures:
                procedures[name].append(procedure)
            else:
                procedures[name] = [procedure]
            print(f"Procedure '{procedure}' added for {name}.")
        else:
            print(f"Patient {name} not found.")

# Defining change info function
def change_info():

    change_choice = 0
    change_patient = 1
    change_procedure = 2

    print('1. Change Patient Info')
    print('2. Change Patient Procedure Info')

    change_choice = int(input('Enter Choice: '))

    if change_choice == change_patient:
        pass
    elif change_choice == change_patient:
        pass
    
# Defining delete info function
def delete_info():
    delete_choice = 0
    delete_patient = 1
    delete_procedure = 2

    print('1. Delete Patient Info')
    print('2. Delete Patient Procedure')

    delete_choice = int(input('Enter Choice: '))

    if delete_choice == delete_patient:
        #Get a name to look up.
        name = input('Enter the patient\'s first and last name: ')
        #If the name is found, delete the entry.
        if name in patient:
            del patient[name]
            print('Patient information is deleted.')
        else:
            print('The name is not found.')
        
    elif delete_choice == delete_procedure:
        #Get name to look up procedure
        name = input('Enter the first and last name of the patient: ')
        if name in procedures:
            print(f'The Procedures of {name}: {procedures[name]}')
        #Get procedure
        delete_procedure = input('Enter the procedure to delete: ')
        #If the name is found, delete the entry.
        if delete_procedure in procedures[name]:
            del procedures[name]
            print('Procedure is deleted.')
        else:
            print('The procedure is not found.')

if __name__ == '__main__':
    main()

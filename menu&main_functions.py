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

# Displays patient list and return if patients exist
def display_patient_list():
    print ("\nCurrent Patients:")
    print ("===================")
    patients_exist = False
    try:
        for patient_id, patient in patient_manager.get_all_patients():
            patients_exist = True
            print(f"ID: {patient_id}, Name: {patient.get_full_name()}")
    except Exception as e:
        print (f"Error displaying patients: {e}")

    print ("===================")

    if not patients_exist:
        print ("No Patients in the System.")
    return patients_exist

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
        new_patient = patient_class.Patient()
        new_patient.input_patient_info()
        patient_id = patient_manager.add_patient(new_patient)
        print (f"\nPatient added successfully! ID: {patient_id}")
    
    elif add_choice == add_procedure:
        if display_patient_list():
            try:
                user_id = int(input("\nEnter Patient ID:"))
                patient = patient_manager.get_patient(user_id)
                if patient:
                    new_procedure = patient_class.Procedure()
                    new_procedure.input_procedure_info()
                    if patient.add_procedure(new_procedure):
                        print ("procedure added successfully!")
                else:
                    print("Patient ID not found.")
            except ValueError:
                print("Please enter a valid integer ID.")
        else:
            print ("Please add a patient first.")

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

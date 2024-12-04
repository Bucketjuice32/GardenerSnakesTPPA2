
#Patient class holds data about patients information
class Patient:
    #__init__ method initializes the attributes
    def __init__(self, first_name='', middle_name='', last_name='', address='', city='', state='', zip_code='', number='', emergency_contact='', emergency_number=''):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__number = number
        self.__emergency_contact = emergency_contact
        self.__emergency_number = emergency_number
        self.__procedures = []
        
    #Input procedure       
    def input_patient_info() :
        return Patient(
        input('Enter the first name: '),
        input('Enter the middle name: '),
        input('Enter the last name: '),
        input('Enter the address: '),
        input('Enter the city: '),
        input('Enter the state: '),
        input('Enter the zipcode: '),
        input('Enter the phone number: '),
        input('Enter the emergency contact: '),
        input('Enter the emergency contact number: '))

    #Output procedure
    def output_patient_info(self):
        return((f'First Name:', f'{self.get_first_name()}'), 
        (f'Middle Name:', f'{self.get_middle_name()}'),
        (f'Last Name: ', f'{self.get_last_name()}'),
        (f'Address: ', f'{self.get_address()}'),
        (f'City: ',f'{self.get_city()}'),
        (f'State: ',f'{self.get_state()}'),
        (f'Zip Code:', f'{self.get_zip_code()}'),
        (f'Phone Number:', f'{self.get_number()}'),
        (f'Emergency Contact: ',f'{self.get_emergency_contact()}'),
        (f'Emergency Contact Number: ',f'{self.get_emergency_number()}'))             

    #Mutator method accepts the arguments for each attribute
    def set_first_name(self, first_name):
        self.__first_name = first_name
        
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_number(self, number):
        self.__number = number

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    def set_emergency_number(self, emergency_number):
        self.__emergency_number = emergency_number

    #Accessor method returns the attributes
    def get_first_name(self):
        return self.__first_name
    def get_middle_name(self):
        return self.__middle_name
    def get_last_name(self):
        return self.__last_name
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zip_code(self):
        return self.__zip_code
    def get_number(self):
        return self.__number
    def get_emergency_contact(self):
        return self.__emergency_contact
    def get_emergency_number(self):
        return self.__emergency_number
    def get_procedures(self):
        return self.__procedures.items()

#Procedure class holds data about procedure information
class Procedure:
    #__init__ method initializes the attributes
    def __init__(self, procedure='', date='', practitioner='', charge=''):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        self.__id = 1

    #Creates procedure instance
    def input_procedure_info():
        return Procedure(
        input('Enter the procedure: '),
        input('Enter the date: '),
        input('Enter the practitioner: '),
        input('Enter the charge: '))

    #Output procedure
    def output_procedure_info(self):
        return((f'Procedure: ',f'{self.get_procedure()}'),
        (f'Date: ', f'{self.get_date()}'),
        (f'Practitioner: ', f'{self.get_practitioner()}'),
        (f'Charge: ', f'{self.get_charge()}'))
  

    #Mutator method accepts the arguments for each attribute

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner

    def set_charge(self, charge):
        self.__charge = charge

    #Accessor method returns the attributes
    def get_procedure(self):
        return self.__procedure
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_charge(self):
        return self.__charge
    def get_first_name(self):
        return self.__first_name
    def get_id(self):
        return self.__id

def main():
    lookup = 1
    add_choice = 2
    change_choice = 3
    delete_choice = 4
    quit_program = 5
    # Constant variable
    choice = 0
    patient_list = {}
    patient_id = 1

    # Loop to end program depending on choice made
    while choice != quit_program:
        choice = menu_choices()

        # If choice is equal to 1 it calls the lookup function
        if choice == lookup:
            lookup_info()
        # If choice is equal to 2 it calls the add_info function
        elif choice == add_choice:
            patient_id = add_info(patient_list, patient_id)
            patient_id = patient_id       
        # If choice is equal to 3 it calls the change_info function
        elif choice == change_choice:
            change_info()
        # If choice is equal to 4 it calls the delete_info function
        elif choice == delete_choice:
            delete_info()

# Displays list of Patient by ID & First Name
def patient_display(patient_dict):
    if not patient_dict:  # checks if dictionary is empty
        print("\nNo patients in the system.")
        return False
    print("\nList of Patients:")
    print("-----------------")
    for patient_id, patient_info in patient_dict.items():
        print(f"ID: {patient_id} - First Name: {patient_info['First Name:']}")
    print("-----------------")

# Defining menu function
def menu_choices():
    lookup = 1
    quit_program = 5

    # Display menu choices
    print('Menu', '\n--------------------------')
    print('1. Lookup Info')
    print('2. Add Info')
    print('5. Quit Program')
 
    
    choice = int(input('Enter your choice: '))

    # If choice isn't between paramenter error message
    while choice < lookup or choice > quit_program:

        choice = int(input('Enter a valid choice: '))

    return choice


# Defining add info function 
def add_info(patient_list, patient_id):

    add_choice = 0
    add_patient = 1
    add_procedure = 2


    print('1. Add Patient Info')
    print('2. Add Patient Procedure')

    add_choice = int(input('Enter Choice: '))

    if add_choice == add_patient:
        while True:
            Input_Patient = Patient.input_patient_info()
            Output_Patient = Input_Patient.output_patient_info()
            patient_info = dict((x,y) for x, y in Output_Patient)
            patient_list[patient_id] = patient_info
            name = patient_list[patient_id]["First Name:"]
            patient_list[patient_id]["Procedures:"] = []
            print(end='\n')
            print(f"Patient info for {name} added successfully with ID: {patient_id}")
            patient_id += 1
            print (patient_list)
            print(end='\n')
            cont = input('Do you want to add another person? (yes/no): ').lower()
            if cont != 'yes':
                break
            else:
                Input_Patient = Patient.input_patient_info()
                Output_Patient = Input_Patient.output_patient_info()
                patient_info = dict((x,y) for x, y in Output_Patient)
                patient_list [patient_id] = patient_info
                name = patient_list[patient_id]["First Name:"]
                patient_list[patient_id]["Procedures:"] = []
                print(end='\n')
                print(f"Patient info for {name} added successfully with ID: {patient_id}")
                patient_id += 1
                print(patient_list)
                cont = input('Do you want to add another person? (yes/no): ').lower()
                if cont != 'yes':
                    break                
    if add_choice == add_procedure:
        while True:
            if patient_display(patient_list) == False:
                print (f"Add a patient.")
                break 
            selection = int(input("Which patient would you like to add a procedure to? Select ID: "))
            Input_Procedure = Procedure.input_procedure_info() 
            Output_Procedure = Input_Procedure.output_procedure_info() 
            procedure_info = dict((x,y) for x, y in Output_Procedure)
            patient_list[selection]["Procedures:"].append(procedure_info)
            print (patient_list)
            print (len(patient_list[selection]["Procedures:"]))
            print(end='\n')
            print(f"Procedure info for  added successfully.")
            print(end='\n')
            cont = input('Do you want to add another procedure? (yes/no): ').lower()
            if cont != 'yes':
                break     
            else:
                Input_Procedure = Procedure.input_procedure_info() 
                Output_Procedure = Input_Procedure.output_procedure_info() 
                procedure_info = dict((x,y) for x, y in Output_Procedure)
                patient_list[selection]["Procedures:"].append(procedure_info)
                print (patient_list)
                print(end='\n')
                print(f"Procedure info for  added successfully.")
                print(end='\n')
                cont = input('Do you want to add another procedure? (yes/no): ').lower()
                if cont != 'yes':
                    break     
    return patient_id


if __name__ == '__main__':
    main()
    

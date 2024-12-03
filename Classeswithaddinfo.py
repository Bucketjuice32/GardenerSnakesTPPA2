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

#Procedure class holds data about procedure information
class Procedure:
    #__init__ method initializes the attributes
    def __init__(self, procedure='', date='', practitioner='', charge='',first_name=''):
        self.__first_name = first_name
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    #Input procedure
    def input_procedure_info():
        return Procedure(
        input('Enter the first name: '),
        input('Enter the procedure: '),
        input('Enter the date: '),
        input('Enter the practitioner: '),
        input('Enter the charge: '))

    #Output procedure
    def output_procedure_info(self):
        return((f'First Name:', f'{self.get_first_name()}'),
        (f'Procedure: ',f'{self.get_procedure()}'),
        (f'Date: ', f'{self.get_date()}'),
        (f'Practitioner: ', f'{self.get_practitioner()}'),
        (f'Charge: ', f'{self.get_charge()}'))
                    

    #Mutator method accepts the arguments for each attribute
    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner

    def set_charge(self, charge):
        self.__charge = charge
        
    def set_first_name(self, first_name):
        self.__first_name = first_name

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


# Defining add info function 
def add_info():

    add_choice = 0
    add_patient = 1
    add_procedure = 2

    print('1. Add Patient Info')
    print('2. Add Patient Procedure')

    add_choice = int(input('Enter Choice: '))

    if add_choice == add_patient:
        #creates an instance for patient
        Input_Patient = Patient.input_patient_info()
        #outputs the input for the pateint into a tuple
        Output_Patient = Input_Patient.output_patient_info()
        #Stores tuple into a dictionary
        Dictionary = dict((x,y) for x, y in Output_Patient)
        print(end='\n')
        print(f"Patient info for {Dictionary['First Name:']} added successfully.")
        print(end='\n')
    if add_choice == add_procedure:
        #creates an instance for patient
        Input_Procedure = Procedure.input_procedure_info()
        #outputs the input for the procedure into a tuple
        Output_Procedure = Input_Procedure.output_procedure_info()
        #stores tuple into a dictionary
        Dictionary = dict((x,y) for x, y in Output_Procedure)
        print(end='\n')
        print(f"Procedure info for {Dictionary['First Name:']} added successfully.")
        print(end='\n')
               


if __name__ == '__main__':
    main()
    

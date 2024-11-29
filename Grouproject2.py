#Patient class holds data about patients information
class Patient:
    #__init__ method initializes the attributes
    def __init__(self, first_name=None, middle_name=None, last_name=None, address=None, city=None, state=None, zip_code=None, number=None, emergency_contact=None, emergency_number=None):
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
    def input_patient_info(self) :
        self.__first_name = input('Enter the first name: ')
        self.__middle_name = input('Enter the middle name: ')
        self.__last_name = input('Enter the last name: ')
        self.__address = input('Enter the address: ')
        self.__city = input('Enter the city: ')
        self.__state = input('Enter the state: ')
        self.__zip_code = input('Enter the zipcode: ')
        self.__number = input('Enter the phone number: ')
        self.__emergency_contact = input('Enter the emergency contact: ')
        self.__emergency_number = input('Enter the emergency contact number: ')

    #Output procedure
    def output_patient_info(self):
        print(end='\n')
        print(f'First Name: {self.get_first_name()}')
        print(f'Middle Name: {self.get_middle_name()}')
        print(f'Last Name: {self.get_last_name()}')
        print(f'Address" {self.get_address()}')
        print(f'City: {self.get_city()}')
        print(f'State: {self.get_state()}')
        print(f'Zip Code: {self.get_zip_code()}')
        print(f'Phone Number: {self.get_number()}')
        print(f'Emergency Contact: {self.get_emergency_contact()}')
        print(f'Emergency Contact Number: {self.get_emergency_number()}')
             

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
    def __init__(self, procedure=None, date=None, practitioner=None, charge=None):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
    #Input procedure
    def input_procedure_info(self):
        print(end='\n')
        self.__procedure = input('Enter the procedure: ')
        self.__date = input('Enter the date: ')
        self.__practitioner = input('Enter the practitioner: ')
        self.__charge = input('Enter the charge: ')

    #Output procedure
    def output_procedure_info(self):
        print(end='\n')
        print(f'Procedure: {self.get_procedure()}')
        print(f'Date: {self.get_date()}')
        print(f'Practitioner: {self.get_practitioner()}')
        print(f'Charge: {self.get_charge()}')
                    

    #Mutator method accepts the arguments for each attribute
    def set_procedure(self, procedure):
        self.__procedure = procedure

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

def main():

    #Creating an instance for patient
    The_Patient = Patient()
    The_Patient.input_patient_info()
    The_Patient.output_patient_info()

    #Creating an instance for three procedures
    The_Procedure1 = Procedure()
    The_Procedure2 = Procedure()
    The_Procedure3 = Procedure()
    
    The_Procedure1.input_procedure_info()
    The_Procedure1.output_procedure_info()
    
    The_Procedure2.input_procedure_info()
    The_Procedure2.output_procedure_info()
    
    The_Procedure3.input_procedure_info()
    The_Procedure3.output_procedure_info()
                     

if __name__ == '__main__':
    main()
    


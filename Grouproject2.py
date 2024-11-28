#Patient class holds data about patients information
class Patient:
    #__init__ method initializes the attributes
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, number, emergency_contact, emergency_number):
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
    def __init__(self, procedure, date, practitioner, charge):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

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
    #patient
    firstname = input('Enter the first name: ')
    middlename = input('Enter the middle name: ')
    lastname = input('Enter the last name: ')
    address = input('Enter the adress: ')
    city = input('Enter the city: ')
    state = input('Enter the state: ')
    zipcode = input('Enter the zipcode: ')
    number = input('Enter the phone number: ')
    emergencycontact = input('Enter the emergency contact number: ')
    emergencycontactnumber = input('Enter the emergency contactnumber: ')


    #procedure
    the_procedure = input('Enter the procedure: ')
    the_date = input('Enter the date: ')
    the_practitioner = input('Enter the practitioner: ')
    the_charge = input('Enter the charge: ')
    
    #Creates an instance for patient
    P = Patient(firstname, middlename,lastname, address, city, state, zipcode, number, emergencycontact, emergencycontactnumber)   
    print(P.get_first_name())
    print(P.get_middle_name())
    print(P.get_last_name())
    print(P.get_address())
    print(P.get_city())
    print(P.get_state())
    print(P.get_zip_code())
    print(P.get_number())
    print(P.get_emergency_contact())
    print(P.get_emergency_number())

    #creates an instance for procedure
    The_Procedure = Procedure(the_procedure,the_date,the_practitioner,the_charge)
    print(The_Procedure.get_procedure())
    print(The_Procedure.get_date())
    print(The_Procedure.get_practitioner())
    print(The_Procedure.get_charge())
                     

if __name__ == '__main__':
    main()
    


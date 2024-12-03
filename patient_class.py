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
        self.__procedures = []
        self.__next_procedure_id = 1
        

    def add_procedure(self, procedure):
        # Adds procedure to this patient's record
        if isinstance(procedure, Procedure):
            procedure.set_id(self.__next_procedure_id)
            self.__procedures.append(procedure)
            self.__next_procedure_id += 1
            return True
        return False

    def get_procedures(self):
        # Returns list of all procedures
        return self.__procedures

    def remove_procedure(self, procedure_id):
        # Remove a procedure by ID
        for procedure in self.__procedures:
            if procedure.get_id() == procedure_id:
                self.__procedures.remove(procedure)
                print (f"Procedure Removed Successfully!")
                return True
        return False

    def get_full_name(self):
        return f"{self.__first_name} {self.__middle_name} {self.__last_name}".strip()

    #Input Patient Info      
    def input_patient_info(self):

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
        
        while True:
            add_procedure = input("\nWould you like to add a procedure? (yes/no): ").lower()
            if add_procedure == 'yes':
                new_procedure = Procedure()
                new_procedure.input_procedure_info()
                self.add_procedure(new_procedure)
                continue_adding = input("Add another procedure? (yes/no): ").lower()
                if continue_adding != 'yes':
                    break
            else:
                break
        return self

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
        
        if self.__procedures:
            print("\nProcedures:")
            for procedure in self.__procedures:
                print ("\n============")
                procedure.output_procedure_info()

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
    def __init__(self, procedure_name=None, date=None, practitioner=None, charge=None):
        self.__id = None
        self.__procedure_name = procedure_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    #Input procedure
    def input_procedure_info(self):
        print(end='\n')
        self.__procedure_name = input('Enter the procedure: ')
        self.__date = input('Enter the date: ')
        self.__practitioner = input('Enter the practitioner: ')
        self.__charge = input('Enter the charge: ')

        return self

    #Output procedure
    def output_procedure_info(self):
        print(end='\n')
        print(f"Procedure ID: {self.get_id()}")
        print(f'Procedure: {self.get_procedure_name()}')
        print(f'Date: {self.get_date()}')
        print(f'Practitioner: {self.get_practitioner()}')
        print(f'Charge: {self.get_charge()}')
                    

    #Mutator method accepts the arguments for each attribute
    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charge(self, charge):
        self.__charge = charge
    
    def set_id(self, id):
        self.__id = id

    #Accessor method returns the attributes
    def get_procedure_name(self):
        return self.__procedure_name
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_charge(self):
        return self.__charge
    def get_id(self):
        return self.__id

# Manages the data of Patient Class
class PatientManager:
    def __init__(self):
        self.__patients = {}
        self.__next_id = 1
    
    def add_patient(self, patient):
        if isinstance(patient, Patient):
            patient_id = self.__next_id
            self.__patients[patient_id] = patient
            self.__next_id += 1
            return patient_id
        return None
    def get_patient(self, patient_id):
        return self.__patients.get(patient_id)
    
    # def find_patient_by_name(self, full_name):
    #     for patient_id, patient in self.__patients.items():
    #         if patient.get_full_name().lower() == full_name.lower():
    #             return patient_id, patient
    #     return None, None
    
    def delete_patient (self, patient_id):
        if patient_id in self.__patients:
            del self.__patients[patient_id]
            return True
        return False
    def get_all_patients(self):
        return self.__patients.items()


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
    


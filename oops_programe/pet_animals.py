class Bank1:
    def __init__(self, b_name, b_loc):
        self.b_name = b_name
        self.b_loc = b_loc

    def b_info(self):
        print('BANK_DETAILS =', self.b_name, self.b_loc)

class Bank_person(Bank1):
    def __init__(self, name, acc_no, phone_no, b_name, b_loc):
        # Call the __init__ method of the parent class (Bank1)
        super().__init__(b_name, b_loc)

        self.name = name
        self.acc_no = acc_no
        self.phone_no = phone_no

    def person_info(self):
        print('PERSONAL DETAILS =', self.name, self.acc_no, self.phone_no)

# Create an instance of Bank1
bank_obj = Bank1('SBI', 'CHENNAI')

# Create an instance of Bank_person
person_obj = Bank_person('Gopi', 100002233444, 8838935551, 'SBI', 'CHENNAI')

# Call the b_info method on the bank_obj
bank_obj.b_info()

# Call the person_info method on the person_obj
person_obj.person_info()

# Call the b_info method on the person_obj (which inherits it from Bank1)
person_obj.b_info()

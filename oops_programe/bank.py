class Bank1:
    def __init__(self, b_name, b_loc):
        self.b_name = b_name
        self.b_loc = b_loc

    def b_info(self):
        print('BANK_DETAILS =', self.b_name, self.b_loc)

class Bank_person(Bank1):
    def __init__(self, name, acc_no, phone_no, b_name, b_loc):
        super().__init__(b_name, b_loc)
        self.name = name
        self.acc_no = acc_no
        self.phone_no = phone_no

    def person_info(self):
        super().b_info()  # Corrected this line
        print('PERSONAL DETAILS =', self.name, self.acc_no, self.phone_no, self.b_name, self.b_loc)

bank_obj = Bank1('SBI', 'CHENNAI')


person_obj = Bank_person('Gopi', 100002233444, 8838935551, 'SBI', 'CHENNAI')

bank_obj.b_info()

person_obj.person_info()

person_obj.b_info()

class Insurance(Bank1):
    def __init__(self,name,ins_amount,b_name, b_loc):
        super().__init__(b_name, b_loc)
        self.name=name
        self.ins_amount=ins_amount

    def insurance_detials(self):
        super().b_info()
        print('insurance detials =', self.b_name,self.b_loc, self.name ,self.ins_amount)

ins_person = Insurance('Gopi',450000,'SBI','CHENNAI')

ins_person.insurance_detials()












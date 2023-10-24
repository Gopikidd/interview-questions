class Ktm:
    def __init__(self, name, cc, price):
        self.name = name
        self.cc = cc
        self.price = price

    def bike_info(self):
        print('BIKE DETAILS =', self.name, self.cc, self.price)

class Customer(Ktm):
    def __init__(self, c_name, amount, name, cc, price):
        super().__init__(name, cc, price)
        self.c_name = c_name
        self.amount = amount

    def c_details(self):
        super().bike_info()
        print('CUSTOMER DETAILS =', self.c_name, self.amount, self.name, self.cc, self.price)

class Loan(Customer):
    def __init__(self, c_name, amount, name, cc, price, balance = 0):
        super().__init__(c_name, amount, name, cc, price)  # Corrected the order of parameters
        self.balance=balance


    def loan_balance(self):
        super().c_details()
        print('LOAN AMOUNT =', self.balance)

brand = Ktm('DUKE', 390, 350000)
#brand.bike_info()

cust1 = Customer('Gopi', 150000, 'DUKE', 390, 350000)
#cust1.c_details()

due_amount = Loan('Gopi', 350000, 'DUKE',390, 350000)
due_amount.loan_balance()

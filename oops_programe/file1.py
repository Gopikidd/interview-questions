class Food:
    hotel_name = 'Ambur Hotel'
    loc  = 'chennai'
    def __init__(self, food1, food2, food3):
        self.food1 = food1
        self.food2 = food2
        self.food3 = food3

    def get_info(self):
        print("food detials =", self.food1, self.food2, self.food3)

    @classmethod
    def address(cls):
        print(cls.hotel_name, cls.loc)

    @classmethod
    def update(cls, val):
        cls.hotel_name = val

obj=Food('dosa ,','poori ,','pongal')

obj.get_info()

Food.address()

Food.update('SALEM_RR')

Food.address()



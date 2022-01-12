class Foo:
    @classmethod  #Used when the created objects will need the class during instantiation
    def hi(cls): #Method starts with the class Foo as its only parameter
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod #Used when consructed objects need no paramets.
    def hi():
        print('Hello, I don\'t take any parameters.')


another_object = Bar()
another_object.hi()

print('_______________________________________________________________________')

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)



number = FixedFloat(18.5746)
print(number)
new_number = number.from_sum(19.575, 0.789)
print (new_number)

### **^^Don't like the above from_sum method.  Lets make it a static method instead...


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod  #Staticmethod changed to classmethod after writing Euro object...
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)
    # ^Declaring this a static method means we remove **self** and then we can call the method from the class.

new_new_number = FixedFloat.from_sum(342.69, 12.21)
print(new_new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "E"

        def __repr__(self):
            return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro.from_sum(18.781, 119.996)
print(money)





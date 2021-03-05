# Calculate the Actual Price
def actual_price(base_price):
    return base_price * 1.25

# Property is created to mask the class attribute from outside the class
# Property helps handle the manipulation of the class attribute, set value, get value , delete value
# Class attribute is typically initialized within the __init__ method.
# Property name is same as class attribute defined in the __init__ method.
# Once the property is defined, the getter and setter, etc methods can be defined
# @propertyname.setter => will be invoked whenever a value is assigned to class attribute
# @propertyname.getter => will be invoked when the class attribute is to be retrieved


class Products:
    # Initialize the Products Class
    def __init__(self, pid, name, base_price=0):
        self.special_price = base_price
        self._pid = pid
        self._name = name
        self.price = base_price

    # **************************************************
    # Define the property for the class attribute: price
    # **************************************************
    @property
    def price(self):
        print('Entering the Price property definition')
        return self._price

    # ***************************************
    # Set the value to class attribute: price
    # ***************************************
    @price.setter
    def price(self, base_price):
        print('Entering the Price property setter method')
        if not isinstance(base_price, int):
            raise TypeError('Product Price is expected to be Integer value')
        if base_price < 0:
            raise ValueError('Product price cannot be Negative')
        self._price = actual_price(base_price)

    # ********************************************
    # Retrieve the value of class attribute: price
    # ********************************************
    @price.getter
    def price(self):
        print('Entering the Price property getter method')
        return self._price

    @property
    def special_price(self):
        return self._special_price

    # **********************************************************
    # Set the value to class attribute: special_price
    # **********************************************************
    @special_price.setter
    def special_price(self, base_price):
        print('Entering the Special Price property setter method')
        if not isinstance(base_price, int):
            raise TypeError('Product Price is expected to be Integer value')
        if base_price < 0:
            raise ValueError('Product price cannot be Negative')
        self._special_price = base_price * 1.5


if __name__ == '__main__':
    p1 = Products(1, 'drink', 5)
    # price = p1.get_price
    print(p1.price)
    print(p1.special_price)
    p1.price = 10
    print(p1.price)
    p2 = Products(2, 'small_drink', -1)
    print(p2.price)
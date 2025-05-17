from Customer import Customer
from Coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price should be float")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self)
        
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
   
    @property
    def price(self):
       return self._price
    
    @price.setter
    def price(self,_):
        raise AttributeError("Cannot modify the price once initialized!")
    


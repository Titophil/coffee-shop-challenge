from Order import Order

class Coffee:
    all = []

    def __init__(self,name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string and should be greater than 3 characters")
        Coffee.all.append(self)
    
    def orders(self):
        return[order for order in Order.all if order.coffee == self]
        
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        coffee_orders = self.orders()
        if not coffee_orders:
            return 0
        total = sum(order.price for order in coffee_orders)
        return  total/len(coffee_orders)
    
    def customers(self):
        return list({order.customer for order in self.orders()})


    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,_):
        raise AttributeError("Cannot change name after initialization")

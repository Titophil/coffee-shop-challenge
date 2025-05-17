from Order import Order
class Customer:

    def __init__(self,name):
        self.name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string")
    def create_order(self,coffee,price):
        return Order(self,coffee,price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_order_counts = {}

        for order in Order.all:
            if order.coffee == coffee:
                customer = order.customer
                customer_order_counts[customer]=customer_order_counts.get(customer,0)+1

        if not customer_order_counts:
           return None
            
        return max(customer_order_counts, key = customer_order_counts.get)


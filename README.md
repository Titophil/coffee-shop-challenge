☕ Coffee Shop Object Relationships
A simple Python OOP system modeling a coffee shop's data using three main classes: Customer, Coffee, and Order. The program establishes and manages relationships between these entities, mimicking real-world interactions in a coffee ordering system.

📦 Classes Overview
✅ Customer
Represents a customer who can place orders for coffee.

Attributes
name (string, 1–15 characters): The name of the customer. Validated and stored immutably.

Methods
orders(): Returns a list of all Order instances for this customer.

coffees(): Returns a unique list of Coffee instances this customer has ordered.

create_order(coffee, price): Creates a new Order with this customer.

most_aficionado(coffee): Class method that returns the customer who ordered a specific coffee the most.

✅ Coffee
Represents a type of coffee that can be ordered by customers.

Attributes
name (string, 3+ characters): The name of the coffee. Immutable after initialization.

Methods
orders(): Returns a list of all Order instances for this coffee.

customers(): Returns a unique list of customers who have ordered this coffee.

num_orders(): Returns the number of times this coffee has been ordered.

average_price(): Returns the average price of all orders for this coffee.

✅ Order
Represents an order made by a customer for a coffee at a specific price.

Attributes
customer: A Customer instance.

coffee: A Coffee instance.

price (float, 1.0–10.0): Price of the coffee. Immutable after creation.

Class Attributes
Order.all: Class-level list containing all orders created.

🧠 Features
Enforces data integrity using custom type and value validations.

Establishes:

One-to-many relationship between Customer and Order.

One-to-many relationship between Coffee and Order.

Many-to-many relationship between Customer and Coffee via Order.

Supports aggregate calculations like total orders and average coffee price.

Identifies the most frequent customer for a specific coffee via Customer.most_aficionado(coffee).

✅ Example Usage
from Customer import Customer
from Coffee import Coffee
from Order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 5.0)
bob.create_order(latte, 6.0)
alice.create_order(espresso, 4.5)

print(latte.num_orders())  # 2
print(latte.average_price())  # 5.5
print(Customer.most_aficionado(latte))  # Alice or Bob (if tied)

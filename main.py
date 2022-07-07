class Product:
    def __init__(self, name, size, colour, price):
        self.name = name
        self.size = size
        self.colour = colour
        self.price = price
    def __str__ (self):
        return "Product [name={} size={}, colour={}, price={}]"
dress = ("Dress", "M", "Red", "20$")
tshirt = ("T-shirt", "S", "Black", "7$")
jeans = ("Jeans", "M", "Blue", "32$")
print(dress, tshirt, jeans, sep="\n")

class Customer:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
    def __str__(self):
        return "name={}, surname={}, age={}, phone_number={}"
customer_1 = ("Ivan", "Ivanov", 37, 123456789)
customer_2 = ("Mary", "Honcharova", 23, 987654321)
print(customer_1, customer_2, sep="\n")

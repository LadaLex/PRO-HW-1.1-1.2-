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
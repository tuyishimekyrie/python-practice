# to define the name of class , you should use PascalCase naming convention
class Point:
    default_color = "yellow"
    
    # This is a magic method, every method inside a class should have self as a parameter
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @classmethod
    def zero(cls):
        return cls(0,0)
    
    def __str__(self):
        return f'({self.x},{self.y})'
        
    def draw(self):
        return f"Point ({self.x},{self.y})"

# point = Point(1,2)
# print(point.y)
# print(point.draw())
# print(point.default_color)
# point = Point(12,13)
# point.zero()
# print(point)

class Product:
    
    def __init__(self,price):
        self.price = price
    
    def __getstate__(self):
        return self.__price
    
    def __str__(self):
        return f'{self.__price}'
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,price):
        self.__price = price
    
    # property(get_price,set_price)

product = Product(100)
# product.__price = 1000
# product.set_price(1000)
product.price = 1000
# print(product.price)
print(str(product))
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
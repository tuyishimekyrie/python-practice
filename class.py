class Point:
    default = 0;
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    
    @classmethod    
    def zero(cls):
        return cls(0,0);
        
    def draw(self):
        print(f"point({self.x},{self.y})");
        
point = Point(1,2);
Point.default = 10;
print(Point.default);
print(type(point));
print(isinstance(point,Point));
point.draw();
Point.zero();
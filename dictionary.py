point = {"x":1,"y":2};
data = dict(x=1,y=2);
print(point);
print(data);

print(data.get("x"))

for item,v in data.items():
    print(item,v)
    
numbers = {item:data[item] for item in data}
print(numbers)
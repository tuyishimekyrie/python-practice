message = list("hello");
total = [0]*5 + message;

# print(total);

numbers = list(range(20));

# print(numbers[::-1])

bank = [1,2,3,4,5,6,7,8,9,10];
first,second,*other = bank;

# print(first)
# print(second)
# print(other)

colors = ["red","green","blue"];

# for index,color in enumerate(colors):
 # print(f'{index}:{color}');
# for color in colors:
        # print(color)
    
colors.append("yellow");


# colors.pop(0);
# colors.insert(0,"black");
# colors.remove("green");
# del colors[0 : 2];
# colors.clear();
# print(colors.index("blue"));
# print(colors.count("yellow"))

items = [
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]

def sort_item(item):
    return item[1];

# items.sort(key=lambda item:item[1]))
# items.sort(key=sort_item)
# prices = list(map(lambda item:item[1],items))
# print(prices);

# print(sorted(colors,reverse=True));

prices = list(map(lambda item:item[1],items));
prices = [item[1] for item in items];
# print(prices);

filtered = list(filter(lambda item:item[1] >= 10, items));
filtered = [item for item in items if item[1] >= 10];
# print(filtered);
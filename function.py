def increment(number:int,by:int) -> int:
    return number + by;

# print(increment(2.3,3));

def multiply(*list):
    total = 1
    for number in list:
        total *= number;
        return total;

# print(multiply(2,3,4,5,6,7,8,9,10));

def save_user(**user):
    print(user["id"]);
    
save_user(id=1,name="John",age=22);
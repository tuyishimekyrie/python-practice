age = 18;
if(age >= 18):
    print("You are an adult");
elif(age >= 13):
    print("You are a teenager");
else:
    print("You are a child");

message = "Eligible" if age >= 18 else "Not eligible"

print(message);

for name in "python":
    print(name);

for number in [1,2,3,4,5]:
    print(number);

for all in range(5):
    print(all);


names = ["John", "Mary", "Bob", "Mosh"];

for name in names:
    if(name.startswith("J")):
        print("Found");
        found = "true";
        break;
else:
    print("Not Found");


guess = 0;
answer = 5;

while answer != guess:
    guess = int(input("Guess: "));

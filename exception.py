from timeit import timeit
code = """
try:
  with  open("app.py") as file:
      print("File opened");0
  age = int(input("Enter your age: "));
  total = 0 / age;
except (ValueError,ZeroDivisionError):
  print("You didn't enter a valid age.");
else:
    print("You are eligible to play the game");
"""

print(timeit(code,number=10));
# finally:
#     file.close();
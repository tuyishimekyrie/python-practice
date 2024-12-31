def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

# print(fizz_buzz(15))

sentence = "This is a common interview question";
char_frequency = {}
for char in sentence:
        if char in char_frequency:
             char_frequency[char] += 1;
        else:
             char_frequency[char] = 1;
char_frequency = sorted(char_frequency.items(),key=lambda kv:kv[1],reverse="True")
print(char_frequency[0][0]);             




# number = int(input("What's your number: "))

# # if number < 0:
# #     print("I am negative")
# # elif number == 0:
# #     print("I am zero")
# # else:
# #     print("I am positive")

# if number%2==0:
#     print("Even")
# else:
#     print("Odd")

for number in range(30):
    if number%15 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)

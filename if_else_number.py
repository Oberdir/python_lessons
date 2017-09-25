# 25.09.2017 -- Kevin Akpomuje
# Ask user to input a number
print("Please enter a postive / negative whole number: ")
x = input()
number_x = int(x)
print("Your number is: ", number_x)

if number_x > 0:
    print("This number is positive")
elif number_x == 0:
    print("Your number is zero")
else:
    print("Your number is negative")

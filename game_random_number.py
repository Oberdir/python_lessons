# 25.09.2017 -- Kevin Akpomuje
# Import the modul: random
import random

# Initialize the random modul
random.seed()

# Random number generation and some basic calculation
a = random.randint(1,100)
b = random.randint(1,100)
c = a + b
print("Calculation: ", a, "+", b)

# Input
print("Please enter a number: ")
z = input()
number = int(z)

# Output
print("You entered: ", z)
print("The result: ", c)

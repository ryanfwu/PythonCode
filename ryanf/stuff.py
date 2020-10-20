# Imports
import time
import math

# Print text
print("this is a demo")

# User input
userinput = input("type some input: ")

# If/else
if (userinput == ""):
  print("you typed nothing")
else:
  print("you typed '" + userinput + "'")

# For
print("numbers from 1 to 9")
for x in range(1,10):
  print("- " + x)

# Arithmetic
a = 1
b = 1
sum = a + b
diff = a - b
absdiff = math.abs(diff)
product = a * b
sqrtproduct = math.sqrt(product)
quotient = a / b
exponent = a ** b
modulo = a %% b


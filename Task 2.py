# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
import math

num = float(input("Enter a number: "))
sqrt = math.sqrt(num)
log = math.log(num)
sin = math.sin(num)
print("Square root:", sqrt)
print("Natural logarithm:", log)
print("Sine:", sin)


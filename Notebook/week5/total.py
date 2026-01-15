"""total.py
Usage: python total.py num1 num2 ...
"""

import sys

# Count command-line arguments (script name is included)
count = len(sys.argv)

# Initialize running total and compute how many numeric values were passed
total = 0.0
num_values = count - 1  # excludes the script name

# Walk through the arguments from last to first and accumulate their numeric values
while count > 1:
    count -= 1
    total += float(sys.argv[count])

# If we received any numeric arguments, print total and average; otherwise show a message
if num_values > 0:
    average = total / num_values
    print("Total is", total)
    print("Average is", average)
else:
    print("no arguments were provided")

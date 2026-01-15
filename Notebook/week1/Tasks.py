#TASK: First Code Execution
print("the program has executed")

# TASK: Alternative Messages
print("This is the Second message")
print("This is the Third message")
print("This is the Fourth message")

#TASK: Using Command History 
print("This is the Second message")

#TASK: Entering Basic Expressions
print("45 + 20 =", 45 + 20)

#TASK: Common Operators
print("10 + 20 - 15 =", 10 + 20 - 15)
print("10 * 5 =", 10 * 5)
print("100 / 33 =", 100 / 33)       
print("100 // 33 =", 100 // 33)    
print("10 ** 2 =", 10 ** 2)         
print("10 % 3 =", 10 % 3)           

#TASK: Operator Precedence
print("10 + 5 * 2 =", 10 + 5 * 2)
print("10 - 5 * 10 + 5 =", 10 - 5 * 10 + 5)
print("5 * 10 ** 2 =", 5 * 10 ** 2)

#TASK: Operator Precedence with Parentheses
print("(10 + 5) * 2 =", (10 + 5) * 2)
print("10 - 5 * (10 + 5) =", 10 - 5 * (10 + 5))
print("(5 * 10) ** 2 =", (5 * 10) ** 2)

#TASK: Nested Parentheses
print("12 + (5 * 2 + 3) =", 12 + (5 * 2 + 3))
print("12 + (5 * (2 + 3)) =", 12 + (5 * (2 + 3)))

#TASK: Handling Errors
try:
    print("Ten divided by zero is", 10/0)
except ZeroDivisionError as e:
    print("Error encountered:", e)

# TASK:
total = 100
print("The total is", total)

# TASK:
total = total + 99
print("The total is now", total)

# TASK:
total = 100  
total += 99
print("The total (using +=) is now", total)

# TASK:
total -= 1
print("The total is", total)

total *= 4
print("The total is", total)

total /= 2
print("The total is", total)

# TASK: 
total = 98.2
count = 5
average = total / count
print("The average is", average)


print("\nSECTION: DATA-TYPES")

total = 10
print("Type of total (int):", type(total))
total = 10.5
print("Type of total (float):", type(total))
total = "10.5"
print("Type of total (string):", type(total))

# TASK:
print("Type of False:", type(False))
print("Type of 1000:", type(1000))
print("Type of 100.111:", type(100.111))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))
print("Type of 100 / 5:", type(100 / 5))
print("Type of 100 // 5:", type(100 // 5))
print("10 + 10 result:", 10 + 10)
print("'10' + '10' result:", "10" + "10")

# TASK:
print("'ABC' * 10 result:", "ABC" * 10)


print("\nSECTION: CALLING BUILT-IN FUNCTIONS")

# TASK:
my_name = "Sajal Nepal"
print("Name:", my_name)
print("Address: Kathmandu, Nepal")
print("Contact details: sajal@example.com")
print("Length of my name:", len(my_name))

# TASK:
age_str = input("Enter your age: ")
age = int(age_str)  # The fix using int()
print("in one year your age will be", age + 1)

# TASK:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The product is", num1 * num2)


print("\nSECTION: SINGLE, DOUBLE AND TRIPLE QUOTES")

# TASK:
comment = "I would have 'thought' you knew better!"
print(comment)

# TASK:
print("This text includes characters such as '\\' '\"' and \"'\",")

# TASK:
print("\tThis is a new line that starts with a tab")
print("\t\tThis new line starts with two tabs")

# TASK:
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("Hello there!")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# TASK:
print("""This text spans three lines,
and includes both single ('),
and double quotes (").""")


print("\nSECTION: INDEXING AND SLICING")
surname = "Palin"

# TASK:
print("3rd letter:", surname[2])

# TASK:
try:
    print(surname[9])
except IndexError as e:
    print("Error accessing 10th letter (Index 9):", e)

# TASK: 
print("Second from last letter:", surname[-2])

print("Slice [1:4]:", surname[1:4])

# TASK: 
print("All except first:", surname[1:])

# TASK:
print("All except last:", surname[:-1])


print("\nSECTION: INTRODUCING LISTS")

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# TASK:
print("First four primes:", primes[0:4])

names[0] = "Terry, G."
names[0:0] = ["Tim", "Bill", "Graeme"]
names.append("Brian")
names += ["Jacob"]
print("List after text examples:", names)

# TASK:
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names[-1:-1] = ["Tim", "Bill"]
print("List after inserting before final name:", names)

try:
    test_list = [1, 2] + "string"
except TypeError as e:
    print("Error concatenating string to list:", e)

# TASK: 
nums = [1, 2, 3] * 5
print("Nums list * 5:", nums)

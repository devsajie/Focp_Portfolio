import math


# Creating a set (duplicates removed, order not guaranteed)
names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print("Names set:", names)

# Creating a set using the set() constructor
names_constructor = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])
print("Names using constructor:", names_constructor)

# Creating a set from a string
hex_letters = set("abcdef")
print("Hex letters:", hex_letters)

# Empty set
empty_set = set()
print("Empty set:", empty_set)


sentence = "this is a sentence containing some letters"

# Unique letters (including space)
unique_letters = {x for x in sentence}
print("Unique letters (with spaces):", unique_letters)

# Unique letters excluding spaces
unique_letters_no_space = {x for x in sentence if x != " "}
print("Unique letters (no spaces):", unique_letters_no_space)



name = "Alex"
if name not in names:
    print(name, "is NOT listed in the set of known names")



staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

# Union
staff = staff.union({"Mark", "Ringo"})
print("Union:", staff)

# Intersection
staff_directors = staff.intersection(directors)
print("Intersection:", staff_directors)

# Difference
external = directors.difference(staff)
print("Difference:", external)

# Symmetric difference
staff_or_external = directors.symmetric_difference(staff)
print("Symmetric Difference:", staff_or_external)



vowels = set({"a", "e", "i"})
vowels.update({"o", "u"})
print("Updated vowels:", vowels)



managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("Staff is a superset of managers")



suits = frozenset({"heart", "club", "spade", "diamond"})
print("Frozenset suits:", suits)

print({"club", "diamond"}.issubset(suits))



stock = {"apple": 10, "banana": 15, "orange": 11}
print("Initial stock:", stock)

# Add new item
stock["kiwi"] = 10
print("After adding kiwi:", stock)

# Access value
print("Banana stock level:", stock["banana"])



roots = {n: math.sqrt(n) for n in range(1, 26)}
print("Roots dictionary:", roots)



# Remove items using popitem
removed_item = stock.popitem()
print("Removed item:", removed_item)
print("Stock after popitem:", stock)



# Print keys only
print("Stock keys:")
for item in stock:
    print(item)

# Print values only
print("\nStock values:")
for level in stock.values():
    print(level)

# Print key-value pairs
print("\nStock items:")
for item, level in stock.items():
    print(item, "has a stock level of", level)



for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")


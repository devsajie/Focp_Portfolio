import math

def get_valid_price(prompt):
    while True:
        try:
            price = float(input(prompt))
            if price > 0:
                return price
            print("Price must be positive!")
        except ValueError:
            print("Please enter a number!")

# --- Main Program ---
print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

prices = []
for i in range(1, 5):
    price = get_valid_price(f"Enter Price of Pizza #{i}: ")
    prices.append(price)

# Logic: Find cheapest and subtract it
cheapest = min(prices)
total = sum(prices)
final_price = total - cheapest

# Calculate percentage
percentage = 0
if total > 0:
    percentage = math.ceil((cheapest / total) * 100)

print()
print(f"Order Total is \u00A3{final_price:.2f}, a fabulous discount of {percentage}%!")
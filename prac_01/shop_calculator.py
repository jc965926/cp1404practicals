DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
total_price = 0.00
for i in range(0, number_of_items):
    total_price += float(input(f"Price of item {i+1}: "))

if total_price > 100:
    total_price *= (1-DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92

total_price = 0
number_of_items = int(input("Number of items:"))
while number_of_items <=0:
    print("Invalid number")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print("Total price for{} item is ${:.2f}".format(number_of_items, total_price))
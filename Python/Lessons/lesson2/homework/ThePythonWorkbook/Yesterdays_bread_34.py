#34 from The Python Workbook
bread_price = 3.49
discount = 0.6

old_bread_count = int(input('Enter the number of bread: '))

regular_price = old_bread_count * bread_price
discount_price = regular_price * discount
total_price = regular_price - discount_price

print("Regular price: %5.2f" % regular_price)
print("Discount price: %5.2f" % discount_price)
print("Total price: %5.2f" % total_price)


#64 from The Python Workbook
discount = 0.6
goods = [4.95, 9.95, 14.95, 19.95, 24.95]
purchase_id = 0
print("Discount table")
for purchase in goods:
    amount = purchase * discount
    new_price = purchase - amount
    print(f"{purchase_id}: Original price: {purchase} Discount amount: {round(amount, 2)} New price: {round(new_price, 2)}")
    purchase_id += 1
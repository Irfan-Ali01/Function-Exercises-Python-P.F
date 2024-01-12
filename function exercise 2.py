def bill_amount(items, quantities, price):
  total = 0
  for item, quantity in zip(items, quantities):
    subtotal = quantity * price
    total += subtotal
  return round(total, 2)
print(bill_amount(["apple", "banana", "orange"], [2, 3, 5], 1.5)) 
print(bill_amount(["pizza", "coffee", "drinks"], [1, 2, 3], 10)) 
print(bill_amount(["coffee", "tea", "soda"], [1, 2, 3], 1))

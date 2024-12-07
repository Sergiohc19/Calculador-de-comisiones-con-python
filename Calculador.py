name = input("What is your name?  ")
sales = int(input("How many sales did you make this month? "))
commission = round(sales * 13 / 100, 2)
print(f"Hello {name}, your commissions for this month are ${commission}")

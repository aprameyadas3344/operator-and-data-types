# PART 1 - DATA TYPES
snack_name   = "chips"
price        = 1.50
quantity     =  10
is_available = True

print("snack:", snack_name)
print("price:$", price)
print("in stock:", quantity)
print("available?",is_available)


print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))


# PART 2 - ARTHMETIC OPERATORS
TOTAL = price * quantity
print("total value: $", TOTAL)
print("sale price: $", price - 0.25)
print("double stocks:", quantity * 2)


# PART 3 - COMPARISONS
print("is price under $2", price < 2)
print("more than 5 in stock? ",quantity > 5)
print("is price exacty $1.50", price == 1.50 )
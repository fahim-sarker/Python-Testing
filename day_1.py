#variable diclare
product_name = input("Enter the product name :")
product_price = int(input("Enter the product Price :"))
quantity = int(input("Enter the Product Quantity :"))
Discount = float(input("Enter the discount Percentage :"))
tax = float(input("Enter the text Percentage :"))

#aritmethic operations
total_price = product_price * quantity
after_discount_price = total_price - (Discount * total_price) /100
add_text_price = after_discount_price + (after_discount_price * tax/100)


print(total_price,after_discount_price, add_text_price)


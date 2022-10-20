# Pizza bill

customer_name: str = 'Tariqul Islam'
pizza_base: str = 'Thin'
pizza_size: int = 12
topping: str = 'Olives'
is_extra_cheese: bool = True
price: float = 1002.23

# print(f'Received Order from {customer_name}')
# print(
#     f'Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}')
# print(f'Is Extra Cheese: {is_extra_cheese}')
# print(f'Total price: {price} BDT')

# another way

order_details: str = f"""
**********Pizzza Order Service*********
---------------------------------------
Received Order from {customer_name}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
Is Extra Cheese: {is_extra_cheese}
--------------------------------------
Total price: {price} BDT
--------------------------------------
Thanks For Odering Pizza
"""

print(order_details)

# another way

print(f"""
**********Pizzza Order Service*********
---------------------------------------
Received Order from {customer_name}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
Is Extra Cheese: {is_extra_cheese}
--------------------------------------
Total price: {price} BDT
--------------------------------------
Thanks For Odering Pizza
""")

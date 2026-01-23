d_pizza = float(input("Please enter the diameter of the pizza in cm: "))
p_pizza = float(input("Please enter the price of the pizza in USD: "))
d2_pizza = float(input("Please enter the diameter of the second pizza in cm: "))
p2_pizza = float(input("Please enter the price of the second pizza in USD: "))
pi = 3.14
def converter():
    pizza_meter = d_pizza / 100
    pizza_m2 = pi * pizza_meter
    price_per_pizza = pizza_m2 / p_pizza
    return price_per_pizza
pizza_1 = converter()
pizza_2 = converter()
if pizza_1 > pizza_2:
    print("The price of the second pizza is better than the first pizza.")
else:
    print("The price of the first pizza is better than the second pizza.")
# Pizza Delivery Program
small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_for_small = 2
pepperoni_for_medium_or_large = 3
extra_cheese_any = 1

final_bill = 0

print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    if pepperoni == "Y" and extra_cheese == "Y":
        final_bill = small_pizza + pepperoni_for_small + extra_cheese_any
    elif pepperoni == "Y" and extra_cheese == "N":
        final_bill = small_pizza + pepperoni_for_small
    elif pepperoni == "N" and extra_cheese == "N":
        final_bill = small_pizza
elif size == "M":
    if pepperoni == "Y" and extra_cheese == "Y":
        final_bill = medium_pizza + pepperoni_for_medium_or_large + extra_cheese_any
    elif pepperoni == "Y" and extra_cheese == "N":
        final_bill = medium_pizza + pepperoni_for_medium_or_large
    elif pepperoni == "N" and extra_cheese == "N":
        final_bill = medium_pizza
elif size == "L":
    if pepperoni == "Y" and extra_cheese == "Y":
        final_bill = large_pizza + pepperoni_for_medium_or_large + extra_cheese_any
    elif pepperoni == "Y" and extra_cheese == "N":
        final_bill = large_pizza + pepperoni_for_medium_or_large
    elif pepperoni == "N" and extra_cheese == "N":
        final_bill = large_pizza

print(f"Your final bill is: ${final_bill}.")

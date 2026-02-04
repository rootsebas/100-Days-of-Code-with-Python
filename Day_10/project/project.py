import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def do_calculation(operator, operations, first_number, second_number):
    for opt in operations:
        if opt == operator:
            return operations[opt](first_number, second_number)

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:
        operator = input("Pick and operation: '+', '-', '*', '/': ")
        second_number = float(input("What's the second number?: "))
        result = do_calculation(operator, operations, first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        continue_calculating = input(
            f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: "
        ).lower()

        if continue_calculating == "y":
            first_number = result
        elif continue_calculating == "n":
            should_accumulate = False
            print("\n" * 25)
            calculator()

calculator()

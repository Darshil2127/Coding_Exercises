def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operation = {
    "+": add,
    "-": sub,
    "*": multiplication,
    "/": division
}
def calculator():
    n1 = int(input("Enter the first number = "))
    for symbol in operation:
        print(symbol)

    should_countinue = True
    while should_countinue:

        operation_symbol = input("Pick an operation from the line above: ")
        n2 = int(input("Enter the second number = "))
        calculation_symbol = operation[operation_symbol]
        answer = calculation_symbol(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        if input("Type 'y' for continue or 'n'  for quit = ").lower() == "y":
            n1 = answer
        else:
            should_countinue = False
            calculator()

calculator()
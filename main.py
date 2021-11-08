from art import logo


#Add
def add(n1, n2):
    return n1 + n2


#Substract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


#Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }


def calculator():
    """"Calculator function allows you to add, substract, multiply and divide two numbers. You can then
    use the answer for another calculation, start new calculation or quit."""
    calculating = True
    print(logo)
    num1 = float(input("What's the first number?"))

    while calculating:
        num2 = float(input("What's the second number?"))

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Which of the operations would you like to do?: ")

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        what_next = input(f"Click 'y' to continue with {answer} or 'n' to start new equation. Press 'q' to quit)")
        if what_next in ['y', 'Y']:
            num1 = answer
        else:
            calculating = False
            if what_next in ['n', 'N']:
                calculator()


calculator()
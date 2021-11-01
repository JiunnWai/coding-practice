def algorithm(msg_0, msg_1, msg_2, msg_3):
    # Run the algorithm according to the flowchart in project
    is_valid_inputs = False

    while not is_valid_inputs:
        x, operand, y = get_input(msg_0)

        if not is_numbers(x, y):
            print(msg_1)
        else:
            if not is_operand(operand):
                print(msg_2)
            else:
                x = float(x)
                y = float(y)
                is_valid_inputs = calculate(x, y, operand, msg_3)


def get_input(msg_0):
    # Ask user for input
    print(msg_0)
    calc = input()

    calc = calc.split()
    x = calc[0]
    operand = calc[1]
    y = calc[2]

    return x, operand, y


def is_numbers(x, y):
    # Check if the input are numbers
    try:
        _ = float(x)
        _ = float(y)
        is_number = True
    except ValueError:
        is_number = False
    return is_number


def is_operand(operand):
    # Check if the input is a valid operand
    return operand in ["+", "-", "*", "/"]


def calculate(x, y, operand, msg_3):
    # Attempt to calculate and print the result
    result = None
    is_valid_inputs = True

    if operand == "+":
        result = x + y
    elif operand == "-":
        result = x - y
    elif operand == "*":
        result = x * y
    elif result == "/" and y != 0:
        result = x / y
    else:
        is_valid_inputs = False
        print(msg_3)

    if is_valid_inputs:
        print(result)

    return is_valid_inputs


if __name__ == '__main__':
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = ("Yes ... an interesting math operation. You've slept through "
             "all classes, haven't you?")
    msg_3 = "Yeah... division by zero. Smart move..."

    algorithm(msg_0, msg_1, msg_2, msg_3)

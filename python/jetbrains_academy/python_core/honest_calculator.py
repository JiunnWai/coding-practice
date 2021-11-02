def honest_calculator(messages):
    # Run the calculator algorithm according to the flowchart in project
    memory = 0.0
    is_valid_inputs = False
    should_continue = True

    while not is_valid_inputs or should_continue:
        x, operand, y = get_input(messages["input"])

        if x == "M":
            x = memory
        if y == "M":
            y = memory

        if not is_numbers(x, y):
            print(messages["wrong_number"])
        else:
            if not is_operand(operand):
                print(messages["wrong_operand"])
            else:
                x = float(x)
                y = float(y)

                is_valid_inputs, should_continue, memory = calculate(x,
                                                                     y,
                                                                     operand,
                                                                     memory,
                                                                     messages)


def get_input(message):
    # Ask user for an equation
    calc = input(f"{message}\n")

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


def calculate(x, y, operand, memory, messages):
    # Attempt to calculate and print the result
    result = None
    is_valid_inputs = True
    should_continue = False

    if operand == "+":
        result = x + y
    elif operand == "-":
        result = x - y
    elif operand == "*":
        result = x * y
    elif operand == "/" and y != 0:
        result = x / y
    else:
        is_valid_inputs = False
        print(messages["division_by_zero"])

    if is_valid_inputs:
        print(result)
        memory = store_result(messages, memory, result)
        should_continue = continue_calculations(messages)

    return is_valid_inputs, should_continue, memory


def store_result(messages, memory, result):
    # Check if user want to store the result for further use
    while True:
        should_store_result = input(f"{messages['store_result']}\n")

        if should_store_result == "y":
            memory = result
            return memory
        elif should_store_result == "n":
            return memory


def continue_calculations(messages):
    # Check if user want to continue and do more calculations
    while True:
        should_continue = input(f"{messages['continue']}\n")

        if should_continue == "y":
            return True
        elif should_continue == "n":
            return False


if __name__ == '__main__':
    messages = {
        "input": "Enter an equation",
        "wrong_number": "Do you even know what numbers are? Stay focused!",
        "wrong_operand": ("Yes ... an interesting math operation. You've "
                          "slept through all classes, haven't you?"),
        "division_by_zero": "Yeah... division by zero. Smart move...",
        "store_result": "Do you want to store the result? (y / n):",
        "continue": "Do you want to continue calculations? (y / n):",
    }

    honest_calculator(messages)

def print_greetings():
    # Display a simple greeting message
    print("Hello! My name is Jarvis.")
    print(f"I was created in 2008.")


def get_user_name():
    # Asks the user for their name
    name = input("Please, remind me your name.\n")
    print(f"What a great name you have, {name}!")
    return name


def guess_age():
    # Asks the user for hints towards their age, return calculated age
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())

    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")
    return age


def count_numbers():
    # Ask for a number and count from 0
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())
    for n in range(num + 1):
        print(f"{n} !")


def programming_test():
    # Give the user a programming multiple choice test
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several subroutines")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = None
    correct_answer = 2

    while answer != correct_answer:
        answer = int(input())
        if answer != correct_answer:
            print("Please, try again.")
        else:
            print("Completed, have a nice day!")


def print_goodbyes():
    # Display a simple goodbye message
    print("Congratulations, have a nice day!")


if __name__ == "__main__":
    print_greetings()
    get_user_name()
    guess_age()
    count_numbers()
    programming_test()
    print_goodbyes()

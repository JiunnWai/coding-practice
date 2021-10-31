import argparse
import math


VALID_TYPES = ("annuity", "diff")
MIN_DIFF_TYPE_ARGS = 4
MIN_ANNUITY_TYPE_ARGS = 4


def is_valid_args(type, principal, periods, interest, payment):
    # Check if the user arguments are valid and return a boolean
    has_type = bool(type)
    is_valid_type = type in VALID_TYPES
    is_valid_combo = False if type == "diff" and payment > 0 else True
    has_interest = True if interest > 0 else False
    is_positives = (principal >= 0 and
                    periods >= 0 and
                    interest >= 0 and
                    payment >= 0)
    return (has_type and
            is_valid_type and
            is_valid_combo and
            has_interest and
            is_positives)


def is_valid_diff_args(num_args):
    return num_args >= MIN_DIFF_TYPE_ARGS


def is_valid_annuity_args(num_args):
    return num_args >= MIN_ANNUITY_TYPE_ARGS


def calculate_diff_payments(principal, periods, interest):
    p = principal
    n = periods
    i = interest / (12 * 100)
    total_payment = 0

    for m in range(1, n + 1):
        d = p / n + i * (p - ((p * (m - 1)) / n))
        print(f"Month {m}: payment is {math.ceil(d)}")
        total_payment += math.ceil(d)

    over_payment = total_payment - principal
    print(f"\nOverpayment = {over_payment}")


def calculate_annuity_payments(principal, periods, interest):
    p = principal
    n = periods
    i = interest / (12 * 100)

    annuity_payment = p * (i * (1 + i)**n) / ((1 + i)**n - 1)
    annuity_payment = math.ceil(annuity_payment)
    total_payment = annuity_payment * n
    print(f"Your annuity payment = {annuity_payment}!")

    over_payment = total_payment - principal
    print(f"\nOverpayment = {over_payment}")


def calculate_annuity_principal(payment, periods, interest):
    a = payment
    n = periods
    i = interest / (12 * 100)

    principal = a / ((i * (1 + i)**n) / ((1 + i)**n - 1))
    principal = math.ceil(principal)
    total_payment = a * n
    print(f"Your loan principal = {principal}!")

    over_payment = total_payment - principal
    print(f"\nOverpayment = {over_payment}")


def calculate_annuity_periods(principal, payment, interest):
    p = principal
    a = payment
    i = interest / (12 * 100)

    n = math.log(a / (a - i * p), 1 + i)
    n = math.ceil(n)
    total_payment = a * n
    print_loan_duration(n)

    over_payment = total_payment - principal
    print(f"\nOverpayment = {over_payment}")


def print_loan_duration(periods):
    years = periods // 12
    months = periods % 12
    output = "It will take "

    if years > 1:
        output += f"{years} years"
        if months > 1:
            output += f" and {months} months"
        elif months == 1:
            output += f" and {months} month"
    elif years == 1:
        output += f"{years} year"
        if months > 1:
            output += f" and {months} months"
        elif months == 1:
            output += f" and {months} month"

    output += " to repay this loan!"
    print(output)


# Setup parser for arguments
parser = argparse.ArgumentParser(description="Loan calculator")
parser.add_argument("--type", choices=VALID_TYPES)
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()
num_args = len(vars(args))

# Initialize variables
type = args.type
principal = int(args.principal) if args.principal else 0
periods = int(args.periods) if args.periods else 0
interest = float(args.interest) if args.interest else 0
payment = int(args.payment) if args.payment else 0

# Process based on calculation type
if not is_valid_args(type, principal, periods, interest, payment):
    print("Incorrect parameters")
else:
    if type == "diff" and is_valid_diff_args(num_args):
        calculate_diff_payments(principal, periods, interest)
    elif type == "annuity" and is_valid_annuity_args(num_args):
        if payment == 0:
            calculate_annuity_payments(principal, periods, interest)
        elif principal == 0:
            calculate_annuity_principal(payment, periods, interest)
        elif periods == 0:
            calculate_annuity_periods(principal, payment, interest)

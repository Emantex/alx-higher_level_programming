#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if last_digit == 0:
        print(f"{0}", end="")
        return 0
    else:
        print(f"{last_digit}", end="")
        return last_digit

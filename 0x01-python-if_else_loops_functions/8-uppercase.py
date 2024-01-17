#!/usr/bin/python3
def uppercase(str):
    for item in str:
        if ord(item) >= 97 and ord(item) <= 122:
            new = ord(item) - 32
            item = chr(new)
        print("{}".format(item), end="")
    print("")

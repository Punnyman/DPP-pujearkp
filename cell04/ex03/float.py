print("Give me a number:", end=" ")
number = float(input())
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")

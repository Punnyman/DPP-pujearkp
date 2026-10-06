print("Enter a number less than 25:")
number = input()
if number >= "25":
    print("error")
else:
    while int(number) < 25:
        print(f"Inside the loop, my variable is: {number}")
        number = int(number) + 1
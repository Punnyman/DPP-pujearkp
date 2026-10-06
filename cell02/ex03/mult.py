print("Enter the first number:")
first_number = input()
print("Enter the second number:")
second_number = input()
result = int(first_number) * int(second_number)
print(f"{first_number} x {second_number} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
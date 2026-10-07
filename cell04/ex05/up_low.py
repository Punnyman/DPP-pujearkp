print(end="")
string = input()
for char in string:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")

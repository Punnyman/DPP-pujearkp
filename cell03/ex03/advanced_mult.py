col = 0
row = 0

while col < 11:
    print(f"Table de {col}:", end="")
    while row < 11:
        print(f" {col * row}", end="")
        row += 1
    print() 
    col += 1
    row = 0
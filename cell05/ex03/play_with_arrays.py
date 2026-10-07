arr = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", arr)
new_arr_not_same = set(x + 2 for x in arr if x > 5)
print("New array: ", new_arr_not_same)
list = [1, 2, 3, 4, 1, 2, 3, 1 , 5, 6, 7, 8, 0, 2, 5, 6]

# using loop to find duplicates
for i in list:
    if list.count(i) > 1:
        print(f"Duplicate element is: {i}")
else:
    print("No duplicate elements found")

# Using set to find duplicates
if len(list) != len(set(list)):
    print("Duplicate elements exist")
else:
    print("No duplicate elements found")
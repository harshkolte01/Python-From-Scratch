list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 5]

# using loop to find common elements
for i in list1:
    for j in list2:
        if i == j:
            print("Common element found:", i)
            break
        else:
            print("No common element found")

# using set disjoint
if set(list1).isdisjoint(set(list2)):
    print("No common element found")
else:
    print("Common elements exist")

# using intersection
common_elements = set(list1).intersection(set(list2))
if common_elements:
    print("Common elements found:", common_elements)    
else:
    print("No common element found")
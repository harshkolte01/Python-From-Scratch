a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

(a, b) = (b, a)
print("After Swapping:")
print("Number 1:", a)
print("Number 2:", b)
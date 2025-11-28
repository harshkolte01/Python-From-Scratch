a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

def printEven(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)

printEven(a, b)
a = int(input("Enter a number: "))
def printDigits(n):
    if n == 0:
        return
    else:
        digit = n % 10
        printDigits(n // 10) # Removes the last digit
        print(digit)

printDigits(a)
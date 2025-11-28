a = int(input("Enter first number: "))
def sumOfDigits(n):
    if n == 0:
        return 0
    
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

result = sumOfDigits(a)
print("Sum of digits:", result)


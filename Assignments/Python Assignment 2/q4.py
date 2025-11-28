a = int(input("Enter first number: "))
def countDigit(n):
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

result = countDigit(a)
print("Number of digits:", result)


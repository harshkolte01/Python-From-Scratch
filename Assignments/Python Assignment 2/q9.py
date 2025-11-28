a = int(input("Enter number: "))

def isPrime(a):
    if a <= 1:
        return False
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

result = isPrime(a)
print(result)
    
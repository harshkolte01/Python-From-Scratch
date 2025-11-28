a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
ops = input("Enter operator: ")

def calc(a, b, ops):
    match ops:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Invalid operator"

result = calc(a, b, ops)
print(result)
x = 10 + 3 * 2 ** 2
print(x)

# evaluate the expression step-by-step
step1 = 2 ** 2          # Exponentiation priority
step2 = 3 * step1       # Multiplication priority
x = 10 + step2          # Addition last
print(x)
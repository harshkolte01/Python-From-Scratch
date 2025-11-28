salary = float(input("Enter your salary: "))
if salary < 30000:
    tax_rate = salary * 0.05
elif salary >= 30000 and salary <= 70000:
    tax_rate = salary * 0.15
else:
    tax_rate = salary * 0.25
print("The tax rate is:", tax_rate)
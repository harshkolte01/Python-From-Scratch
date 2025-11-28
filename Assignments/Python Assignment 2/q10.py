a = int(input("Enter number: "))
secret = 10
if a == secret:
    print("correct")
elif a < secret:
    print("too low")
else:
    print("too high")
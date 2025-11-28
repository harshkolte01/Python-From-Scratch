while True:
    a = input("Enter number: ")

    if a == "Quit":
        print("Program Quit")
        break

    a = int(a)
    if a > 0:
        print("Positive")
    else:
        print("Negative")
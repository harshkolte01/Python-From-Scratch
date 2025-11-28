while True:
    a = input("Enter number: ")

    if a == "Quit":
        print("Program Quit")
        break

    a = int(a)
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
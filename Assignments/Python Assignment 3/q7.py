a = input("Enter string with spaces: ")

def countSpace(a):
    count = 0
    for char in a:
        if char == " ":
            count += 1
    return count

print(countSpace(a))
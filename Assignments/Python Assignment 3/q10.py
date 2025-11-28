a = input("Enter String: ").lower()

def uniqueChar(a):
    unique = ""
    for char in a:
        if char not in unique:
            unique += char
    return unique

print(uniqueChar(a))

# Using set
print(set(a))
a = input("Enter Text: ")
# Check palindrome using slice
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")

# Check palindrome using loop
c = ""
for char in a:
    c = char + c
if a == c:
    print("Palindrome") 
else:
    print("Not Palindrome")
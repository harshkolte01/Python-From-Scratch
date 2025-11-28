tuple = (1, 2, 3, 4, 5)
eventuple = ()
oddtuple = ()

for i in tuple:
    if i % 2 == 0:
        eventuple += (i,)
    else:
        oddtuple += (i,)

print("Even Tuple:", eventuple)
print("Odd Tuple:", oddtuple)
dict = {
    "John": "100",
    "Alice": "85",
    "Bob": "90",
    "Charlie": "95"
}

choice = input("Enter Choice: A, B, C, D: ")

match choice:
    case "A":
        name, marks = input("Enter student name and marks: ").split()
        dict[name] = marks
        print("Student added successfully.")
    case "B":
        name = input("Enter student name: ")
        if name in dict:
            dict.update({name: input("Enter new marks: ")})
            print(f"Marks updated for {name}. Updated Marks: {dict[name]}")
        else:
            print("Student not found.")
    case "C":
        name = input("Enter Student name: ")
        if name in dict:
            print(f"Student name: {name}, Marks: {dict[name]}")
    case "D":
        print("All Students and Marks:")
        for name, marks in dict.items():
            print(f"Student name: {name}, Marks: {marks}")
    case _:
        print("Invalid Choice")

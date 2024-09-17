# Exercise 1:
#     Create a program in your favourite programming language (e.g. Python, Java, C, C++, etc) that 
#     - perform any task you like to do (sorting, searching, shuffling, get max, get min,
#       take average, fibonacci, factorial, GCD, pythagoras, etc.)

def get_min_max():
    while True:
        print("\nHello! Choose an option 🤗")
        print("1. Get Minimum Number")
        print("2. Get Maximum Number")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            numbers = eval(input("Enter a list of numbers 🔢: "))
            # e.g. input: 1, 2, 3, 4
            print("Minimum Number: ", min(numbers))
        elif choice == '2':
            numbers = eval(input("Enter a list of numbers 🔢: "))
            # e.g. input: 1, 2, 3, 4
            print("Maximum Number: ", max(numbers))
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

get_min_max()
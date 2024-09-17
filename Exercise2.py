# Exercise 2:
#  a) Create a program in your favourite programming language (e.g. Python, Java, C, C++, etc) that
#     - reads the source code CHARACTER BY CHARACTER
#     - print out to the screen

#  b) The same Program that prints ONLY THE PYTHON/C++/C/Java KEYWORDS
#     please, provide a MENU to let users choose
#     - OPTION 1: Print PER CHARACTER
#     - OPTION 2: Print ALL THE KEYWORD


import keyword

def menu():
    while True: 
        print("\nHello! Choose an option 🤗")
        print("1. Print PER CHARACTER")
        print("2. Print ALL THE KEYWORDS")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        # Change according to your file path in your laptop
        file_path = "/Users/clarissaaudrey/Desktop/Semester 5/Compilation Techniques/Session 2/Exercise1.py"
        
        if choice == '1':
            file = open(file_path, "r")
            for code in file:
                print(code, end="")
        elif choice == '2':
            file = open(file_path, "r")
            for code in file:
                # Ignore comments 
                if code.strip().startswith("#"):
                    continue
                
                words = code.split()

                for word in words:
                    # Check if the word is a Python keyword
                    if word in keyword.kwlist:
                        print(word)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

menu()
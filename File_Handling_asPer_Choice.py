def open_file():
    f=open('abc.txt', 'r')
    print("File opened successfully!")

def write_file():
    f=open('abc.txt', 'w')
    s=input("Enter the content: ")
    f.write(s)
    print("Successfully..Content was written")

def search_file():
    word_To_search=input("Enter word to search:")
    f=open('abc.txt', 'r')
    content = f.read()
    if word_To_search in content:
        print("Word",word_To_search ,"found in the file.")
    else:
        print("Word",word_To_search ,"not found in the file.")

def menu():
    while True:
        print("\nChoose an option:")
        print("1. Open File")
        print("2. Write File")
        print("3. Search for word")
        print("4. Exit")
        
        choice = input("Enter your choice (R/W/S/E): ")
        
        if choice == 'R':
            open_file()
        elif choice == 'W':
            write_file()
        elif choice == 'S':
            search_file()
        elif choice == 'E':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.try again.")


menu()

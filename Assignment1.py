# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Odam Tong
# Assignment Number: Lab#1
# Due Date: 01/21/ 2026
# Purpose: This program is to create a menu
# that allows the user to add string into a buffer, clear it and then display.
# List Specific resources used to complete the assignment. I used classroom materials
# python help from the web: https://www.geeksforgeeks.org/python/help-function-in-python/

def main():
    input_buffer = ""

    while True:
        print("\nMenu:")
        print("1. Buffer Input")
        print("2. Clear buffer")
        print("3. Display buffer")
        print("4. Exit the program")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            data = input("Enter the buffer string: ")
            input_buffer += data + " "  # This will add the data with a space
            print("Data added to buffer successfully.")

        elif choice == '2':
            input_buffer = ""  # This will clear the buffer
            print("Input buffer data cleared successfully.")

        elif choice == '3':
            print("Most recently saved data in the buffer:", input_buffer.strip())  #This will display what is currently in the buffer

        elif choice == '4':
            print("Exiting the program.") #This will exit the program.
            break

        else:
            print("Invalid option. Please choose a number between 1 and 4.") #Catch all if the user inputs anything other than 1,2,3 or 4


if __name__ == "__main__":
    main()

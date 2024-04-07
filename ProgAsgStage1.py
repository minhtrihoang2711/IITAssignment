"""
Student name: Minh Tri Hoang
Student ID: u3281069
Assessment: Python Programming Assignment
Date: 6/04/2024
"""

# Constants
ATHLETES_FILE = "athletes.txt"

# Function to print the menu options
def print_menu():
    print("Welcome to the Atheletes App")
    print("\n1. Display all athletes' data")
    print("2. Search for athletes by sport")
    print("3. Exit")

# Function to read athletes data from file
def read_athletes_file(filename):
    athletes = []
    with open(filename, "r") as file:
        for line in file:
            athlete_data = line.strip().split(",")
            athletes.append(tuple(athlete_data))
    return athletes


# Function to display all athletes data
def display_athletes_data(athletes, show_header=True):
    if show_header:
        print("All Athletes' Data:")
    print("{:<10} {:<15} {:<15} {:<8} {:<5} {:<8} {:<8} {:<15} {:<15} {:<10}".format(
        "Number", "First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport", "Class"))

    for i, athlete in enumerate(athletes, 1):
        print("{:<10} {:<15} {:<15} {:<8} {:<5} {:<8} {:<8} {:<15} {:<15} {:<10}".format(
            i, *athlete))

    choice = input("Press 1 to go back to the menu or any other key to exit the program: ")
    if choice == "1":
        return
    else:
        print("\nGoodbye, hope to see you next time")
        exit()

# Function to search for athletes by sport
def search_athletes(athletes):
    sport = input("Enter the sport you want to search: ")
    found_athletes = []
    for athlete in athletes:
        if athlete[7].lower() == sport.lower():
            found_athletes.append(athlete)
    if not found_athletes:
        choice = input("No results found. Press 1 to go back to the main menu or any other key to exit the program: ")
        if choice == "1":
            return
        else:
            print("\nGoodbye, hope to see you next time")
            exit()
    else:
        found_athletes.sort(key=lambda x: (x[8], x[1]))
        display_athletes_data(found_athletes, False)

# Main function to direct the program
def main():
    athletes = read_athletes_file(ATHLETES_FILE)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            athletes.sort(key=lambda x: (x[8], x[1])) 
            display_athletes_data(athletes)
        elif choice == "2":
            search_athletes(athletes)
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

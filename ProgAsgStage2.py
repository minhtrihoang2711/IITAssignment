"""
Student name: Minh Tri Hoang
Student ID: u3281069
Assessment: Python Programming Assignment
Date: 7/04/2024
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext

# Constants
ATHLETES_FILE = "athletes.txt"

# Function to read athletes data from file
def read_athletes_file(filename):
    athletes = []
    with open(filename, "r") as file:
        for line in file:
            athlete_data = line.strip().split(",")
            athletes.append(tuple(athlete_data))
    return athletes

# Function to search for athletes by sport
def search_athletes(athletes, sport):
    # Filter athletes by the specified sport
    return [athlete for athlete in athletes if athlete[7].lower() == sport.lower()]

# GUI Application
class AthletesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Athletes App")
        self.geometry("1366x768") 

        self.athletes = read_athletes_file(ATHLETES_FILE)

        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left frame for athletes list and search results list
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Athletes list label, listbox, and scrollbar
        tk.Label(left_frame, text="Athletes List").pack()
        athletes_list_frame = tk.Frame(left_frame)
        athletes_list_frame.pack(fill=tk.BOTH, expand=True)
        self.athletes_listbox = tk.Listbox(athletes_list_frame, height=4)  
        self.athletes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        athletes_scrollbar = tk.Scrollbar(athletes_list_frame, orient="vertical", command=self.athletes_listbox.yview, width=20)  
        athletes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.athletes_listbox.config(yscrollcommand=athletes_scrollbar.set)

        # Search results list label, listbox, and scrollbar
        tk.Label(left_frame, text="Search Results List").pack()
        search_results_list_frame = tk.Frame(left_frame)
        search_results_list_frame.pack(fill=tk.BOTH, expand=True)
        self.search_results_listbox = tk.Listbox(search_results_list_frame, height=4)  
        self.search_results_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        search_results_scrollbar = tk.Scrollbar(search_results_list_frame, orient="vertical", command=self.search_results_listbox.yview, width=20)  
        search_results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.search_results_listbox.config(yscrollcommand=search_results_scrollbar.set)

        # Right frame for details and search
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Welcome label
        tk.Label(right_frame, text="Welcome to the Athletes App, Stage(2) !", font=("Helvetica", 16)).pack(pady=20)

        # Details frame
        details_frame = tk.Frame(right_frame)
        details_frame.pack()

        # Entry widgets for athlete details
        self.entries = {}
        details = ["First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport", "Class"]
        for detail in details:
            frame = tk.Frame(details_frame)
            frame.pack(side=tk.LEFT)
            tk.Label(frame, text=detail).pack(side=tk.TOP)
            entry = tk.Entry(frame, width=10, state='readonly') 
            entry.pack(side=tk.BOTTOM)
            self.entries[detail] = entry

        # Search area
        search_frame = tk.Frame(right_frame)
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Enter a sport to search").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        self.search_button = tk.Button(search_frame, text="Search...", command=self.on_search)
        self.search_button.pack(side=tk.LEFT)

        # Bind the listbox select event for the athletes listbox
        self.athletes_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        # Bind the listbox select event for the search results listbox
        self.search_results_listbox.bind('<<ListboxSelect>>', self.on_search_listbox_select)

        # Initially fill the athletes list
        self.refresh_athletes_list()

    def refresh_athletes_list(self):
        # Clear the current list
        self.athletes_listbox.delete(0, tk.END)
        # Fill the listbox with athletes' first names
        for athlete in self.athletes:
            self.athletes_listbox.insert(tk.END, athlete[0])  # Use index 0 for first name

    def on_search(self):
        # Clear the search results list
        self.search_results_listbox.delete(0, tk.END)
        # Perform the search
        sport = self.search_entry.get().strip().lower()  
        if sport:  # Check if the search entry is not empty
            found_athletes = search_athletes(self.athletes, sport)
            if found_athletes:  # Check if any athletes were found
                # Update the search results list with first names of found athletes
                for athlete in found_athletes:
                    self.search_results_listbox.insert(tk.END, athlete[0])  # Use index 0 for first name
            else:
                # Display "No result found" message
                self.search_results_listbox.insert(tk.END, "No result found")

    def on_listbox_select(self, event):
        # Get selected index
        try:
            index = self.athletes_listbox.curselection()[0]
            athlete = self.athletes[index]
        except IndexError:
            return  # In case of empty selection

        # Update entry widgets with athlete details
        details = ["First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport", "Class"]
        for i, detail in enumerate(details):
            self.entries[detail].config(state='normal')  
            self.entries[detail].delete(0, tk.END)
            self.entries[detail].insert(0, athlete[i])
            self.entries[detail].config(state='readonly')  

    def on_search_listbox_select(self, event):
        # Get selected index from the search results listbox
        try:
            index = self.search_results_listbox.curselection()[0]
            selected_name = self.search_results_listbox.get(index)
            # Find the full details of the selected athlete by matching the first name
            for athlete in self.athletes:
                if athlete[0].lower() == selected_name.lower():  # Use index 0 for first name
                    self.update_entries(athlete)
                    break
        except IndexError:
            return  # In case of empty selection

    def update_entries(self, athlete):
        # Update entry widgets with athlete details
        details = ["First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport", "Class"]
        for i, detail in enumerate(details):
            self.entries[detail].config(state='normal')  
            self.entries[detail].delete(0, tk.END)
            self.entries[detail].insert(0, athlete[i])
            self.entries[detail].config(state='readonly')  

def main():
    app = AthletesApp()
    app.mainloop()

if __name__ == "__main__":
    main()

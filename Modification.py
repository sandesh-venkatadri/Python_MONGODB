import tkinter as tk
from tkinter import messagebox, ttk
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["infoteck"]
collection = db["employees"]

# Function to retrieve employee details by name
def get_employee_details(name):
    employee = collection.find_one({"name": name})
    return employee

# Function to handle button click event
def search_employee():
    name = entry_name.get()
    if name:
        employee = get_employee_details(name)
        if employee:
            details_text.set(f"EmpID: {employee['empid']}\nName: {employee['name']}\nAge: {employee['age']}")
        else:
            details_text.set("Employee not found.")
    else:
        messagebox.showerror("Error", "Please enter employee name.")

# Create main application window
root = tk.Tk()
root.title("Employee Database")

# Create and pack widgets
label_name = ttk.Label(root, text="Enter Employee Name:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_name = ttk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

button_search = ttk.Button(root, text="Search", command=search_employee)
button_search.grid(row=0, column=2, padx=10, pady=10)

details_text = tk.StringVar()
details_label = ttk.Label(root, textvariable=details_text, wraplength=300, justify="left")
details_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()

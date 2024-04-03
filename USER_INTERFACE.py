import tkinter as tk
from tkinter import messagebox
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
            messagebox.showinfo("Employee Details", f"EmpID: {employee['empid']}\nName: {employee['name']}\nAge: {employee['age']}")
        else:
            messagebox.showerror("Error", "Employee not found.")
    else:
        messagebox.showerror("Error", "Please enter employee name.")

# Create main application window
root = tk.Tk()
root.title("Employee Database")

# Create and pack widgets
label_name = tk.Label(root, text="Employee Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

button_search = tk.Button(root, text="Search", command=search_employee)
button_search.pack()

# Run the application
root.mainloop()

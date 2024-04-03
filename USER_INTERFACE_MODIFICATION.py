import tkinter as tk
from tkinter import messagebox
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["infoteck"]
collection = db["employees"]

# Function to save employee
def save_employee():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        try:
            age = int(age)
            employee = {"name": name, "age": age}
            collection.insert_one(employee)
            messagebox.showinfo("Success", "Employee details saved successfully.")
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")
    else:
        messagebox.showerror("Error", "Please enter employee name and age.")

# Function to delete employee
def delete_employee():
    name = entry_name.get()
    if name:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            messagebox.showinfo("Success", "Employee deleted successfully.")
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Employee not found.")
    else:
        messagebox.showerror("Error", "Please enter employee name.")

# Create main application window
root = tk.Tk()
root.title("Employee Management")

# Create and pack widgets
label_name = tk.Label(root, text="Enter Employee Name:")
label_name.pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack()

label_age = tk.Label(root, text="Enter Employee Age:")
label_age.pack()

entry_age = tk.Entry(root, width=30)
entry_age.pack()

button_save = tk.Button(root, text="Save", command=save_employee)
button_save.pack()

button_delete = tk.Button(root, text="Delete", command=delete_employee)
button_delete.pack()

# Run the application
root.mainloop()

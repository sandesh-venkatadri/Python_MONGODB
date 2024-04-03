import tkinter as tk
from tkinter import messagebox
import pymongo


#Connecting to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["admin"]
collection = db["My_First_Collection"]

root = tk.Tk()
root.title("collection_management")

#Create entry widget for name and age
entry_name = tk.Entry(root, width=30)
entry_name.pack()
entry_age = tk.Entry(root, width=30)
entry_age.pack()

def save_person():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        try:
            age = int(age)
            person = {"name" : name, "age" : age}
            collection.insert_one(person)
            messagebox.showinfo("Success", "Person details saved successfully")
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Enter valid age")
    else:
        messagebox.showerror("Error", "enter person name and age")

def delete_person():
    name = entry_name.get()
    if name:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            messagebox.showinfo("Success", "Person details deleted successfully")
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)

        else:
            messagebox.showerror("Error", "Person not found")
    else:
        messagebox.showerror("Error", "Please enter person's name")


#Create main application window
root = tk.Tk()
root.title("collection_management")

#Create a packet widget
label_name = tk.Label(root, text="Enter person's name: ")
label_name.pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack()

label_age = tk.Label(root,text= "Enter person's age: ")
label_age.pack()

entry_age = tk.Entry(root, width=30)
entry_age.pack()

button_save = tk.Button(root, text="Save", command=save_person)
button_save.pack()

button_delete = tk.Button(root, text = "Delete", command=delete_person)
button_delete.pack()

#Run the application
root.mainloop()






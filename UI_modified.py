import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["infoteck"]
collection = db["employees"]

# Function to retrieve employee details by name
def get_employee_details(name):
    employee = collection.find_one({"name": name})
    return employee

# Main function
def main():
    # Sample data
    sample_data = [
        { "empid": 1, "name": "John", "age": 30 },
        { "empid": 2, "name": "Alice", "age": 25 },
        { "empid": 3, "name": "Bob", "age": 35 },
        # Add more sample data as needed
    ]

    # Insert sample data into the collection
    collection.insert_many(sample_data)

    print("Sample data inserted successfully.")

    # Input employee name
    employee_name = input("Enter employee name: ")

    # Retrieve employee details
    employee = get_employee_details(employee_name)

    # Check if employee exists
    if employee:
        print("Employee Details:")
        print(f"EmpID: {employee['empid']}")
        print(f"Name: {employee['name']}")
        print(f"Age: {employee['age']}")
    else:
        print("Employee not found.")

if __name__ == "__main__":
    main()

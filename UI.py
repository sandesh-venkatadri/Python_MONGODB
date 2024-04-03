import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["infoteck"]
collection = db["employees"]

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

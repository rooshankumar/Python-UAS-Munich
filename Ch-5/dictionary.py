# Create a dictionary
person = {
    "name": "Roshan",
    "age": 22,
    "city": "Patna"
}

print("Original dictionary:", person)

# keys() → Get all keys
print("Keys:", person.keys())

# values() → Get all values
print("Values:", person.values())

# items() → Get all key-value pairs
print("Items:", person.items())

# get() → Access value by key safely
print("Age:", person.get("age"))
print("Country (with default):", person.get("country", "Not specified"))

# update() → Add or update entries
person.update({"city": "Delhi", "country": "India"})
print("After update:", person)

# pop() → Remove a key and get its value
age = person.pop("age")
print("Popped age:", age)
print("After popping age:", person)

# popitem() → Remove and return the last inserted item
last_item = person.popitem()
print("Popped last item:", last_item)
print("After popping last item:", person)

# copy() → Create a copy of the dictionary
person_copy = person.copy()
print("Copy of dictionary:", person_copy)

# clear() → Empty the dictionary
person.clear()
print("After clearing:", person)

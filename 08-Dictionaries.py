emptyDictionary = (
    dict()
)  # This is Deprecated in Python 3.9 and Above, Use emptyDictionary = {} Instead
print("Empty Dictionary:", emptyDictionary)

# Creating a Dictionary
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {"street": "123 Main St", "city": "New York", "state": "NY"},
}
print("Person Dictionary:", person)
print("Length of Person Dictionary:", len(person))
# Accessing Dictionary Items
print(
    "First Name:", person["first_name"]
)  # Using Key Raises An Error if Key Does Not Exist
print("Skills:", person["skills"])
print("Main Skill:", person["skills"][0])
print("Street:", person["address"]["street"])

print(
    "Last Name:", person.get("last_name")
)  # Using get() Returns None if Key Does Not Exist
print("Middle Name:", person.get("middle_name"))  # Returns None if Key Does Not Exist

# Adding And Modifying Items to a Dictionary
person["gender"] = "Male"
print("Gender:", person["gender"])
person["middle_name"] = "William"
print("Person Dictionary after adding middle name:", person)

print("Age:", person["age"])
person["age"] = 31  # If Key Exists, It Will Modify the Value
print("Modified Age:", person["age"])

# Checking if a Key Exists in a Dictionary
print('Is "first_name" in Person Dictionary: ', "first_name" in person)
print('Is "nickname" in Person Dictionary: ', "nickname" in person)

# Removing Items from a Dictionary
person.pop(
    "address"
)  # Removes the Key-Value Pair and Returns the Value, Raises an Error if Key Does Not Exist
print("Person Dictionary after removing address:", person)

del person[
    "middle_name"
]  # Removes the Key-Value Pair, Also Raises an Error if Key Does Not Exist
print("Person Dictionary after removing middle name:", person)

person.popitem()  # Removes the Last Key-Value Pair and Returns it as a Tuple
print("Person Dictionary after removing last item:", person)

# Changing a Dictionary to a List of Tuples
personItems = person.items()  # Return a dict_items List Of Tupes, Needs to Be Converted to a List using list() to Access the Items
print("Person Items:", personItems)
print("First Pair in Person Items:", list(personItems)[0])

#Copying a Dictionary
laptop = {
    "brand": "Dell",
    "model": "XPS 13",
    "processor": "Intel Core i7",
    "ram": "16GB",
    "storage": "512GB SSD",
}
laptopCopy = laptop.copy()
print("Copied Laptop Dictionary:", laptopCopy)

#Clearing a Dictionary
print("Laptop Dictionary before clearing:", laptop)
laptop.clear()
print("Laptop Dictionary after clearing:", laptop)

#Deleting a Dictionary
del laptop  # Accessing laptop after deletion will raise an error

print("LaptopCopy Dictionary Still Exists Even After Deletion of Laptop Dictionary:", laptopCopy)

#Getting Dictionary Keys and Values as Lists
print("LaptopCopy Keys:", laptopCopy.keys()) #Returns a dict_keys List of Keys, Needs to Be Converted to a List using list() to Access the Keys
print("LaptopCopy Values:", laptopCopy.values()) #Returns a dict_values List of Values, Needs to Be Converted to a List using list() to Access the Values
print("LaptopCopy Keys as List:", list(laptopCopy.keys()))
print("LaptopCopy Values as List:", list(laptopCopy.values()))


##############1 Common serialization

import pickle
# objects into a binary format, supporting almost all Python data types, including custom objects.
# Use cases:
# Saving Python objects (e.g., model weights in machine learning).
# Sharing Python-specific data between applications.
# Define a sample object
data = {'name': 'Alice', 'age': 25, 'is_student': False}

# Serialize the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize the object from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)


# import dill
# # The dill module is an extended version of pickle, capable of serializing more complex objects, such as functions, lambdas, and closures.
# # Define a function
# def greet(name):
#     return f"Hello, {name}!"

# # Serialize the function
# with open('greet.pkl', 'wb') as file:
#     dill.dump(greet, file)

# # Deserialize the function
# with open('greet.pkl', 'rb') as file:
#     loaded_function = dill.load(file)

# print(loaded_function('Alice'))



# human-readable JSON format,
import json

# Define a sample object
data = {'name': 'Alice', 'age': 25, 'is_student': False}

# Serialize the object to a JSON string
json_data = json.dumps(data)
print(json_data)

# Deserialize back to a Python object
loaded_data = json.loads(json_data)
print(loaded_data)

# Write JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Read JSON from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)


import marshal
# The marshal module is used for Python-specific object serialization, primarily for writing and reading .pyc files (compiled Python files). It's faster but less flexible and less secure than pickle.
# Define a sample object
data = {'name': 'Alice', 'age': 25, 'is_student': False}

# Serialize the object to a binary string
serialized_data = marshal.dumps(data)

# Deserialize back to a Python object
loaded_data = marshal.loads(serialized_data)
# Use cases:
# Low-level serialization for internal Python tasks.
# Not recommended for general-purpose serialization.
print(loaded_data)






##################2=Custom Object Serialization

#  Serializing Custom Objects with pickle
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object
person = Person('Alice', 25)

# Serialize the object
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# Deserialize the object
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)

print(f"Name: {loaded_person.name}, Age: {loaded_person.age}")



# Serializing Custom Objects with json

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

# Custom decoder
def person_decoder(dct):
    if 'name' in dct and 'age' in dct:
        return Person(dct['name'], dct['age'])
    return dct

# Create an object
person = Person('Alice', 25)

# Serialize the object
json_data = json.dumps(person, cls=PersonEncoder)
print(json_data)
# Custom Encoding with cls=PersonEncoder
# To handle custom objects, we use the cls parameter in json.dumps.
# The cls parameter allows you to specify a custom encoder class that extends json.JSONEncoder.
# The PersonEncoder class overrides the default method of json.JSONEncoder. This method is called for objects that are not directly serializable.

# Deserialize the object
loaded_person = json.loads(json_data, object_hook=person_decoder)
print(f"Name: {loaded_person.name}, Age: {loaded_person.age}")
# Custom Decoding with object_hook=person_decoder
# The object_hook parameter lets you specify a custom function that processes each dictionary produced during deserialization.
# When json.loads() encounters a dictionary, it passes that dictionary to the person_decoder function.

# Convert JSON data to Python object
import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
py_obj = json.loads(json_obj)
print("JSON Data: ")
print(py_obj)
print(f'Name:{py_obj["Name"]}')
print(f'Class:{py_obj["Class"]}')
print(f'Age:{py_obj["Age"]}')
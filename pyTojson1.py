# Convert Python dictionary object to JSON data. Print the object members with indent level 4
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original:",j_str)
print("Json: ",json.dumps(j_str,sort_keys=True,indent=4))
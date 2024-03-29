# Convert Python object to JSON data
import json
py_obj = {
    "name":'Meow',
    "class":12,
    "age":10
}
jsn = json.dumps(py_obj)
print(jsn)

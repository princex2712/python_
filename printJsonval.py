import json
py_dict = {"name": "David", "age": 6, "class":"I"}
py_list = ["Red", "Green", "Black"]
py_str = "Python Json"
py_int = (1234)
py_float = (12.34)
py_T = (True)
py_F = (False)
py_N = (None)

json_dict = json.dumps(py_dict)
json_list = json.dumps(py_list)
json_str = json.dumps(py_str)
json_int = json.dumps(py_int)
json_flt = json.dumps(py_float)
json_T = json.dumps(py_T)
json_F = json.dumps(py_F)
json_N = json.dumps(py_N)

print("json_dict: ",json_dict)
print("json_list: ",json_list)
print("json_str: ",json_str)
print("json_int: ",json_int)
print("json_flt: ",json_flt)
print("json_T: ",json_T)
print("json_F: ",json_F)
print("json_N: ",json_N)
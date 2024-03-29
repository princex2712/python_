# Check whether an instance is complex or not
import json
def is_complex(obj):
    if isinstance(obj,complex):
        return [obj.real,obj.imag]
    raise TypeError(repr(object) + " is not JSON serialized")
obj = json.dumps(2+3j,default=is_complex)
print(obj)
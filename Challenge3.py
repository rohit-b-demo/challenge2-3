any_dict = {"a": {"b": {"c": "d", "g": "h"}, "i": {"c": "m1", "g": "m2"}}}
any_dict2 = {"a": {"b": {"c": "d"}}}

# Funtion to get the value of specific key
def get_value(val, expected_key):
    for key, val in val.items():
        if key in expected_key:
            print(val)
            break
        elif isinstance(val, dict):
            get_value(val, expected_key)
        else:
            print ("Not Matched")

get_value(any_dict, "a")
get_value(any_dict, "b")
get_value(any_dict, "c")
get_value(any_dict2, "c")
get_value(any_dict2, "g")

import json

# get list of all types
with open('data/type_resolution/universal_type_map_final.json') as f:
    universal_type_map = json.load(f)
    type_list = list(universal_type_map.keys())
    
type_handling = dict()

for _type in type_list:
    if "." in _type:
        _type = _type.split(".")[-1]
        
    _type_name = _type    
    if "<" in _type:
        _type_name = _type.split("<")[0]
        
    type_handling[_type] = f"{{}}.as({_type_name}.class)"


# save to type_handling.json
with open('src/compositional_glue_tests/type_handling.json', 'w') as f:
    json.dump(type_handling, f, indent=4)

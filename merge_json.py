import json,os

new_attrs = {
    'numpy': './data/numpy_new.json',
    'matplotlib': './temp/matplotlib_new.json'
}

new_json = []

for library_name, library_json_path in new_attrs.items():
    with open(library_json_path, 'r') as f:
        library_json = json.load(f)
    for func_dict in library_json:
        func_name = func_dict['function name']
        func_desc = func_dict['function description']
        new_json.append({
            'funct_name': func_name,
            'funct_description': func_desc,
            'library': library_name
        })

with open('./temp/pyhint.json', 'w') as f:
    json.dump(new_json, f, indent=4)
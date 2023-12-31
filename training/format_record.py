import json
import os

with open('data/matplotliib.json', 'r') as f:
    data = json.load(f)
new_data = []
for key, value in data.items():
    new_item = {
        'function name': key,
        'function description': value,
    }
    new_data.append(new_item)
with open('./temp/matplotlib_new.json', 'w') as f:
    json.dump(new_data, f, indent=4)

import json

# matplotlib_path = './data/matplotliib.json'
# with open(matplotlib_path) as f:
#     matplotlib_dict = json.load(f)
# new_dict = {}
# # reverse key and value
# for k, v in matplotlib_dict.items():
#     new_dict[v] = k
# with open('./temp/matplotlib.json', 'w') as f:
#     json.dump(new_dict, f, indent=4)

with open('./temp/matplotlib.json', 'r') as f:
    matplotlib_dict = json.load(f)

# convert all the words in key to lower case
new_dict = {}
for k, v in matplotlib_dict.items():
    # remove comma, period, question mark, exclamation mark
    new_dict[k.lower().rstrip(',.?!')] = v
with open('./temp/matplotlib.json', 'w') as f:
    json.dump(new_dict, f, indent=4)



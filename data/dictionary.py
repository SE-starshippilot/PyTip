#

import json

# 读取文本文件内容
with open('matplotlib.txt', 'r') as file:
    lines = file.readlines()

# 创建一个空的字典，用于存储键值对
data = {}

# 遍历每行内容，将奇数行作为键，偶数行作为值
for i in range(0, len(lines), 2):
    key = lines[i].strip()
    value = lines[i + 1].strip()
    data[key] = value

# 将字典存储为 JSON 格式的字符串
json_data = json.dumps(data)

# 将 JSON 字符串写入到文件中
with open('matplotliib.json', 'w') as file:
    file.write(json_data)

print("OK!")

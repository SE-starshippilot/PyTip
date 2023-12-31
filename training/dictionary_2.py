import json

# 读取文本文件
with open("numpy.txt", "r") as file:
    lines = file.readlines()

# 创建一个空的列表来存储JSON结构
json_list = []

# 遍历行号和内容
for i in range(0, len(lines), 2):
    # 提取奇数行作为"function name"
    function_name = lines[i].strip()
    # 提取偶数行作为"function description"
    function_description = lines[i + 1].strip()

    # 创建JSON结构
    json_data = {
        "function name": function_name,
        "function description": function_description
    }

    # 将JSON结构添加到列表中
    json_list.append(json_data)

# 将列表写入JSON文件
with open("output.json", "w") as file:
    json.dump(json_list, file, indent=4)
import json

# 读取文本文件
with open("numpy.txt", "r") as file:
    lines = file.readlines()

# 创建一个空的字典来存储数据
data_ALL = []

# 遍历行号和内容
for i, line in enumerate(lines):
    data = {}
    # 奇数行存储为"function name"
    if i % 2 == 0:
        data["function name"] = line.strip()
    # 偶数行存储为"function description"
    else:
        data["function description"] = line.strip()
    data_ALL.append(data)
# 将数据写入JSON文件
with open("numpy.json", "w") as file:
    file.write(str(data_ALL))
print("OK!")
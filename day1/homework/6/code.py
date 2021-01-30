names = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}]

names.insert(len(names), {"name": "wangwu", "age": 21})

for i in range(0, len(names)):
    if names[i]["name"] == "lisi":
        names[i]["name"] = "李四"

print(names)

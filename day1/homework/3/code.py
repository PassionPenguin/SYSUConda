original_list = [0, 1593, 5385, 14294, 42149, 182419]  # 滚键盘
insert_num = int(input())

for i in range(len(original_list) - 1, -1, -1):
    print(i)
    print(original_list[i])
    if i == 0:
        original_list.insert(1, insert_num)  # 如果遍历完成了还没有添加，证明最小，扔到最前面
    elif original_list[i] > insert_num:
        continue  # 不是最小，继续扔
    else:
        original_list.insert(i + 1, insert_num)
        break  # 是最小的，扔掉吧没救了

print(original_list)

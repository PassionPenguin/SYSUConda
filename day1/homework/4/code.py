n = int(input())
l = list(range(1, n + 1))
print(l)
while len(l) > 2:
    j = 0
    i = 0
    while i < len(l):
        j += 1
        if j == 3:
            l.remove(l[i])
            i += 1  # 弥补删除的元素
            j = 0
        i += 1

print(l)

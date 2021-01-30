import itertools

for i in itertools.permutations('xyz'):  # 创造排列组合
    if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':  # 判断是否 [0] <=> X 以及 [2] <=> X / Z
        print('a vs %s, b vs %s, c vs %s' % (i[0], i[1], i[2]))

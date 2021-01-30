# SYSU Project
# Copyright PassionPenguin

def div_prime(num):
    print(str(num), end=" = ")

    lt = []  # 质因数
    while num != 1:
        for i in range(2, int(num + 1)):  # 从 2 开始递增直到 num + 1
            if num % i == 0:  # i 是 num 的一个质因数
                lt.append(str(i))
                num = num / i  # 将 num 除以 i，剩下的部分继续分解
                break

    print('*'.join(iter(lt)))


div_prime(int(input()))

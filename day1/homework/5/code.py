from math import floor

encrypt_n = int(input())


def encrypt(n):
    # [(floor(n / 1000) + 5) % 10, (floor(n / 100 % 10) + 5) % 10, (floor(n / 10 % 10) + 5) % 10, (n % 10 + 5) % 10]
    l = [(n % 10 + 5) % 10, (floor(n / 10 % 10) + 5) % 10, (floor(n / 100 % 10) + 5) % 10,
         (floor(n / 1000) + 5) % 10]  # 取余运算，不可逆
    return l[0] * 1000 + l[1] * 100 + l[2] * 10 + l[3]


print(encrypt(encrypt_n))

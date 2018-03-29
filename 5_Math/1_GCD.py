#-*- coding: utf-8 -*-
# 구글 면접 대비 1 - GCD

"""
기본 출처 : https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

최대 공약수를 빠르게 찾는 GCD와 조합에서 잘 쓰이는 역원을 위한 확장 유클리드
"""

def GCD(a, b):
    while a % b != 0:
        a %= b
        a, b = b, a
    return b

print (GCD(7, 3))

# ax + by = GCD(a, b)
def ExtendedGCD(a, m):
    if m == 1: return 0

    m0 = m
    x = 1
    y = 0

    while a > 1:
        q = a // m
        a, m = m, a % m
        x, y = y, x - q * y

    x = (x + m0) % m0
    return x

print (ExtendedGCD(13, 5))
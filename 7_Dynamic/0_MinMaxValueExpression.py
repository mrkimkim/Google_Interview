#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/minimum-maximum-values-expression/

[문] - 1*2*3*4+1+2+3*4와 같은 수식이 주어질 때 괄호를 사용하여 가장 큰 값을 출력하고,
그에 대한 괄호문을 출력하여라.

[입력]
1. 스트링
2. 트리
"""

def calc(a, b, exp):
    if exp == '+': return a + b
    return a * b

def Func(s):
    s += "="
    num = []
    exp = []
    n_min = ord('0')
    n_max = ord('9')

    # Parse String
    i = 0
    while i < len(s):
        tmp = 0
        while ord(s[i]) >= n_min and ord(s[i]) <= n_max:
            tmp = tmp * 10 + int(s[i])
            i += 1
        num.append(tmp)
        exp.append(s[i])
        i += 1

    # DP Solution O(N^3)
    N = len(num)
    D = [[0] * N for i in range(N)]

    for i in range(N): D[i][i] = num[i]

    print (num)
    print (exp)
    for L in range(2, N + 1):
        for i in range(N - L + 1):
            # D[i][k] exp D[k + 1][i + L]
            for k in range(i, i + L - 1):
                print (L, i, k, k + 1, i + L - 1)
                t = calc(D[i][k], D[k + 1][i + L - 1], exp[k])
                D[i][i + L - 1] = max(t, D[i][i + L - 1])
    print (D[0][N-1])





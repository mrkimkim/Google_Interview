#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/

[문] - 이항계수를 구하여라
"""

def Solution(n, k):
    DP = [[0] * (k + 1) for i in range(n + 1)]

    DP[0][0] = 1
    for i in range(1, n + 1):
        DP[i][0] = 1
        for j in range(1, min(k, i) + 1):
            DP[i][j] = DP[i-1][j-1]
            if i - 1 >= j: DP[i][j] += DP[i-1][j]
    return DP[n][k]

print (Solution(5,5))

"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

추가 문제 - 공간을 더 줄일 수 없나?

오로지 C(N, K)만을 구하는 거라면 가능하다.
C(N, K) = C(N-1,K) + C(N-1,K-1)인데 K를 내림차순으로 순회하면
C(N, K - 1) = C(N - 1, K - 1) + C(N - 1, K - 2)이므로
C(N, K)를 C(N - 1, K)에 넣을 수 있는 공간을 없을 수 있다.
"""

def Solution2(n, k):
    DP = [0] * (k + 1)
    DP[0] = 1 # C(0,0) = 1
    for i in range(1, n + 1):
        # C(n, 0) = 1
        for j in range(min(i, k), 0, -1):
            # C(i, j) = C(i - 1, j) + C(i - 1, j - 1)
            DP[j] = DP[j] + DP[j - 1]
    return DP[k]

print (Solution2(5, 5))



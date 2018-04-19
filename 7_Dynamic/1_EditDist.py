#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

[문] - 주어진 두 문자열 str1과 str2를 같게 만들기 위해서 연산을 수행한다.
str1에 수행가능한 연산은 DEL, INSERT, REPLACE로 모두 동일한 값을 가진다.

NULL인 경우를 고려하여 DP의 인덱스는 1부터 첫 글자를 의미한다.
DP[i][j] = str1[:i]와 str2[:j]가 같게 하기 위한 값
DP[0][j] = j와 같다
DP[0][i] = i와 같다
"""

def Solution1(a, b):
    N, M = len(a), len(b)
    DP = [[0] * (M + 1) for i in range(N + 1)]

    for i in range(N + 1): DP[i][0] = i
    for j in range(M + 1): DP[0][j] = j

    for i in range(1, N +1):
        for j in range(1, M + 1):
            if a[i - 1] == b[j - 1]:
                DP[i][j] = DP[i - 1][j - 1]
            else:
                # Replace, Delete, Insert
                DP[i][j] = 1 + min(DP[i - 1][j - 1], DP[i - 1][j], DP[i][j - 1])
    return DP[N][M]

"""
추가 문제 - Palindrom

어떤 문자열이 주어질 때 최소의 DEL을 사용해서 문자가 Palindrom이 되도록 하는 방법

A = "abcd"
B = "dcba"

0 1 2 3 4
1 2
2
3
4

"abc"
"abd"의 비교에서

i - 1은 "ab", "abd"의 비교이며 이미 이 상태에서 두 문자열을 동일하게 만들기 위한 해는
구해졌다. 따라서 "abc", "abd"에서 "ab", "abd"로 전환하기 위한 비용만 더해주면 된다는 말

[!] 새로운 관점
LCS 문제로도 이것을 풀어낼 수 있다.
두 문자의 최장 공통 부분 문자열을 찾아내면 된다.
"""


def Solution2(a, b):
    N = (len(a))
    DP = [[0] * (N + 1) for i in range(N + 1)]
    # DP[N][N]

    for i in range(N + 1): DP[i][0], DP[0][i] = i
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if a[i] == b[j]:
                DP[i][j] = DP[i - 1][j - 1]
            else:
                DP[i][j] = 1 + min(DP[i - 1][j], DP[i][j - 1])
    return DP[N][N]

"""
추가 문제 - O(N^2)을 더 개선할 수 있는 방법

K에 포커스를 맞춰보자.

DP[1][5]이고 K = 2라고 생각해보자.

"a"
"abcde"를 동일하게 만드는 작업이다.
이 작업은 어떻게 하더라도 DIST가 최소 4가 된다.
즉, 이 작업을 계산할 필요가 없다는 말이다.

따라서 i와 j의 차이는 K를 넘을 필요가 없다.

따라서 j의 from은 (1, i - K)이고 to는 (i + K, N)이다.
"""

import sys

def Solution3(a, b, K):
    N = (len(a))
    DP = [[sys.maxsize] * (N + 1) for i in range(N + 1)]
    # DP[N][N]
    for i in range(N + 1): DP[i][0], DP[0][i] = i, i
    for i in range(1, N + 1):
        for j in range(max(1, i - K), min(i + K + 1, N + 1)):
            if a[i - 1] == b[j - 1]:
                DP[i][j] = DP[i - 1][j - 1]
            else:
                DP[i][j] = 1 + min(DP[i - 1][j], DP[i][j - 1])
    return DP[N][N]

print (Solution3("abxa", "axba", 1))
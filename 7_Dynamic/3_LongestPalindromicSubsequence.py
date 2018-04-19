#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/

[문] - 가장 긴 Palindromic Subsequence를 구하여라

DP를 통해 어떻게 해결하는가

DP[i][j]는 A[i:j+1]에서의 최대 Palindromic Subsequence이다.
DP[i][j]에서 A[i] == A[j]라면 DP[i][j] = 1 + DP[i+1][j-1]이다.
그렇지 않다면 DP[i][j] = max(DP[i+1][j], DP[i][j-1])이다.

여기서 DP[i][j]를 구하기 위한 새로운 i'과 j'의 j'-i'는 j-i보다 항상 작다는 것을
알 수 있다.
"""

def Solution(a):
    N = len(a)
    DP = [[0] * N for i in range(N)]
    for i in range(N): DP[i][i] = 1
    for L in range(2, N + 1):
        for i in range(N - L + 1):
            if a[i] == a[i + L - 1]:
                DP[i][i + L - 1] = DP[i + 1][i + L - 2] + 2
            else:
                DP[i][i + L - 1] = max(DP[i + 1][i + L - 1], DP[i][i + L - 2])
    return DP[0][N-1]

print (Solution("A"))

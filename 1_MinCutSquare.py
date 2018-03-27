#-*- coding: utf-8 -*-

# 구글 면접 대비 1 - MinCutSquare

"""
기본 출처 : https://practice.geeksforgeeks.org/problems/min-cut-square/0
해당 문제는 직사각형이 주어질 때 이것을 정사각형만으로 분할하려고 한다.
이 때 최소 정사각형의 갯수를 찾아내는 것이다.

DP를 통해 해결한다. 직사각형을 가로와 세로로 자를 수 있는 경우의 수들에
대해 재귀적으로 탐색하되 이미 구해진 값은 저장하여 중복 호출을 막는다.
"""

MAX_N = 1000
DP = [[-1] * MAX_N for i in range(MAX_N)]

def Calc(A, B):
    A, B = min(A, B), max(A, B)

    if DP[A][B] > 0:
        return DP[A][B]

    if A == B:
        DP[A][B] = 1
        return 1

    MinCut = A + B + MAX_N
    for i in range(1, int(A / 2) + 1):
        if A - i > 0: MinCut = min(MinCut, Calc(i, B) + Calc(A - i, B))

    for i in range(1, int(B / 2) + 1):
        if B - i > 0: MinCut = min(MinCut, Calc(A, i) + Calc(A, B - i))

    DP[A][B] = MinCut
    return MinCut

a, b = [int(x) for x in input().split(' ')]
print (Calc(a, b))
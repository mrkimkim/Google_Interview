#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/

[문] - 가장 합이 큰 증가수열을 구하여라

DP를 통해 해결하는 방법은 O(N^2)이다.
이걸 좀 더 좋게 할 수는 없을까?

종전의 LIS를 구할 때 길이를 비교의 기준으로 했다면
이번에는 크기를 기준으로 하면 된다.

1 2 3 100 4 5 6이 있을 때
최대 값은 100이 1 + 2 + 3 + 100이 된다.

이분 검색을 도입할 수 있는 방법은 없을까?
우선 정렬을 수행해보자 O(N log N)

1 2 10 4 5 6 7 8 9 => 1 2 4 5 6 7 8 9 10
자신보다 인덱스가 낮은 모든 값들에 자기를 더한다.

"""

def Solution(arr):
    N = len(arr)
    Sum = [0] * (N + 1)
    for i in range(1, N + 1):
        Sum[i] = arr[i - 1]
        for j in range(1, i):
            if arr[i - 1] > arr[j - 1] and Sum[i] < Sum[j] + arr[i - 1]:
                Sum[i] = Sum[j] + arr[i - 1]
    print (Sum)
    return max(Sum)


print (Solution([1,3,100,4,5,6,7,8,9]))


"""
Bitonic Subsequence

증가했다가 감소하는 수열 또는 감소했다가 증가하는 수열
오로지 증가하거나 감소하기만 하더라도 상관없음

1. 오로지 증가, 오로지 감소
2. 증가했다가 감소, 감소했다가 증가

1 3 6 4 2
-5 -4 -3 -4 -5
"""

def Calc(arr):
    Ret = 0
    N = len(arr)
    DP = [[0] * 2 for i in range(N)]
    for i in range(N):
        DP[i][0] = 1
        DP[i][1] = 1
        for j in range(i):
            if arr[i] > arr[j] and DP[i][0] < 1 + DP[j][0]:
                DP[i][0] = DP[j][0] + 1
            elif arr[i] < arr[j]:
                if DP[i][1] < DP[j][0] + 1:
                    DP[i][1] = DP[j][0] + 1
                if DP[i][1] < DP[j][1] + 1:
                    DP[i][1] = DP[j][1] + 1
        Ret = max(Ret, DP[i][0], DP[i][1])
    return Ret

def Solution2(arr):
    Ret = Calc(arr)
    for i in range(len(arr)): arr[i] = -arr[i]
    Ret = max(Calc(arr), Ret)
    return Ret
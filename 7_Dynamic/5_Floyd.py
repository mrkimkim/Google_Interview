#-*- coding: utf-8 -*-
# 구글 면접 대비 7 - 다이나믹

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/

[문] - 모든 정점으로부터 다른 모든 정점까지의 최소 거리를 구하여라

Floyd는 인접행렬이 기본 베이스다
"""

import sys

def Solution(n, graph):
    INF = sys.maxsize
    Dist = [[INF] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            Dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if Dist[i][j] > Dist[i][k] + Dist[k][i]:
                    Dist[i][j] = Dist[i][k] + Dist[k][i]
    return

#-*- coding: utf-8 -*-
# 구글 면접 대비 9 - BellmanFord

"""
기본 출처 : https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
BellmanFord 알고리즘은 음수의 가중치를 가지는 간선이 있는 경우에
최단 거리를 찾아내는 알고리즘이다. 앞서 다룬 다익스트라는 간선이 양
수라는 가정하에 수행된다.

알고리즘의 시간 복잡도는 O(VE)이다.

BellmanFord는 음수 사이클을 찾아낼 수 있으며, 이외의 경로에 대해서는
최단 경로를 반환한다.

1. 시작 src를 제외한 모든 정점까지의 거리 Dist[]를 INF로 초기화
2. 아래의 동작을 |V| - 1번 수행한다.
2-1 모든 간선 u-v에 대해 dist[v] > dist[u] + weight이면 dist[v]를 업뎃
3. dist[v] > dist[u] + weight 패치가 발생하면 음수 사이클 발생

원리 : 모든 단순 경로는 길이가 |V| - 1 보다 클 수 없다.
증가 사이클이면 패치가 안될 것이지만 감소 사이클을 패치가 되므로
패치가 되는 노드는 최단 사이클에 속해있지 않다.

다만 모든 E에 대해 알고리즘을 수행하는데,
"""

import queue

class ConnectedGraph:
    def __init__(self):
        self.Graph = {}
        self.Size = 0

    def addNode(self, u):
        self.Graph[u] = []
        self.Size += 1

    def addEdge(self, u, v, w):
        # 가중치, 시점, 종점
        self.Graph[u].append((w, u, v))

    def BellmanFord(self, v):
        # 거리 초기화
        INF = 999999999999
        self.Dist = {}
        self.Negative = {}
        for node in self.Graph:
            self.Dist[node] = INF
            self.Negative[node] = False
        self.Dist[v] = 0

        # |V| - 1번의 Iteration
        for i in range(self.Size - 1):
            print (self.Dist)
            for node in self.Graph:
                if self.Dist[node] == INF: continue
                print (node)
                for edge in self.Graph[node]:
                    u, v, w = edge[1], edge[2], edge[0]
                    if self.Dist[u] + w < self.Dist[v]:
                        self.Dist[v] = self.Dist[u] + w

        # STEP 3
        Flag = True
        while Flag:
            Flag = False
            for node in self.Graph:
                for edge in self.Graph[node]:
                    u, v, w = edge[1], edge[2], edge[0]
                    if self.Dist[u] != INF and \
                            self.Dist[u] + w < self.Dist[v]:
                        if not self.Negative[v]:
                            self.Negative[v] = True
                            Flag = True

        print(self.Dist)
        for node in self.Graph:
            if not self.Negative[node]:
                print (node, self.Dist[node])

G = ConnectedGraph()
G.addNode(0)
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)

G.addEdge(0, 1, -1)
G.addEdge(0, 2, 4)
G.addEdge(1, 2, 3)
G.addEdge(1, 3, 2)
G.addEdge(1, 4, 2)
G.addEdge(3, 2, 5)
G.addEdge(3, 1, 1)
G.addEdge(4, 3, -4)

G.BellmanFord(0)

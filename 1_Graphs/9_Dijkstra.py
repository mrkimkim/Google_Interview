#-*- coding: utf-8 -*-
# 구글 면접 대비 9 - Dijkstra

"""
기본 출처 : https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
하나의 정점에서 다른 모든 정점으로 향하는 최단 경로를 구하는
알고리즘으로 '우선 순위 큐'를 쓰면 O(E log V)로 구할 수 있다.
- 매 Iteration 마다 하나의 정점에 대한 거리를 완전히 픽스한다.
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
        self.Graph[v].append((w, v, u))

    def Diskstra(self, s):
        Q = queue.PriorityQueue()
        self.Dist = {}
        self.Sets = {}
        for node in self.Graph:
            self.Dist[node] = 999999999999
            self.Sets[node] = False
        self.Dist[s] = 0

        Q.put((0, s))
        size = 1
        while size < self.Size and not Q.empty():
            # 최소 거리의 정점 중
            dist, u = Q.get()
            # 세트에 포함되지 않은 정점
            if not self.Sets[u]:
                self.Sets[u] = True
                size += 1
                # 에서 도달가능한 점들의 거리를 패치
                for edge in self.Graph[u]:
                    v, w = edge[2], edge[0]
                    if self.Dist[v] > self.Dist[u] + w:
                        self.Dist[v] = self.Dist[u] + w
                        Q.put((self.Dist[v], v))

        print (self.Dist)

G = ConnectedGraph()
G.addNode(0)
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addNode(5)
G.addNode(6)
G.addNode(7)
G.addNode(8)

G.addEdge(0, 1, 4)
G.addEdge(0, 7, 8)
G.addEdge(1, 2, 8)
G.addEdge(1, 7, 11)
G.addEdge(2, 3, 7)
G.addEdge(2, 5, 4)
G.addEdge(2, 8, 2)
G.addEdge(3, 4, 9)
G.addEdge(3, 5, 14)
G.addEdge(4, 5, 10)
G.addEdge(5, 6, 2)
G.addEdge(6, 7, 1)
G.addEdge(6, 8, 6)
G.addEdge(7, 8, 7)

G.Diskstra(0)
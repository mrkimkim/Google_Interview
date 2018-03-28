#-*- coding: utf-8 -*-

# 구글 면접 대비 5 - Longest Path in a Directed Acyclic Graph

"""
기본 출처 : https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
가중치가 주어진 DAG의 한 정점에서 다른 모든 정점으로의 최대 거리를 찾는 문제다.

일반적인 그래프에서의 Longest Path Problem은 NP-Hard이지만 DAG의 경우에만 예외다.
이 문제는 위상 정렬을 통해 해결할 수 있다. O(V+E)
"""

class DAG:
    def __init__(self):
        self.Graph = {}
        self.isRoot = {}
        self.Size = 0
        self.Stack = []

    def addNode(self, v):
        self.Graph[v] = []
        self.isRoot[v] = True
        self.Size += 1

    def addEdge(self, u, v, w):
        self.Graph[u].append((v, w))
        self.isRoot[v] = False

    def TopologicalSortUtil(self, node):
        self.isVisited[node] = True
        for (next_node, _) in self.Graph[node]:
            if not self.isVisited[next_node]:
                self.TopologicalSortUtil(next_node)
        self.Stack.append(node)


    def TopologicalSort(self):
        self.isVisited = {}
        for node in self.Graph:
            self.isVisited[node] = False

        for node in self.Graph:
            if self.isRoot[node]:
                self.TopologicalSortUtil(node)

    def LongestPath(self, v):
        # 거리 초기화
        INF = -9999999999999
        self.Dist = {}
        for node in self.Graph:
            self.Dist[node] = INF
        self.Dist[v] = 0

        # 위상 정렬
        self.TopologicalSort()

        for i in range(self.Size - 1, -1, -1):
            node = self.Stack[i]
            for (next_node, weight) in self.Graph[node]:
                if self.Dist[next_node] < self.Dist[node] + weight:
                    self.Dist[next_node] = self.Dist[node] + weight
        print (self.Dist)

G = DAG()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addNode(5)
G.addNode(6)
G.addEdge(1, 2, 5)
G.addEdge(1, 3, 3)
G.addEdge(2, 3, 2)
G.addEdge(2, 4, 6)
G.addEdge(3, 4, 7)
G.addEdge(3, 6, 4)
G.addEdge(3, 6, 2)
G.addEdge(4, 6, 1)
G.addEdge(4, 5, -1)
G.addEdge(5, 6, -2)
G.LongestPath(1)
G.LongestPath(2)
G.LongestPath(3)
G.LongestPath(4)
G.LongestPath(5)
G.LongestPath(6)
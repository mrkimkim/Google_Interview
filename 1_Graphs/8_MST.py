#-*- coding: utf-8 -*-
# 구글 면접 대비 8 - MST

"""
기본 출처 : https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
MST의 대표적인 알고리즘인 Kruskal과 Prim 알고리즘.

Kruskal은 O(E log E)의 성능, Prim은 O(E log V)의 성능으로
Dense한 그래프 (Sparse Graph)에서는 Prim을 쓰는 것이 좋다.

프림 알고리즘은 현재 연결된 정점 중에서 현재 연결되지 않은 정점
으로 향하는 간선 중 가장 적은 가중치를 가진 것을 뽑아서 추가.

크루스칼 알고리즘은 사이클을 이루지 않는 조건하에서 가장 가중치
가 작은 간선을 추가하는 것으로 Union-Find를 사용한다.
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
        self.Graph[u].append((w, u, v))
        self.Graph[v].append((w, v, u))

    def Prim(self):
        self.MST = {}
        self.Dist = {}
        Q = queue.PriorityQueue()

        for node in self.Graph:
            self.MST[node] = False
            self.Dist[node] = 99999999999999

        s = list(self.Graph.keys())[0]
        self.MST[s] = True
        self.Dist[s] = 0
        for child in self.Graph[s]:
            Q.put(child)

        MST_SIZE = 1
        while MST_SIZE < self.Size:
            # Pick Up Minimum Edge
            edge = Q.get()
            u, v, w = edge[1], edge[2], edge[0]
            if not self.MST[v]:
                print(u, v, w)
                self.MST[v] = True
                self.Dist[v] = w
                MST_SIZE += 1

                # 새롭게 구한 정점의 인접 간선을 삽입
                for child in self.Graph[v]:
                    if not self.MST[child[2]]:
                        Q.put((child[0], v, child[2]))

        print (self.MST)
        print (self.Dist)

    def getParent(self, u):
        tmp = u
        while self.Parent[u] != u:
            u = self.Parent[u]

        while self.Parent[tmp] != tmp:
            self.Parent[tmp] = u
            tmp = self.Parent[tmp]
        return u

    def Kruskal(self):
        self.MST = []
        self.Parent = {}
        for node in self.Graph:
            self.Parent[node] = node

        # 우선 순위 큐에 모든 간선을 넣는다
        Q = queue.PriorityQueue()
        for v in self.Graph:
            for edge in self.Graph[v]:
                Q.put(edge)

        NumEdge = 0
        while NumEdge < self.Size - 1 and not Q.empty():
            edge = Q.get()
            pu, pv = self.getParent(edge[1]), self.getParent(edge[2])

            if pu == pv: continue
            else:
                self.MST.append(edge)
                self.Parent[pu], self.Parent[pv] = min(pu, pv), min(pu, pv)
                NumEdge +=1

        print (self.MST)



G = ConnectedGraph()
G.addNode(0)
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)

G.addEdge(0, 1, 2)
G.addEdge(1, 2, 3)
G.addEdge(0, 3, 6)
G.addEdge(1, 3, 8)
G.addEdge(3, 4, 9)
G.addEdge(1, 4, 5)
G.addEdge(2, 4, 7)

G.Prim()
print ("===")
G.Kruskal()





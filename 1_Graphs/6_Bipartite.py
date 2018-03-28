#-*- coding: utf-8 -*-

# 구글 면접 대비 6 - Check whether a graph is Bipartite or not

"""
기본 출처 : https://www.geeksforgeeks.org/bipartite-graph/
Bypartite Graph는 주어진 그래프가 두 개의 독립된 Set로 나뉠 수 있는
그래프를 말한다. 모든 Edge (u, v)가 U와 V의 Set의 원소를 잇는 그래프
이기도 하다. 이런 형태의 Graph는 2색으로 모든 정점을 색칠할 수 있다는
특성을 가진다.

BFS를 통해 체크할 수 있다
"""

class Bipartite:
    def __init__(self):
        self.Graph = {}
        self.Size = 0

    def addNode(self, v):
        self.Graph[v] = []
        self.Size += 1

    def addEdge(self, u, v):
        self.Graph[u].append(v)
        self.Graph[v].append(u)

    def isBipartite(self):
        self.Color = {}
        for node in self.Graph:
            self.Color[node] = -1

        for node in self.Graph:
            if self.Color[node] != -1: continue

            Queue = []
            length = 1
            Queue.append(node)
            self.Color[node] = True

            while length > 0:
                cur = Queue[0]
                color = self.Color[cur]
                del Queue[0]

                for next_node in self.Graph[cur]:
                    if self.Color[next_node] == -1:
                        Queue.append(next_node)
                        self.Color[next_node] = not color
                        length += 1

                    elif self.Color[next_node] == color:
                        return False
                length -= 1

        return True

"""
실행 예제
"""

G = Bipartite()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)

G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(3, 4)
G.addEdge(4, 1)
print (G.isBipartite())
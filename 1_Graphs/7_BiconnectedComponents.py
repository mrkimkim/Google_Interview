#-*- coding: utf-8 -*-

# 구글 면접 대비 7 - Biconnected Components

"""
기본 출처 : https://www.geeksforgeeks.org/biconnected-components/
Biconnected의 정의는 Component를 구성하는 정점들 중 하나가 제거되어도
남아있는 다른 정점들이 여전히 연결된 상태인 것을 의미한다.

DFS 탐색 중 방문 정점을 Stack에 저장하고 Articulation Point를 찾는다.
Articulation Point인 정점 u에 대해 u에서 방문한 정점들은 BCC에 해당한
다. DFS가 하나의 connected component를 완료하면 스택 상의 모든 Edge
는 BCC를 구성한다.

만약 Articulation Point가 없다면 그래프는 하나의 BCC를 구성한다.
"""

"""
Find Articulation Point O(V + E) <DFS>

DFS에서 탐색은 DFS 트리의 형태로 이루어지는데, 어떤 정점 v가 다른
정점 u에 의해 발견될 때 u는 v의 parent다. 다음과 같은 조건에서 u
는 Articulation Point로 볼 수 있다.

1. u는 DFS의 루트이며 최소 두 개의 자식을 가진다.
2. u는 DFS의 루트가 아니며 자신의 자식 v의 서브트리 중 어떤 것도
u의 조상으로 향하는 Edge를 가지지 않는다.

DFS에서 사용하는 배열
parent[u]: u의 parent를 저장한다.
disc[u] : 정점의 최소 discovery time을 저장한다.
low[u] : u의 서브트리 중 가장 빠르게 탐색되는 정점

disc[u]란 u를 발견하는 최소 시간이며, low[u]는 자신을 포함한
서브 트리 중 가장 최단 시간에 발견될 수 있는 노드의 disc[v]를
의미한다. 만약 자식 v에 대해 low[v] < low[u]이면 v의 서브트
리 중에서 u의 부모. 즉, u보다 빠르게 발견되는 노드로 연결된다는
것이다. 반면에 low[v] > low[u]라면 v에서 u의 부모로 연결되는
것은 없다고 볼 수 있다.
"""

class ConnectedGraph:
    def __init__(self):
        self.Graph = {}
        self.Size = 0

    def addNode(self, v):
        self.Graph[v] = []
        self.Size += 1

    def addEdge(self, v, u):
        self.Graph[v].append(u)
        self.Graph[u].append(v)

    def findBCC(self):
        # 방문 여부를 저장
        self.visited = {}
        # 자신을 발견한 노드를 저장
        self.parent = {}
        # discovery time을 저장
        self.disc = {}
        # u에서 닿을 수 있는 정점 중 가장 적은 disc를 저장
        self.low = {}
        # AP 여부를 저장
        self.ap = {}
        # Stack 여부를 저장
        self.stack = []

        for node in self.Graph:
            self.visited[node] = False
            self.parent[node] = -1
            self.disc[node] = 0
            self.low[node] = 0
            self.ap[node] = False

        for node in self.Graph:
            if not self.visited[node]:
                self.findBCCUtil(node, 0)

        print (self.visited)
        print (self.parent)
        print (self.disc)
        print (self.low)
        print (self.ap)
        return self.ap

    def findBCCUtil(self, u, time):
        time += 1
        children = 0

        self.visited[u] = True
        self.disc[u], self.low[u] = time, time

        for v in self.Graph[u]:
            if not self.visited[v]:
                # 자식 탐색을 추가
                children += 1
                self.parent[v] = u
                self.stack.append((u, v))

                # DFS 수행
                self.findBCCUtil(v, time)

                # 수행 결과를 패치
                self.low[u] = min(self.low[v], self.low[u])

                # AP를 찾은 경우
                if (self.parent == -1 and children > 1) or\
                        (self.parent != -1 and self.low[v] > self.low[u]):
                    self.ap[u] = True
                    i = len(self.stack) - 1
                    while self.stack[i] != (u, v):
                        print (self.stack[i])
                        del self.stack[i]
                        i -= 1
                    print (self.stack[i])
                    del self.stack[i]

            elif v != self.parent[u] and self.disc[v] < self.low[u]:
                self.low[u] = min(self.low[u], self.disc[v])
                self.stack.append((u, v))
        return

G = ConnectedGraph()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addNode(5)

G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(2, 3)
G.addEdge(1, 4)
G.addEdge(4, 5)

G.findBCC()
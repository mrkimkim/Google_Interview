#-*- coding: utf-8 -*-

# 구글 면접 대비 4 - Graph Cycle

"""
기본 출처 : https://www.geeksforgeeks.org/union-find/
여기에서는 유향 그래프와 무향 그래프 둘 다에서 Cycle를 찾아
내는 방법에 대하여 다룬다
"""

# 유향 그래프 O(V)
class DirectedGraph:
    def __init__(self):
        self.Graph = {}
        self.Size = 0
        self.isCycle = False

    def addNode(self, V):
        if V in self.Graph:
            print ("Node", V, "already exists")
            return
        self.Graph[V] = []
        return

    def addEdge(self, u, v):
        self.Graph[u].append(v)
        return

    # Check Cycle with DFS
    def isCyclic(self):
        # 한 번 방문한 지점은 다시 방문할 필요가 없다.
        # 그 지점에서 가능한 모든 깊이를 이미 탐색했기 때문이다
        self.Visited = {}
        self.Stack = {}
        for key in self.Graph:
            self.Visited[key] = False
            self.Stack[key] = False

        # 사이클이 하나라도 있는지를 찾는 것
        for key in self.Graph:
            if self.DFS(key):
                self.isCycle = True
                return True
        return False


    def DFS(self, node):
        self.Visited[node] = True
        self.Stack[node] = True

        # 다음 노드의 방문에서 사이클을 찾거나
        # 현재 경로에서 방문한 지점일 경우 사이클 등장
        for next_node in self.Graph[node]:
            if self.Visited[next_node] != True and self.DFS(next_node):
                return True
            elif self.Stack[next_node]:
                return True

        # POP
        self.Stack[node] = False
        return False

"""
실행 예제
"""
G = DirectedGraph()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(2, 3)
G.addEdge(2, 4)
G.addEdge(3, 4)
G.addEdge(4, 1)
print (G.isCyclic())


# 무향 그래프 O(ElogV)
class UndirectedGraph:
    def __init__(self):
        self.Graph = {}
        self.parent = {}
        self.Edge = []
        self.Size = 0
        self.isCycle = False
        return

    def addNode(self, v):
        self.Graph[v] = []
        self.parent[v] = v
        return

    def addEdge(self, u, v):
        self.Graph[u].append(v)
        self.Graph[v].append(u)
        self.Edge.append((u, v))
        return

    def getParent(self, u):
        tmp = u
        while self.parent[tmp] != tmp:
            tmp = self.parent[tmp]
        self.parent[u] = tmp
        return tmp

    def Union(self, u, v):
        if self.parent[u] > self.parent[v]:
            self.parent[u] = self.parent[v]
        else:
            self.parent[v] = self.parent[u]

    def isCyclic(self):
        for edge in self.Edge:
            (u, v) = edge
            if self.getParent(u) == self.getParent(v):
                return True
            else:
                self.Union(u, v)
        return False

"""
실행 예제
"""
G = UndirectedGraph()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(3, 4)
G.addEdge(1, 4)
print (G.isCyclic())



# 무향 그래프 DFS(E + V)
# 모든 방문된 정점 v에 대해서 직전에 방문하지 않은
# 이미 방문된 인접한 정점 u가 존재하면 사이클 존재
# 이 알고리즘은 A<->B인 간선 2개가 존재하는 것을 탐지할 수 없기 때문에
# 이러한 경우가 없다고 가정한 상태에서 수행하여야한다.
import sys


class Edge:
    def __init__(self, dest, capacity, reverse):
        self.dest = dest
        self.flow = 0
        self.capacity = capacity
        self.reverse = reverse

class Graph:
    def __init__(self):
        self.G = {}
        self.Level = {}
        self.start = {}
        self.size = 0

    def addNode(self, u):
        self.G[u] = []
        self.Level[u] = -1
        self.start[u] = 0
        self.size += 1

    def addEdge(self, u, v, capacity):
        s1, s2 = len(self.G[v]), len(self.G[u])
        self.G[u].append(Edge(v, capacity, s1))
        self.G[v].append(Edge(u, 0, s2))

    def BFS(self, s, t):
        for key in self.Level: self.Level[key] = -1

        self.Level[s] = 0
        Visited = {}

        Q = [s]
        Len = 1

        while Len > 0:
            cur = Q[0]
            del Q[0]
            Len -= 1

            if cur not in Visited:
                Visited[cur] = True
                for edge in self.G[cur]:
                    if edge.flow < edge.capacity and self.Level[edge.dest] < 0:
                        self.Level[edge.dest] = self.Level[cur] + 1
                        Q.append(edge.dest)
                        Len += 1

        return (self.Level[t] != -1)

    def sendFlow(self, u, flow, t):
        if u == t:
            print (u, flow)
            return flow

        for i in range(self.start[u], len(self.G[u])):
            edge = self.G[u][i]
            if self.Level[edge.dest] == self.Level[u] + 1 and edge.flow < edge.capacity:
                min_flow = min(flow, edge.capacity - edge.flow)
                temp_flow = self.sendFlow(edge.dest, min_flow, t)

                if temp_flow > 0:
                    edge.flow += temp_flow
                    self.G[edge.dest][edge.reverse].flow -= temp_flow
                    print (u, temp_flow)
                    return temp_flow
            self.start[u] += 1
        return 0

    def MaxFlow(self, s, t):
        MaxFlow = 0

        # Get Level
        while self.BFS(s, t) == True:
            # Do Something
            for key in self.start: self.start[key] = 0
            MaxFlow += self.sendFlow(s, 100000000, t)

        return MaxFlow

graph = Graph()
graph.addNode(0)
graph.addNode(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addNode(5)

graph.addEdge(0, 1, 16)
graph.addEdge(0, 2, 13)
graph.addEdge(1, 2, 10)
graph.addEdge(1, 3, 12)
graph.addEdge(2, 1, 4)
graph.addEdge(2, 4, 14)
graph.addEdge(3, 2, 9)
graph.addEdge(3, 5, 20)
graph.addEdge(4, 3, 7)
graph.addEdge(4, 5, 4)

print (graph.MaxFlow(0, 5))
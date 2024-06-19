from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def bfs(self, s):
        visited = set()
        queue = deque([s])
        visited.add(s)

        while queue:
            s = queue.popleft()
            print(s, end=' ')

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.bfs(2)

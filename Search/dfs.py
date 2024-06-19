class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
g.dfs(2)

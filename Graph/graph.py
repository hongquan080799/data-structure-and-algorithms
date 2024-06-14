class Graph:
    def __init__(self):
        self.adjacency_matrix = []
        self.adjacency_list = {}
        self.edge_list = []

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
            self.adjacency_list[vertex2].append((vertex1, weight))  # For undirected graph

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list:
                self.adjacency_list[other_vertex] = [edge for edge in self.adjacency_list[other_vertex] if edge[0] != vertex]
            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1] = [edge for edge in self.adjacency_list[vertex1] if edge[0] != vertex2]
            self.adjacency_list[vertex2] = [edge for edge in self.adjacency_list[vertex2] if edge[0] != vertex1]

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        order = []

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)
                order.append(current_vertex)
                queue.extend([neighbor[0] for neighbor in self.adjacency_list[current_vertex] if neighbor[0] not in visited])
        return order

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        order = []

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                order.append(current_vertex)
                stack.extend([neighbor[0] for neighbor in self.adjacency_list[current_vertex] if neighbor[0] not in visited])
        return order

    def display_adjacency_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)

    def display_adjacency_list(self):
        print("Adjacency List:")
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")

    def display_edge_list(self):
        print("Edge List:")
        print(self.edge_list)


# Example Usage
if __name__ == "__main__":
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D']
    
    for vertex in vertices:
        graph.add_vertex(vertex)

    edges = [
        ('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 3),
        ('C', 'D', 4), ('D', 'A', 5)
    ]
    
    for edge in edges:
        graph.add_edge(*edge)

    graph.display_adjacency_matrix()
    graph.display_adjacency_list()
    graph.display_edge_list()
    
    print("BFS traversal starting from vertex 'A':", graph.bfs('A'))
    print("DFS traversal starting from vertex 'A':", graph.dfs('A'))





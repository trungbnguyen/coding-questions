# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
# Solution: use BFS from the source and find a match. Time complexity: O(n), where n is the number of vertices
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_reachable(self, source, destination):
        # at the beginning, all nodes in the graph are not visited
        visited = [False] * self.vertices

        queue = [source]
        visited[source] = True

        while queue:
            # dequeue a vertex from the queue
            adjacent_node = queue.pop()
            if adjacent_node == destination:
                return True

            # continue BFS
            # visit adjacent node in the graph and append it to the queue; and mark as visited
            for i in self.graph[adjacent_node]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        return False


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    u = 1
    v = 3
    print(g.is_reachable(u, v))

    u = 3
    v = 1
    print(g.is_reachable(u, v))


if __name__ == "__main__":
    main()

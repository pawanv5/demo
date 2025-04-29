from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph.get(node, []))

# User-defined graph input
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space-separated): ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")
bfs(graph, start)
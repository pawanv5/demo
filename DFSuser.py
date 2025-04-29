def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

# Take graph input from user
graph = {}
num_nodes = int(input("Enter number of nodes: "))

for i in range(num_nodes):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space-separated): ").split()
    graph[node] = neighbours

# Initialize visited set
visited = set()

# Input starting node
start_node = input("Enter the starting node for DFS: ")

# Perform DFS
print("Following is the Depth-First Search")
dfs(visited, graph, start_node)

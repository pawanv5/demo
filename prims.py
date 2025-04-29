INF = 9999999

# Taking number of vertices from user
N = int(input("Enter the number of nodes: "))

# Taking adjacency matrix input from user
print("Enter the adjacency matrix row by row (use space to separate numbers, use 0 for no connection):")
G = []
for i in range(N):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    G.append(row)

selected_node = [0] * N
no_edge = 0
selected_node[0] = True

# Printing for edge and weight
print("\nEdge : Weight\n")
while (no_edge < N - 1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(str(a) + "-" + str(b) + " : " + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

import heapq

# Inputting the order (n), size (m), and starting node of the graph
n, m, s = map(int, input().split(" "))
s -= 1

# Creating an empty adjacency list
adj = list(map(lambda _: [], range(n)))

# Inputting node values
vals = list(map(lambda _: input(), range(n)))

# Inputting edges
for _ in range(m):
    u, v, w = map(int, input().split(" "))
    u -= 1
    v -= 1
    
    adj[u].append((v, w))
    adj[v].append((u, w))

# Dijkstra's
## Creating a list of distances
dist = [-1] * n

## Storing previous values to
## reconstruct shortest paths
par = [0] * n
par[s] = s

## Creating a heap of nodes to process
q = [(0, s, s)]

while(len(q) > 0):
    c, i, pr = heapq.heappop(q)

    if(dist[i] >= 0): continue
    dist[i] = c
    par[i] = pr

    for j, w in adj[i]:
        heapq.heappush(q, (c + w, j, i))

# Dijkstra's Output
for i in range(n):
    rpath = []
    cur_p_node = i
    while cur_p_node != par[cur_p_node]:
        rpath.append(vals[cur_p_node])
        cur_p_node = par[cur_p_node]
    rpath.append(vals[s])
    rpath = list(reversed(rpath))

    print(f"Node {vals[i]}: Distance = {dist[i]}, Path: {' -> '.join(rpath)}")
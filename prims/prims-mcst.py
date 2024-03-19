"""
Input format:
n m
u_1 v_1 w_1
u_2 v_2 w_2
u_3 v_3 w_3
...
u_m v_m w_m

Here, each of the lines
with u_i, v_i, and w_i
represent an edge from
vertices u_i to v_i
with weight w_i
"""
import heapq

# Inputting the order (n) and size (m) of the graph
n, m = map(int, input().split(" "))

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

# Prim's MCST

## Creating a heap to track the next node to be processed
heap = [(0, 0, 0)]
heapq.heapify(heap)

## Maintaining a list of visited nodes
vis = [False] * n

## To reconstruct the tree, we must take note of the parent of each node
par = [0] * n
adj_mcst = list(map(lambda _: [], range(n)))

total_weight = 0

# Main loop: while there are items in the heap,
# Process the item in the heap that adds the least
# weight to the tree
while(len(heap) > 0):
    cost, i, prev = heapq.heappop(heap)
    
    if(vis[i]): continue
    vis[i] = True
    par[i] = prev
    total_weight += cost
    
    for j, w in adj[i]:
        heapq.heappush(heap, (w, j, i))

# Convert the parent representation into an
# adjacency list representation
for i in range(1, n):
    adj_mcst[i].append(par[i])
    adj_mcst[par[i]].append(i)

# Output of Prim's
print(f"Total Weight: {total_weight}")

for i in range(n):
    print(f"Node {vals[i]}: {', '.join(map(lambda j: vals[j], adj_mcst[i]))}")

"""
Input format:
n m
n_1
n_2
...
n_n
u_1 v_1
u_2 v_2
u_3 v_3
...
u_m v_m

Here, each of the lines
with u_i and v_i
represent a directed edge from
vertices u_i to v_i

This program does not check whether the
graph is acyclic. If the graph has a cycle,
this program will produce an incorrect answer.
"""
# Inputting the order (n) and size (m) of the graph
n, m = map(int, input().split(" "))

# Creating an empty adjacency list
adj = list(map(lambda _: [], range(n)))

# Inputting node values
vals = list(map(lambda _: input(), range(n)))

# Inputting edges
for _ in range(m):
    u, v = map(int, input().split(" "))
    u -= 1
    v -= 1
    
    adj[u].append(v)

# Toposort Algorithm
def _dfs(vis, adj, i):
    # Skip processing if this node
    # has already been visited
    if(vis[i]): return
    vis[i] = True

    # For every neighbor of the current
    # node, call dfs on its neighbors, and
    # iterate through the DFS ordering
    for j in adj[i]:
        for deffered_iter in _dfs(vis, adj, j):
            yield deffered_iter
    yield i

def toposort(adj):
    n = len(adj)

    # Creating an array to track visited nodes
    vis = [False] * n

    # This will store the result
    l = [0] * n
    
    cur_l_ind = n - 1
    for i in range(n):
        # Perform multiple DFSes,
        # merging the result of each
        # DFS into the list
        for j in _dfs(vis, adj, i):
            l[cur_l_ind] = j
            cur_l_ind -= 1
    
    # Return the answer
    return l

# Output the Topological Sort
print(f"TOPOLOGICAL SORT: {', '.join(map(lambda i: vals[i], toposort(adj)))}")
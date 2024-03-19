from collections import deque

# BFS function
def bfs(adj, s):
    q = deque()
    q.append(s)

    vis = [False] * len(adj)

    while(len(q) > 0):
        """
        Instead of popping from the right
        (as in a stack),
        we pop from the left
        (as in a queue)
        """
        i = q.popleft()

        if(vis[i]): continue
        vis[i] = True
        yield i

        for j in adj[i]:
            q.append(j)

# Inputting the order (n), size (m), and the starting node of the graph
n, m, s = map(int, input().split(" "))
s -= 1

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
    adj[v].append(u)

print(f"BFS ordering: {' '.join(map(lambda i: vals[i], bfs(adj, s)))}")
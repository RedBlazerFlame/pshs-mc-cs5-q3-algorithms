class UnionFind():
    def __init__(self, n):
        self.num_comps = n
        self.csize = [1] * n
        self.par = list(range(n))
    
    def find(self, i):
        orig = i
        while i != self.par[i]:
            i = self.par[i]
        
        while orig != self.par[orig]:
            oldpar = self.par[orig]
            self.par[orig] = i
            orig = oldpar
        
        return i
    
    def is_connected(self, i, j):
        return self.find(i) == self.find(j)
    
    def unify(self, i, j):
        if(self.is_connected(i, j)): return
        
        pari = self.find(i)
        parj = self.find(j)

        if(self.csize[pari] < self.csize[parj]):
            self.par[pari] = parj
            self.csize[parj] += self.csize[pari]
        else:
            self.par[parj] = pari
            self.csize[pari] += self.csize[parj]
        
        self.num_comps -= 1

# Inputting the order (n) and size (m) of the graph
n, m = map(int, input().split(" "))

# Creating an empty edge list
edges = []

# Inputting node values
vals = list(map(lambda _: input(), range(n)))

# Inputting edges
for _ in range(m):
    u, v, w = map(int, input().split(" "))
    u -= 1
    v -= 1
    edges.append((u, v, w))

# Kruskal's MCST
## Initialize an empty adjacency list
adj_mcst = list(map(lambda _: [], range(n)))

## Sort edges by edge weight
edges.sort(key=lambda x: x[2])

## Initialize the Union Find Data Structure
uf = UnionFind(n)

## Iterate through edges in increasing order
total_weight = 0
for u, v, w in edges:
    if(uf.is_connected(u, v)): continue
    uf.unify(u, v)
    total_weight += w
    adj_mcst[u].append(v)
    adj_mcst[v].append(u)

# Output of Kruskal's
print(f"Total Weight: {total_weight}")

for i in range(n):
    print(f"Node {vals[i]}: {', '.join(map(lambda j: vals[j], adj_mcst[i]))}")

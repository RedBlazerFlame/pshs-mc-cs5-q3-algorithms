"""
INPUT FORMAT
q
qtype1 qparams1
qtype2 qparams2
qtype3 qparams3
qtype4 qparams4

The first line is q, the number of queries
Then, q lines follow, each describing a query
qtype describes the type of query, and is one of 
PUSH, POP, or TOP

PUSH v - insert a new value v into the heap
POP - remove the minimum value
TOP - print the minimum value
"""

# Heap implementation (1-based indexing)
class Heap:
    def __init__(self, order_fn=lambda a, b: a <= b):
        self.__nodes = []
        self.__fn = order_fn # Represents the heap invariant
    
    def par(self, i):
        return (i - 1) >> 1
    
    def lchild(self, i):
        return (i << 1) + 1
    
    def rchild(self, i):
        return (i << 1) + 2

    def float(self, i):
        # Base case: floating the root does nothing
        if(i == 0): return

        # Recursive case: float if the heap
        # invariant is violated
        par_ind = self.par(i)
        par_v = self.__nodes[par_ind]
        v = self.__nodes[i]

        if(not self.__fn(par_v, v)):
            self.__nodes[par_ind], self.__nodes[i] = self.__nodes[i], self.__nodes[par_ind]
        
        self.float(par_ind)

    def sink(self, i):
        # Base case: sinking a node without children does nothing
        left_ind = self.lchild(i)
        right_ind = self.rchild(i)
        v = self.__nodes[i]

        if(left_ind >= len(self.__nodes)): return
        lv = self.__nodes[left_ind]

        # Recursive case 1: there is only one child
        if(right_ind >= len(self.__nodes)):
            if(not self.__fn(v, lv)):
                self.__nodes[i], self.__nodes[left_ind] = self.__nodes[left_ind], self.__nodes[i]
            return
        
        rv = self.__nodes[right_ind]

        # Recursive case 2: two children
        if(self.__fn(lv, rv)):
            # subcase 1: lv <= rv
            # swap with lv
            self.__nodes[i], self.__nodes[left_ind] = self.__nodes[left_ind], self.__nodes[i]
            self.sink(left_ind)
        else:
            # subcase 2: lv > rv
            # swap with rv
            self.__nodes[i], self.__nodes[right_ind] = self.__nodes[right_ind], self.__nodes[i]
            self.sink(right_ind)

    def push(self, v):
        # Add a new node to the last layer
        self.__nodes.append(v)

        # Float the new node to its proper place
        self.float(len(self.__nodes) - 1)

    def pop(self):
        # Edge case: tree is empty
        if(len(self.__nodes) == 0):
            return None

        oldv = self.__nodes[0]

        # Swap root with the last node in the last level
        self.__nodes[0], self.__nodes[-1] = self.__nodes[-1], self.__nodes[0]

        # Pop the last node in the last level
        self.__nodes.pop()

        # Sink the new root value to the proper position
        if(len(self.__nodes) > 0):
            self.sink(0)
        return oldv
    
    @property
    def top(self):
        return self.__nodes[0]

    @property
    def empty(self):
        return len(self.__nodes) == 0

# Driver code
def answer_query(qtype, qargs, min_h):
    if(qtype == "PUSH"):
        [v] = qargs
        min_h.push(v)
    elif(qtype == "POP"):
        min_h.pop()
    elif(qtype == "TOP"):
        print(min_h.top)


def main():
    # Number of queries
    q = int(input())

    min_h = Heap(order_fn = lambda a,b: a <= b) # Min heap

    for _ in range(q):
        qtype, *qargs = input().split(" ")
        answer_query(qtype, list(map(int, qargs)), min_h)

if __name__ == "__main__":
    main()
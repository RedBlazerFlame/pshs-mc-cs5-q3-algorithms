from collections import deque

class BSTNode():
    def __init__(self, v, par):
        self.v = v
        self.par = par
        self.l = None
        self.r = None
    
    """
    Inserts a new node into the BST
    """
    def insert(self, v):
        if(v <= self.v):
            # If the new value is smaller
            # Insert left
            if(self.l is None):
                self.l = BSTNode(v, self)
            else:
                self.l.insert(v)
        else:
            # If the new value is larger
            # Insert right
            if(self.r is None):
                self.r = BSTNode(v, self)
            else:
                self.r.insert(v)

    """
    Returns a reference to a node in
    the BST, returns None if not found
    """
    def search(self, v):
        if(self.v == v):
            return self
        elif(v <= self.v and self.l is not None):
            return self.l.search(v)
        elif(v > self.v and self.r is not None):
            return self.r.search(v)
    
    """
    A generator that iterates through the node values
    using preorder
    """
    def preorder(self):
        yield self.v
        if(self.l is not None):
            for i in self.l.preorder():
                yield i
        if(self.r is not None):
            for i in self.r.preorder():
                yield i
    
    """
    A generator that iterates through the node values
    using inorder
    """
    def inorder(self):
        if(self.l is not None):
            for i in self.l.inorder():
                yield i
        yield self.v
        if(self.r is not None):
            for i in self.r.inorder():
                yield i
    
    """
    A generator that iterates through the node values
    using postorder
    """
    def postorder(self):
        if(self.l is not None):
            for i in self.l.postorder():
                yield i
        if(self.r is not None):
            for i in self.r.postorder():
                yield i
        yield self.v
    
    """
    A generator that iterates through the node values
    using levelorder
    """
    def levelorder(self):
        q = deque()
        q.append(self)

        while(len(q) > 0):
            i = q.popleft()
            yield i.v
            if(i.l is not None): q.append(i.l)
            if(i.r is not None): q.append(i.r)

# Asking for inputs into the BST
n = int(input())
a = list(map(int, input().split(" ")))
bst = BSTNode(a[0], None)
bst.par = bst

for i in range(1, n):
    bst.insert(a[i])

# Various BST operations
node_42 = bst.search(42)
print(f"Parent of 42: {(None if node_42 is None else node_42.par.v)}")
print("Preorder: " + ", ".join(map(str, list(bst.preorder()))))
print("Inorder: " + ", ".join(map(str, list(bst.inorder()))))
print("Postorder: " + ", ".join(map(str, list(bst.postorder()))))
print("Levelorder: " + ", ".join(map(str, list(bst.levelorder()))))
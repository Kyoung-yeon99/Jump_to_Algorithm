import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        else:
            pNode = self.root
            while pNode is not None:
                if value < pNode.value:
                    if pNode.left is None: break
                    else: pNode = pNode.left
                else:
                    if pNode.right is None: break
                    else: pNode = pNode.right
            if value < pNode.value:
                pNode.left = node
            else:
                pNode.right = node

    def searchNode(self, value):
        pNode = self.root
        while pNode is not None:
            if value < pNode.value:
                pNode = pNode.left
            elif value > pNode.value:
                pNode = pNode.right
            else:
                return True
        return False

n, m = map(int, sys.stdin.readline().split())

tree = Tree()
count = 0

for _ in range(n):
    tree.insert(sys.stdin.readline())

for _ in range(m):
    if tree.searchNode(sys.stdin.readline()):
        count += 1

print(count)
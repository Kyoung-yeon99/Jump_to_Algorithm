# 계수 정렬
import sys 

n = int(sys.stdin.readline())
l = [0] * 10001
for _ in range(n):
    l[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if l[i] != 0:
        for _ in range(l[i]):
            print(i)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.num = 1
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         node = Node(value)
#         if self.root is None:
#             self.root = node
#             return
#         else:
#             pNode = self.root
#             while pNode is not None:
#                 if value < pNode.value:
#                     if pNode.left is None: break
#                     else: pNode = pNode.left
#                 elif value > pNode.value:
#                     if pNode.right is None: break
#                     else: pNode = pNode.right
#                 else:
#                     break
#             if value < pNode.value:
#                 pNode.left = node
#             elif value > pNode.value:
#                 pNode.right = node
#             else:
#                 pNode.num += 1

#     def inorder(self):
#         def __inorder(root):
#             if root is None:
#                 pass
#             else:
#                 __inorder(root.left)
#                 for _ in range(root.num):
#                     print(root.value)
#                 __inorder(root.right)
#         __inorder(self.root)

# n = int(sys.stdin.readline())
# tree = Tree()

# for _ in range(n):
#     tree.insert(int(sys.stdin.readline()))

# tree.inorder()
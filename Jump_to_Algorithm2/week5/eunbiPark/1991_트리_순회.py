n = int(input())
dict = {}
for _ in range(n):
    root, left, right = input().split()
    dict[root] = [left, right]


def preorder(root):
    if not root or root == '.':
        return
    print(root, end='')
    preorder((dict[root])[0])
    preorder((dict[root])[1])

def inorder(root):
    if not root or root == '.':
        return
    inorder((dict[root])[0])
    print(root, end='')
    inorder((dict[root])[1])

def postorder(root):
    if not root or root == '.':
        return
    postorder((dict[root])[0])
    postorder((dict[root])[1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
n = int(input())
tree = {}

for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]


def preorder(root): # 전위 순회
    if root != '.':
        print(root, end='')  # root 먼저
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root): # 중위 순회
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root 중간
        inorder(tree[root][1])  # right


def postorder(root): # 후위 순회
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root 먼저


preorder('A')
print()
inorder('A')
print()
postorder('A')
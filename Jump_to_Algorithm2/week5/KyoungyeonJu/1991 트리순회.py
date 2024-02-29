def preorder(r):  # 전위 순회: 루트 왼쪽 오른쪽
    if r == ".":
        return
    print(r, end="")  # 루트
    preorder(tree[r][0])  # 왼쪽
    preorder(tree[r][1])  # 오른쪽


def inorder(r):  # 중위 순회: 왼쪽 루트 오른쪽
    if r == ".":
        return
    inorder(tree[r][0])  # 왼쪽
    print(r, end="")  # 루트
    inorder(tree[r][1])  # 오른쪽


def postorder(r):  # 후위 순회: 왼쪽 오른쪽 루트
    if r == ".":
        return
    postorder(tree[r][0])  # 왼쪽
    postorder(tree[r][1])  # 오른쪽
    print(r, end="")  # 루트


n = int(input())
tree = dict()
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")


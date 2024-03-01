# 이진 트리 -> 전위 순회, 중위 순회, 후위 순회 (루트 노드: A)
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 노드의 개수
tree = {}
for _ in range(N): # 자식 노드 입력
    nodes = list(input().split())
    tree[nodes[0]] = nodes[1:]

def preorder(cur):
    global res
    l, r = tree[cur][0], tree[cur][1]
    # 부모 노드
    res += cur
    # 왼쪽 자식 노드
    if l != '.':
        preorder(l)
    # 오른쪽 자식 노드
    if r != '.':
        preorder(r)

# 중위 순회 (l -> p -> r)
def inorder(cur):
    global res
    l, r = tree[cur][0], tree[cur][1]
    # 왼쪽 자식 노드
    if l != '.':
        inorder(l)
    # 부모 노드
    res += cur
    # 오른쪽 자식 노드
    if r != '.':
        inorder(r)

def postorder(cur):
    global res
    l, r = tree[cur][0], tree[cur][1]
    # 왼쪽 자식 노드
    if l != '.':
        postorder(l)
    # 오른쪽 자식 노드
    if r != '.':
        postorder(r)
    # 부모 노드
    res += cur

res = ''
preorder('A')
print(res)

res = ''
inorder('A')
print(res)

res = ''
postorder('A')
print(res)
# 전위 순회의 첫번째 값은 루트 노드
# 중위 순회를 분할정복하자
def change(preorder, inorder):
    if inorder:
        node = preorder.pop(0)
        idx = inorder.index(node)
        change(preorder, inorder[:idx])
        change(preorder, inorder[idx + 1:])
        print(node, end=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    change(preorder, inorder)
    print()

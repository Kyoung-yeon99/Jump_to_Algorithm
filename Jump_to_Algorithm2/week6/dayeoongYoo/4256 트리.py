# 이진 트리
# 전위 순회, 중위 순회 한 결과
# 후위 순회한 결과?

# 먼저 루트 노드를 구하자
# 키포인트는 preorder일 때 가장 첫번째 요소가 루트 노드인 것
# inorder일 때 루트노드 기준으로 왼쪽이 왼쪽자식노드, 오른쪽이 오른쪽자식노드라는 것!

import sys

input = sys.stdin.readline


# 후위순회
def make_post_order(pre, in_):
    # 재귀 종료 조건: 트리가 되지 못하는 경우
    if len(pre) == 0:
        return
    elif len(pre) == 1:
        print(pre[0], end=' ')
        return
    elif len(pre) == 2:
        print(pre[1], pre[0], end=' ')
        return

    root = pre[0]  # root 노드는 전위 순회의 첫번째 요소
    mid_idx = in_.index(root)  # 중위 순회에서 루트 노드는 왼쪽 서브 트리와 오른쪽 서브 트리른 나누는 기준에 위치

    # 전위 순회
    pre_left_sub_tree = pre[1:mid_idx + 1]  # 왼쪽 서브 트리
    pre_right_sub_tree = pre[mid_idx + 1:]  # 오른쪽 서브 트리

    # 중위 순회
    in_left_sub_tree = in_[:mid_idx]  # 왼쪽 서브트리
    in_right_sub_tree = in_[mid_idx + 1:]  # 오른쪽 서브트리

    # 재귀
    make_post_order(pre_left_sub_tree, in_left_sub_tree)
    make_post_order(pre_right_sub_tree, in_right_sub_tree)

    # 출력
    print(root, end=' ')


# 입력
t = int(input())  # test case
for _ in range(t):
    n = int(input())  # 노드 수
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    make_post_order(pre_order, in_order)
    print()

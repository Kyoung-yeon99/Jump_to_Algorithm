import sys
input = sys.stdin.readline


def post_order(pre, ino):
    if len(pre) == 0:
        return
    elif len(pre) == 1:
        print(pre[0], end=" ")
        return


    # 중위 순회(root-left-right) 루트 위치 -> left 개수
    idx = ino.index(pre[0])

    # pre - idx(left 개수)를 가지고 left, right slicing
    left_pre = pre[1:idx + 1]  # 전위 순회 - left
    right_pre = pre[idx + 1:]  # 전위 순회 - right

    # in - root 기준 왼쪽, 오른쪽
    left_ino = ino[:idx]  # 중위 순회 - left
    right_ino = ino[idx + 1:]  # 중위 순회 - right

    post_order(left_pre, left_ino)
    post_order(right_pre, right_ino)

    print(pre[0], end=" ")


tc = int(input())
for _ in range(tc):
    n = int(input())
    pre = list(map(int, input().split()))  # root left right
    ino = list(map(int, input().split()))  # left root right

    post_order(pre, ino)  # left right root
    print()

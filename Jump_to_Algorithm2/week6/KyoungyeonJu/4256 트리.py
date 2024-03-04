import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    pre = list(map(int, input().split()))  # root left right
    ino = list(map(int, input().split()))  # left root right
    post = [False]*n  # left right root

    def post_order(pre, ino):
        if len(pre) == 0:
            return
        elif len(pre) == 1:
            print(pre[0], end=" ")
            return
        elif len(pre) == 2:
            print(pre[1], pre[0],end=" ")
            return

        idx = ino.index(pre[0])

        left_pre = pre[1:idx+1]
        right_pre = pre[idx+1:]

        left_ino = ino[:idx]
        right_ino = ino[idx+1:]

        post_order(left_pre, left_ino)
        post_order(right_pre, right_ino)

        print(pre[0], end=" ")


    post_order(pre, ino)

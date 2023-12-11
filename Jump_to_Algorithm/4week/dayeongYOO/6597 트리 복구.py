def get_postorder(pr_order, in_order):
    if len(pr_order) <= 1:  # 1 이하라면 return
        return pr_order

    # 전위 순회 문자열의 첫번째 문자를 중위 순회안에서 찾는다.
    root_node = in_order.index(pr_order[0])

    # 전위 순회, 중위 순회 왼쪽
    left_nodes = get_postorder(pr_order[1:root_node + 1], in_order[:root_node])
    # 중위 순회, 중위 순회 오른쪽
    right_nodes = get_postorder(pr_order[root_node + 1:], in_order[root_node + 1:])
    # 후위 순회 출력
    return left_nodes + right_nodes + pr_order[0]


# 파이썬에서 입력이 끝날 때까지 받고 종료하는 조건
while True:
    try:
        input_str = input()
        preorder, inorder = input_str.split()  # 전위순회, 중위순회
        print(get_postorder(preorder, inorder))  # 실행
    except EOFError:
        break

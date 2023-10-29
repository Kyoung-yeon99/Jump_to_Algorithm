lines = []  # 입력값을 저장할 빈 리스트

# 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 부모 노드
def postorder(inorder, preorder):
    size = len(inorder) # 문자열 길이

    if size == 1: # 문자열 길이가 1일 경우 출력
        print(preorder[0], end='')
    else:
        # preorder 기준
        root = inorder[0] # 첫번째 알파벳이 트리의 루트
        root_index = preorder.find(root)
        left_size = root_index
        right_size = size - left_size - 1

        # 루트 기준 왼쪽 트리와 오른쪽 트리에 대해 postorder 함수 재귀호출
        if left_size > 0:
            postorder(inorder[1:left_size + 1], preorder[:root_index])

        if right_size > 0:
            postorder(inorder[-right_size:], preorder[-right_size:])

        print(inorder[0], end='')

while True: # 한 줄 이상의 입력 받기
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

for line in lines: # 각 테스트 케이스에 대하여
    inorder, preorder = line.split()
    postorder(inorder, preorder) # postorder 순회 값 출력 후 줄바꿈
    print('')
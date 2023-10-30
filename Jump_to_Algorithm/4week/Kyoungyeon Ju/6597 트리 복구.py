import sys
input = sys.stdin.readline

while True: # 테스트케이스 개수를 모르기 때문에
    line = input()
    if line == "":  # 들어온 테스트케이스가 없으면
        break
    pre_order, in_order = line.split()
    result = []

    def post(pre_, in_):
        #print("pre_", pre_, "in_", in_)
        if len(pre_) == 0 or len(in_) == 0:
            #print("길이 0", "pre_", pre_, "in_", in_)
            return

        root = pre_[0]  # 전위순회의 첫 알파벳은 root
        idx = in_.find(root)
        #print("왼쪽서브트리", pre_[1:idx+1], in_[:idx])
        #print("오른쪽서브트리", pre_[idx+1:], in_[idx+1:])
        post(pre_[1:idx + 1], in_[:idx])  # 왼쪽 서브트리
        post(pre_[idx + 1:], in_[idx + 1:])  # 오른쪽 서브트리
        result.append(root)
        #print("root=", root, "result=", result)

    post(pre_order, in_order)
    print("".join(result))




# 전위 순회, 중위 순회 결과를 이용하여 후위 순회 결과 구하기
import sys
input = sys.stdin.readline
T = int(input()) # 테스트 케이스 개수
preorder, inorder, ans = [], [], []

def postorder(p, i):
    c = p[0] # 현재 부모 노드
    l = i.index(c) # 왼쪽 자식 노드의 개수
    r = len(p) - l - 1 # 오른쪽 자식 노드의 개수
    if l: 
        postorder(p[1:l+1], i[:l]) # 왼쪽 자식 노드에 대해 재귀호출
    if r: 
        postorder(p[l+1:], i[l+1:]) # 오르쪽 자식 노드에 대해 재귀호출
    ans.append(c) # 현재 노드 저장

for _ in range(T):
    n = int(input()) # 노드의 개수
    preorder = list(map(int, input().split())) # 전위 순회 결과
    inorder = list(map(int, input().split())) # 중위 순회 결과
    root = preorder[0]
    p = inorder.index(root)
    ans = [] # 후위 순회 결과 초기화
    postorder(preorder, inorder)
    print(*ans)
    


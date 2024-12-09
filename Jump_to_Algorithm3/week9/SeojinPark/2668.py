n=int(input())
x=[0]
for _ in range(n):
    x.append(int(input()))
def dfs(num):
    if visited[num] == False:
        visited[num]=True
        tmp_up.add(num)  # 현재 노드 추가
        tmp_bottom.add(x[num])  # 이동할 노드 추가
        if tmp_up == tmp_bottom:  # 싸이클이 완성되면
            ans.extend(list(tmp_bottom))  # 결과 리스트에 추가
            return
        dfs(x[num])  # 재귀 호출
ans=[]

for i in range(1, n+1):
    visited=[False]*(n+1)
    tmp_up=set()
    tmp_bottom=set()

    dfs(i)

ans=list(set(ans))
ans.sort()

print(len(ans))
[print(i) for i in ans]
n=int(input())

graph={}
for _ in range(n):
    a,b,c=map(str,input().split())
    graph[a]=(b,c)

arr=[]
def preorder(start):
    if start=='.':
        return

    arr.append(start)

    for node in graph[start]:
        preorder(node)


preorder('A')
print(''.join(arr))

arr=[]
check=[False]*26
def inorder(start):
    if start=='.':
        return

    inorder(graph[start][0])
    arr.append(start)
    inorder(graph[start][1])

inorder('A')
print(''.join(arr))

arr=[]
def postorder(start):
    if start=='.':
        return

    postorder(graph[start][0])
    postorder(graph[start][1])
    arr.append(start)

postorder('A')
print(''.join(arr))
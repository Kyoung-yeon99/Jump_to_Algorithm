# 틀림

import sys
input=sys.stdin.readline

def postorder(root,start,end):
    if start>end:
        return

    for i in range(start,end):
        if preorder[root]==inorder[i]:
            postorder(root+1,start,i)
            postorder(root+1+(i-start),i+1,end)
            print(preorder[root], end="")


while True:
    try:
        preorder,inorder=input().split()
        preorder=list(preorder) ; inorder=list(inorder)
        postorder(0,0,len(preorder))
    except:
        break
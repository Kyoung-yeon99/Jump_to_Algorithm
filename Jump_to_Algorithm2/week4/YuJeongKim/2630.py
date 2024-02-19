# 분할정복

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

white,blue=0,0

def recur(x,y,n):
    check=arr[x][y]
    global white, blue


    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != check:
                # seperate
                e = n // 2
                recur(x, y, e)
                recur(x + e, y, e)
                recur(x, y + e, e)
                recur(x + e, y + e, e)
                return

     # count
    if check == 1:
        blue += 1
    else:
        white += 1
    return



recur(0,0,n)

print(white)
print(blue)
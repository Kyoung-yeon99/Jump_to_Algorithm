little = [ int(input()) for _ in range(9)]

arr=[]
def recur(depth, start, _sum):
    if depth==7 and _sum==100:
        for i in arr:
            print(i)
        return

    for i in range(start, 9):
        arr.append(little[i])
        recur(depth+1, i+1, _sum+little[i])
        arr.remove(little[i])

recur(0,0,0)
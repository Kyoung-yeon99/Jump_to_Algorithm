arr=input()

arr=' '+arr
prefix_sum=[0]*len(arr)
for i in range(1, len(arr)):
    # 누적합
    prefix_sum[i]=prefix_sum[i-1]
    if arr[i]=='(' and arr[i+1]==')':
        prefix_sum[i]+=1

stack=[]
_sum=0
for i in range(len(arr)):
    if arr[i]=='(' and arr[i+1]!=')':
        stack.append(i)
    elif arr[i]==')' and arr[i-1]!='(':
        # 자르기
        start=stack.pop()
        _sum+=prefix_sum[i]-prefix_sum[start]+1

print(_sum)
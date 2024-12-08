n=int(input())
sol=list(map(int, input().split()))
acid = 2000000000

l,r = 0 , n-1
while l<r:
    cur_acid = sol[l]+sol[r]
    if acid >= abs(cur_acid):
        acid= abs(cur_acid)
        x=sol[l]
        y=sol[r]
    if cur_acid>0:
        r-=1
    else:
        l+=1

print(x,y)
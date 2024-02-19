x=int(input())

count=0
n=64

# 64, 32, 16, 8, 4, 2, 1로 x 만들기
while x>0:
    if x<n:
        n=n//2
    else:
        x=x-n
        count+=1

print(count)
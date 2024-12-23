import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = input()
eaten = [False]*n
result = 0

for i in range(n):
    if table[i]=='P':
        for j in range(max(0, i-k), min(n, i+k+1)):
            if table[j] == 'H' and not eaten[j]:
                eaten[j] = True
                result+=1
                break
print(result)


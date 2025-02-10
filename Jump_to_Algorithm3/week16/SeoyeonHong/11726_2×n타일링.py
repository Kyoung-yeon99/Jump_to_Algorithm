n = int(input())
count = [1, 2]

for i in range(2, n):
    count.append((count[i-2]+ count[i-1]) % 10007)

print(count[n-1])
h, w, n, m = map(int, input().split())
row = (h - 1) // (n + 1) + 1
column = (w - 1) // (m + 1) + 1
print(row*column)

# n = 1, 1 3 5
# n= 2, 1 4 7
# ax = 1+ (1+n)*(x-1)

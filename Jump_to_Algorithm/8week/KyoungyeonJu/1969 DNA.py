# Counter 사용할려고 했는데.. 틀렸음...
n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

result = ''
hs = 0
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        char = dna[j][i]
        if char == 'A': a += 1
        elif char == 'C': c += 1
        elif char == 'G': g += 1
        elif char == 'T': t += 1
    max_char = max(a, c, g, t)
    if max_char == a:
        result += 'A'
        hs += c + g + t
    elif max_char == c:
        result += 'C'
        hs += a + g + t
    elif max_char == g:
        result += 'G'
        hs += a + c + t
    elif max_char == t:
        result += 'T'
        hs += a + c + g


print(result)
print(hs)

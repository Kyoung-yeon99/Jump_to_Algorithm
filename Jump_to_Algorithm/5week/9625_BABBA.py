k = int(input())
a = [1]
b = [0]
for i in range(k): # A => B, B => AB 이므로
    a.append(b[i]) # 이전 문자열의 B의 개수만큼 A 존재
    b.append(a[i] + b[i]) # 이전 문자열의 (A 개수 + B 개수)만큼 A 존재
print(a[-1], b[-1])
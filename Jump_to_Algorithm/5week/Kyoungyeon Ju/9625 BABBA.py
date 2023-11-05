K = int(input())  # 1 <= K <= 45
dA = [0, 0, 1] + [0] * 44
dB = [0, 1, 1] + [0] * 44

print(dA[0], dA[1], dA[2], dA[3], dA[45])
print(dB[0], dB[1], dB[2], dB[3], dB[45])

for i in range(3, 46):
    dA[i] = dA[i-1] + dA[i-2]
    dB[i] = dB[i-1] + dB[i-2]

print(dA[0], dA[1], dA[2], dA[3], dA[45])
print(dB[0], dB[1], dB[2], dB[3], dB[45])

print(dA[K], dB[K])

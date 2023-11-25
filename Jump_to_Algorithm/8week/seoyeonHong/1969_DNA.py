# Hamming Distance의 합이 가장 작은 DNA s 구하기
# 두 문자열 중 각 위치의 문자가 다른 것의 개수가 적은 것 구하기
import sys
n, m = map(int, input().split()) # DNA의 수, 문자열의 길이
dna = []
nucleotide_nums = []
for _ in range(n):
    dna.append(sys.stdin.readline())
nucleotide = "ACGT"
min_dna = ""
min_dis = 0
for i in range(m):
    a, t, g, c = 0, 0, 0, 0
    for j in range(n): # i번째 문자열의 개수 확인
        if dna[j][i] == 'A':
            a += 1
        elif dna[j][i] == 'T':
            t += 1
        elif dna[j][i] == 'G':
            g += 1
        else:
            c += 1
    nucleotide_nums.append([a, c, g, t])

for i in range(m):
    maxNum = max(nucleotide_nums[i]) # 가장 많은 뉴클레오타이드 개수
    index = nucleotide_nums[i].index(maxNum) # 가장 많은 뉴클레오타이드의 인덱스(사전순)
    min_dna += nucleotide[index] # Hamming Distance가 가장 작은 문자 추가
    min_dis += sum(nucleotide_nums[i]) - maxNum # Hamming Distance 더하기

print(min_dna)
print(min_dis)

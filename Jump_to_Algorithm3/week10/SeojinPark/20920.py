import sys
n ,m = map(int, input().split())
words={}
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        if word in words:
            words[word]+=1
        else:
            words[word]=1
word_dict = sorted(words.items(),key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in word_dict:
    print(i[0])
import sys
alphabet={}
for i in range(65, 91):
    alphabet[chr(i)]=0
s=sys.stdin.readline().strip().upper()
for i in range(len(s)):
    alphabet[s[i]]+=1


max_al=max(alphabet.values())

if list(alphabet.values()).count(max_al)==1:
    for key, value in alphabet.items():
        if value==max_al:
            print(key)
else:
    print('?')
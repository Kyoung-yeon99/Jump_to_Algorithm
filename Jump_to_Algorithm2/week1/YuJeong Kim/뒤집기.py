_input=input()

zero=0
one=0

for i in range(len(_input)-1):
    if _input[i]!=_input[i+1]:
        if _input[i+1]=='1':
            zero+=1
        else:
            one+=1
# 마지막항 처리
if _input[-1]=='0':
    zero+=1
else:
    one+=1

print(min(zero,one))
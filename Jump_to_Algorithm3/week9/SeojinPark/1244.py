switch=int(input())
switch_arr = list(map(int, input().split()))
student=int(input())
students=[]
for _ in range(student):
    sex, num=map(int,input().split())
    students.append((sex,num))

for i in students:
    if i[0]==1:
        for j in range(switch):
            if (j+1)%i[1]==0:
                if switch_arr[j] == 0:
                    switch_arr[j] = 1
                else:
                    switch_arr[j] = 0
    else:
        for j in range(i[1]):
            if (i[1]-1-j)<0 or (i[1]-1+j)>=switch:
                break
            if switch_arr[i[1]-1-j] == switch_arr[i[1]-1+j]:
                if switch_arr[i[1]-1-j] == 0:
                    switch_arr[i[1] - 1 - j] = 1
                    switch_arr[i[1] - 1 + j] = 1
                else:
                    switch_arr[i[1]-1-j] = 0
                    switch_arr[i[1] - 1 + j] = 0
            else:
                break
i=0
while (i!=switch):
    if i!=0 and i%20==0:
        print()
    print(switch_arr[i], end = ' ')
    i+=1

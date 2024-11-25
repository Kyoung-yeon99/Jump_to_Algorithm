from sys import stdin
while True:
    t_list = list(map(int,stdin.readline().rstrip().split()))
    if t_list[0]==t_list[1]==t_list[2]==0:
        break
    t_list.sort()
    if t_list[2] >= t_list[0] + t_list[1]:
        print("Invalid")

    elif t_list[0]==t_list[1]==t_list[2]:
        print("Equilateral")
    elif t_list[0] == t_list[1] or t_list[1]== t_list[2]:
        print("Isosceles")
    else:
        print("Scalene")

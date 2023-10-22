import sys

n = int(sys.stdin.readline())
clist = list(map(int, sys.stdin.readline().split()))
cset = set(clist)
cset = sorted(cset)

cdict = {cset[i] : i for i in range(len(cset))}

for i in clist:
    print(cdict[i], end=' ')


# import sys

# n = int(sys.stdin.readline())
# clist = list(map(int, sys.stdin.readline().split()))
# cset = set(clist)
# cset = sorted(cset)

# for cl in clist:
#     count = 0
#     for cs in cset:
#         if cl == cs:
#             print(count, end=' ')
#             break
#         count += 1



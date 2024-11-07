from sys import stdin
M = int(stdin.readline().rstrip())

s = set()
for _ in range(M):
    commands = stdin.readline().rstrip().split()
    if len(commands) == 2 :
        item = int(commands[1])

    if commands[0] == 'add':
        s.add(item)
    if commands[0] == 'remove':
        s.discard(item)
    if commands[0] == 'check':
        if item in s:
            print(1)
        else:
            print(0)
    if commands[0] == 'toggle':
        if item in s:
            s.discard(item)
        else:
            s.add(item)
    if commands[0] == 'all':
        s = set(range(1,21))
    if commands[0] == 'empty':
        s = set()
      
#딕셔너리로 풀기
# s = dict()
# for _ in range(M):
#     commands = stdin.readline().rstrip().split()
#     if len(commands) == 2 :
#         item = int(commands[1])
#
#     if commands[0] == 'add':
#         if not s.get(item):
#             s[item] = 1
#     if commands[0] == 'remove':
#         if s.get(item):
#             s.pop(item)
#     if commands[0] == 'check':
#         if s.get(item):
#             print(1)
#         else:
#             print(0)
#     if commands[0] == 'toggle':
#         if s.get(item):
#             s.pop(item)
#         else:
#             s[item]= 1
#     if commands[0] == 'all':
#         s = dict.fromkeys(range(1,21), 1)
#     if commands[0] == 'empty':
#         s = dict()
#     #print(s)

N, S, P = map(int, input().split())
if N == 0:
  print(1)
else:
  scores = list(map(int, input().split()))

  if N==P and scores[-1]>=S:
    print(-1)
  else:
    res = N+1
    for i in range(N):
      if scores[i]<=S:
        res=i+1
        break
    print(res)
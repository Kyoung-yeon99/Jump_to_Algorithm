N = int(input())
orders = list(map(int,input().split()))
orders = [(height, ppl) for height, ppl in enumerate(orders)]
stack = [orders[0]]

i = 1
print(stack)

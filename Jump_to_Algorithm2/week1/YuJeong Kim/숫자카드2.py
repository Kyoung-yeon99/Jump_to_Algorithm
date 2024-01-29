n=int(input())
cards=list(map(int,input().split()))

m=int(input())
base_cards=list(map(int,input().split()))

cards.sort()

def findLowerBoundIndex(target):
    index=len(cards)
    left, right = 0,len(cards)-1

    while left<=right:
        mid = (left+right)//2

        if cards[mid]<target:
            left=mid+1
        else:
            right=mid-1
            index=mid
    return index

#초과 처음으로
def findUpperBoundIndex(target):
    index=len(cards)
    left, right= 0, len(cards)-1

    while left<=right:
        mid=(left+right)//2

        if cards[mid]<=target:
            left=mid+1
        else:
            right=mid-1
            index=mid
    return index

for bc in base_cards:
    lowerBoundIndex=findLowerBoundIndex(bc)
    upperBoundIndex=findUpperBoundIndex(bc)
    print(upperBoundIndex-lowerBoundIndex, end=' ')


# n=int(input())
# cards=list(map(int,input().split()))
#
# m=int(input())
# base_cards=list(map(int,input().split()))
#
# # 1. base_cards 하나씩 순회, cards에 값 있는지 확인
#
# # 2. 있으면 증가
#
# dic=dict()
# for c in cards:
#     if c in dic:
#         dic[c]+=1
#     else:
#         dic[c]=1
#
# for bc in base_cards:
#     if bc in dic:
#         print(dic[bc], end=' ')
#     else:
#         print(0, end=' ')
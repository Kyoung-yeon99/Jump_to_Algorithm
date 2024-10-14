def solution(numbers, target):
    arr=[0]
    #tmp 에 num을 각각 더하고 뺸 결과를 업데이트하면서 arr에 저장 -> 점점 늘어남 ->  target 개수만 count하기
    for num in numbers:
        tmp=[]
        for num2 in arr:
            tmp.append(num2+num)
            tmp.append(num2-num)
        arr=tmp
    return arr.count(target)

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))
def solution(numbers):
    numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    len_num = 4 #원소 크기가 1000 이하이므로 최대 늘릴 수있는 문자열의 길이 4개
    for _ in numbers:
        num = numbers.pop(0)
        numbers.append(num * len_num) #각 수를 연속해서 최대 3자리수로 만들기

    numbers.sort(key=lambda x: x[:len_num], reverse=True)

    for _ in numbers:
        num = numbers.pop(0)
        numbers.append(num[:len(num) // len_num]) #늘린 문자열의 길이를 다시 줄이기

    answer = "".join(map(str, numbers))

    if answer == '0' * len(answer): #0이면
        return '0'
    else:
        return answer

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))
print(solution([0,0,0,0]))

# def solution(numbers):
#     numbers = list(map(str,numbers)) #숫자를 문자열로 변환
#     print(numbers)
#     for _ in numbers:
#         num = numbers.pop(0)
#         numbers.append(num*4)
#
#     bucket = [[] for _ in range(10)] #나머지 결과를 담을 버킷
#     len_num = 4
#     i = 0
#
#     while i < len_num:
#         for num in numbers:   #각 수의 자리수 비교, 나머지 r 를 버킷에 append
#             #뒤에서 i 번째 수를 꺼냄,  append
#             tmp_num = num[:len_num]
#             r = int(tmp_num[-1+(-i)])
#             bucket[r].append(num)
#
#         numbers = []
#
#         for nums in bucket: #버킷의 숫자를 앞에서부터 꺼내서 numbers에 append
#             while nums :
#                 num = nums.pop(0)
#                 numbers.append(num)
#         i +=1
#
#     numbers.reverse()
#     for _ in numbers:
#         num = numbers.pop(0)
#
#         numbers.append(num[:len(num)//4])
#
#     answer = "".join(map(str,numbers))
#
#     if answer == '0'*len(answer):
#         return '0'
#     else:
#         return answer



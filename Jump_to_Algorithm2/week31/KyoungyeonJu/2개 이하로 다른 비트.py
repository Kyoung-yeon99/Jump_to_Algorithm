def solution(numbers):
    answer = []
    for number in numbers:
        answer = []
        for number in numbers:
            if number % 2 == 0:  # 짝수, 이진수에서 맨 오른쪽자리 0이므로 1 더해주기
                answer.append(number + 1)
            else:  # 홀수
                bb = "0" + bin(number)[2:]  # 0bX, 맨 앞이 1인 경우를 위해 0 앞쪽에 추가
                b = bb[::-1]  # 역순, 오른쪽에서부터 확인하기 위해
                for i in range(len(bb)):
                    if b[i] == "0":
                        # 오른쪽에서 처음으로 나오는 0을 1로, 그 오른쪽을 0로 바꾸기
                        ans = b[:i - 1] + "01" + b[i + 1:]
                        answer.append(int(ans[::-1], 2))
                        break

    return answer


"""
# 지피티 도움
(1) 가장 오른쪽에 처음으로 나오는 0을 1으로 바꾸고
(2) 그 바로 오른쪽 자리를 0으로 바꾸기
bit = (number ^ (number + 1)) >> 2  # (1)
answer.append(number + bit + 1)  # (2)

# 한 줄로
answer.append(number + (number ^ (number + 1)) >> 2 + 1)
"""
t = int(input())
for i in range(t):
    p = input() # 명령어 (r: 배열 뒤집기, d: 첫번째 수 버리기)
    n = int(input()) # 배열에 담긴 수
    input_nums = input() # 숫자 배열

    # 숫자를 배열로 변환
    input_nums = input_nums[1:-1]
    if input_nums != '':
        nums = list(map(str, input_nums.split(','))) # 이걸 str로 받는 걸 어떻게 알지?
    else:
        nums = []
    '''
    # str을 배열로 변환
    nums = []
    if n > 0:
        for i in range(1, n + 1, 2):
            nums.append(input_nums[i])
'''

    # 시초가 날 것 같단 말이지...
    ## 진짜 뒤집지 말고 idx만 뒤집기
    ## reverse_flag 사용
    reverse_flag = False
    error_flag = False
    for command in p:
        if len(nums) < 0:
            error_flag = True
            break

        if command == 'R': # 뒤집기
            reverse_flag = not reverse_flag

        elif command == 'D': # 첫번째 수 버리기
            if len(nums) <= 0:
                error_flag = True
                break

            if reverse_flag: # 뒤집혀 있으면
                nums.pop(-1)
            else:
                nums.pop(0)

    if error_flag:
        print('error')
    else:
        if reverse_flag:
            nums.reverse()
            print('[' + ','.join(nums)+']')
            # print(nums[::-1]) # 배열 그대로를 출력하면 안된다는 걸 어떻게 알지?
        else:
            print('[' + ','.join(nums) + ']')
            # print(nums)

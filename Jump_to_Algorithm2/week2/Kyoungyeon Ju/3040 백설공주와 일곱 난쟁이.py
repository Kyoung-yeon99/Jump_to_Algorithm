nums = []
for _ in range(9):
    nums.append(int(input()))

fake_sum = sum(nums) - 100  # 가짜 2개 수의 합
for i in range(8):
    for j in range(i+1, 9):
        if nums[i] + nums[j] == fake_sum:
            #print(fake_sum,i,nums[i], j,nums[j])
            nums.remove(nums[i])  # remove(값), del 리스트[idx]
            nums.remove(nums[j-1])  # nums[i]가 제거되므로 인덱스 j-1
            for a in range(7):
                print(nums[a])
            exit(0)






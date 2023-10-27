n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if nums1 == nums2:
        break
    idx = nums1.index(max(nums1[:i + 1]))
    if idx != i:
        nums1[idx], nums1[i] = nums1[i], nums1[idx]

print(1 if nums1 == nums2 else 0)
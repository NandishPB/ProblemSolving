nums = [-2,-1]

max_sum = float('-inf')
for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += nums[j]
        max_sum = max(sum , max_sum)
print(max_sum)
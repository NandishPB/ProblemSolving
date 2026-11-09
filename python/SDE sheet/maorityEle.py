nums = [2,2,2,3,3,2,2,2,1,1]
print(len(nums), len(nums)/2)

for i in range(len(nums)):
    count = 0

    for j in range(len(nums)):
        if nums[j] == nums[i]:
            count += 1 
    # print(f"count: {count}")
    if count > len(nums)/2:
        print(nums[i])




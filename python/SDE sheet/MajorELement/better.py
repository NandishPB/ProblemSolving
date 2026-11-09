nums = [6,5,5]
hashmap = {}

for i in range(len(nums)):
    curr_num = nums[i]
    if curr_num in hashmap:
        hashmap[curr_num] += 1
    else:
        hashmap[curr_num] = 1
print(hashmap)

for i in hashmap:
    if hashmap[i] > len(nums)/2:
        print(i, hashmap[i])
        
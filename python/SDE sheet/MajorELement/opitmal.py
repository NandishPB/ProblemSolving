nums = [2,2,1,1,1,2,2]

count = 0

for i in range(len(nums)):
    if count == 0:
        count = 1
        elem = nums[i]
    elif nums[i] == elem:
        count += 1
    else:
        count -= 1

elem_cnt = 0
for j in range(len(nums)):
    if nums[j] == elem:
        elem_cnt += 1

if elem_cnt > len(nums)//2:
    print(elem)


# MORE PYTHONIC 

# from collections import Counter

# count = Counter(nums)

# for i in count.keys():
#     if count[i] > len(nums)//2:
#         print(i)
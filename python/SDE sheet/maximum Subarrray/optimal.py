nums = [-2,-1]

sum = 0 
max_sum = float('-inf')
arrstart = -1
arrend = -1

for i in range(len(nums)):

    if sum == 0:
        start = i
    sum += nums[i]

    if sum > max_sum:
        max_sum = sum
        print(f"ms: {max_sum}")
        arrstart = start 
        arrend = i

    if sum < 0:
        sum = 0
print(nums[arrstart:arrend +1])
print(max_sum)
# for i in range(arrstart, arrend+1):
#     print(nums[i],end = " ")
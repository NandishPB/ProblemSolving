class Concat:
    def ConcatenationArr(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])

        print(nums)
    
sol = Concat()
sol.ConcatenationArr([1,2,3])


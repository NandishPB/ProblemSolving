class TwoSum:
    def toSum(self, nums, target):
        # hashmap = {}

        # for i, num in enumerate(nums):
        #     diff = target - num

        #     if diff in hashmap:
        #         return [hashmap[diff], i]
            
        #     hashmap[num] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# arrlist = list(map(int, input("Enter the Nums ").split()))
arrlist = [int(x) for x in input("Enter the Nums").split()]
target = int(input("Enter the target value "))

solu = TwoSum()
result = solu.toSum(arrlist, target)

print(result)
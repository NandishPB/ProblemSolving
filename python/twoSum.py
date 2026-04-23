class TwoSum:
    def toSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[num] = i

arrlist = list(map(int, input("Enter the Nums ").split()))
target = int(input("Enter the target value "))

solu = TwoSum()
result = solu.toSum(arrlist, target)

print(result)
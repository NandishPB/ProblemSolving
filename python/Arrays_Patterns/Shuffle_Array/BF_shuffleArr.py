class Shuffle:
    def shuffleArray(self, nums, n):
        i = 0
        j = n
        shuffledArray = []
        for k in range(n):
            shuffledArray.append(nums[i])
            shuffledArray.append(nums[j])
            i += 1
            j += 1
        
        print(shuffledArray)
    
sol = Shuffle()
sol.shuffleArray([1,2,3,4,5,6], 3)
            

        
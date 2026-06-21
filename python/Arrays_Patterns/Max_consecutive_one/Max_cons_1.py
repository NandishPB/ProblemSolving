class MaxOne:
    def Maximum_consecutive_one(self, nums):
        count = 0
        Maxcount = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                if Maxcount < count:
                    Maxcount = count
                count = 0
                pass
        if Maxcount < count:
            print(count)
        else:
            print(Maxcount)
       
        

result = MaxOne()
result.Maximum_consecutive_one([1,1,0,1,1,1,0,1,1,1,1,0])
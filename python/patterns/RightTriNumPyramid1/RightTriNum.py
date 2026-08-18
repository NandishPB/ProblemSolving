class RytTriNum:
    def numPattern(self, n):
        for i in range(n+1):
            for j in range(1,i+1):
                print(i, end = " ")
            print()

sol = RytTriNum()
n = 5
sol.numPattern(n)
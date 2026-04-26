class RytTriNum:
    def numPattern(self, n):
        for i in range(n+1):
            for j in range(i):
                print(i, end = " ")
            print()

sol = RytTriNum()
n = 5
sol.numPattern(n)
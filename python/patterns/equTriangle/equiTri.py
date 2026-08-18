class equilateralTriangle:
    def pattern(self, n):
        for i in range(n+1):
            # for j in range(i):
            print(" " *(n-i-1),"*"*(2*i-1), " "*(n-i-1), end = " ")
            print()

sol = equilateralTriangle()
n = 6
sol.pattern(n)
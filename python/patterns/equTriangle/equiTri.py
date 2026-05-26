class equilateralTriangle:
    def pattern(self, n):
        for i in range(n):
            # for j in range(i):
            print(" " *(n-i-1),"*"*(2*i-1), " "*(n-i-1), end = " ")
            print()

sol = equilateralTriangle()
n = 5
sol.pattern(n)
class RightTriangle:
    def pattern(self, n):
        for i in range(n):
            print(" * " * (i+1))

sol = RightTriangle()
n = 5
sol.pattern(n)
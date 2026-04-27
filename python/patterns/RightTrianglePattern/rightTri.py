# class RightTriangle:
#     def pattern(self, n):
#         for i in range(n):
#             print(" * " * (i+1))

class RightTriangle:
    def pattern(self, n):
        for i in range(n):
            for j in range(i + 1):
                print("*", end = " ")
            print()

sol = RightTriangle()
n = 5
sol.pattern(n)
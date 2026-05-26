class reverseNumberedRightTriangle:
    def numPattern(self, n):
        for i in range(n):
            for j in range(1, n-i+1):
                print(j, end = " ")
            print()

# class reverseNumberedRightTriangle:
#     def numPattern(self, n):
#         for i in range(n):
#             for j in range(n, i, -1):
#                 print(n-j+1, end = " ")
#             print()

sol = reverseNumberedRightTriangle()
n = 6
sol.numPattern(n)

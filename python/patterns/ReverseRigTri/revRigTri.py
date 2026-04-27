class ReverseRightTriangle:
    def pattern(self, n):
        for i in range(n):
            for j in range(n , i, -1):
                print("* ", end = "")
            print()

# class ReverseRightTriangle:
#     def pattern(self, n):
#         for i in range(n):
#             for j in range(n-i):
#                 print("* ",end = "")
#             print()

# class ReverseRightTriangle:
#     def pattern(self, n):
#         for i in range(n):
#             print("* " * (n - i))  

sol = ReverseRightTriangle()
n = 5
sol.pattern(n)
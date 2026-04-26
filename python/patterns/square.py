class Square:
    def pattern(self, n):
        for i in range(n):
            print("* " * n)
        print()

         

sol = Square()
n = 5 
sol.pattern(n)
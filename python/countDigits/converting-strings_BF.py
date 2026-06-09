n = int(input("Enter the number: "))
count = 0

n = str(n)

for i in n:
    n = int(n) // 10
    count += 1

print(count)
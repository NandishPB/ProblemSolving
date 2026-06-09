n = int((input("Enter the Number: ")))
count = 0
# temp = n

while n > 0:
    count += 1
    n //= 10

print(count)
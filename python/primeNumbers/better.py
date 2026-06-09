import math
n = int(input("Enter the Number: "))
divisors = []

if n<=1:
    print("The Number is not Prime Number, Enter the number greater than 1")

for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
        divisors.append(i)

        if n//i != i:
            divisors.append(n//i)

if divisors:
    divisors.append(1)
    divisors.append(n)
    print(f"The number is Not Prime Number, The divisors are {sorted(set(divisors))}")
else:
    divisors.append(1)
    divisors.append(n)
    print(f"The Number is Prime Number, The divisors are {sorted(set(divisors))}")
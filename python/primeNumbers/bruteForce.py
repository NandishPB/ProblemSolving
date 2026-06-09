n = int(input("Enter the Number: "))
divisors = []

if n <= 1:
    print("The number is not Prime Number, Enter the Number greater than 1")

for i in range(2,n):
    if n%i == 0:
        divisors.append(i)
        if n//i != i:
            divisors.append(i)
    
if divisors:
    divisors.append(1)
    divisors.append(n)
    print(f"The Number is Not prime Number, The divisors are {sorted(set(divisors))}")
else:
    divisors.append(1)
    divisors.append(n)
    print(f"The Number is Prime Nmber, The only divisors are {sorted(set(divisors))}")

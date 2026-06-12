n = 5
current_number = 1

for i in range(n):
    for j in range(i+1):
        print(current_number, end = " ")
        current_number += 1
    print()

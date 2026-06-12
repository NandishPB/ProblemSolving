def floyds_triangle(n):
    current_number = 1
    row_index = 1

    while row_index <= n:
        col_index = 1

        while col_index <= row_index:
            print(current_number, end= " ")
            current_number += 1
            col_index += 1

        print()
        row_index += 1

floyds_triangle(5)

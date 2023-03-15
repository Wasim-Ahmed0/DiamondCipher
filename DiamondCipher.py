def solution(table):
    # Check if table has elements in it
    if len(table) == 0:
        return table
    else:
        # Every odd letter is stored in this array
        first_arr = []
        # Every even letter is stored in this array
        second_arr = []

        # gets num of rows
        rowLength = len(table)

        # gets num of columns
        colLength = len(table[0])

        # separates letters into arrays above
        for i in range(1, colLength + 1):
            for j in range(1, rowLength + 1):
                if j % 2 == 0:
                    first_arr.append(table[j - 1][i - 1])
                else:
                    second_arr.append(table[j - 1][i - 1])

        # encrypt the table
        counter_1 = 0
        counter_2 = 0
        for k in range(1, rowLength + 1):
            for z in range(1, colLength + 1):
                if k % 2 == 0:
                    table[k - 1][z - 1] = second_arr[counter_1]
                    counter_1 += 1
                else:
                    table[k - 1][z - 1] = first_arr[counter_2]
                    counter_2 += 1

        return table


unencrypted_table = [["a", "b", "c"],
                     ["d", "e", "f"],
                     ["g", "h", "i"],
                     ["j", "k", "l"],
                     ["m", "n", "o"],
                     ["p", "q", "r"]]

encrypted_table = solution(unencrypted_table)

# print un-encrypted table
print("This is the table to encrypt: \n")
for row in unencrypted_table:
    print(row)


# print encrypted table
print("\nThis is the new encrypted table: \n")
for row in encrypted_table:
    print(row)

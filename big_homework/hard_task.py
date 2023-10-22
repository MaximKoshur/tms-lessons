def matrix():
    n = int(input("Size of matrix: "))
    matrix = []
    for i in range(0, n):
        lst = [int(x) for x in input().split()]
        matrix.append(lst)
    main_sum = sum(matrix[0])
    sum_line(n, main_sum, matrix)


def sum_line(n,main_sum,*args):
    matrix = args[0]
    for i in range(0,n):
        row_sum = sum(matrix[i])
        if row_sum!=main_sum:
            print(False)
            exit()
    sum_column(n, main_sum, matrix,)


def sum_column(n,main_sum,*args):
    matrix = args[0]
    column_sum = 0
    for i in range(0,n):
        for j in range(0,n):
            column_sum += matrix[j][i]
        if column_sum != main_sum:
            print(False)
            exit()
        column_sum = 0
    sum_diag(n, main_sum, matrix, )


def sum_diag(n,main_sum,*args):
    matrix = args[0]
    diag_sum_1 = 0
    diag_sum_2 = 0
    for i in range(0,n):
        diag_sum_1 += matrix[i][i]
    for i in range(0,n,):
        diag_sum_2 += matrix[i][(n-1) - i]
    if diag_sum_1 != main_sum and diag_sum_2 != main_sum:
        print(False)
        exit()
    print(True)


matrix()








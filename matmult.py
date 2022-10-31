import math

'''
calculates and returns matrix multiplication of two matrices
if matrices are not compatible, returns None
'''
def matrix_mult(a, b):
    # calculating sizes of a and b
    a_row_size = len(a)
    b_row_size = len(b)
    a_col_size = []
    b_col_size = []
    for row in a:
        a_col_size.append(len(row))
    for row in b:
        b_col_size.append(len(row))
    # checking a and b don't have rows with different length, and length of a's column = length of b's row
    if min(a_col_size) == max(a_col_size) and min(b_col_size) == max(b_col_size) \
            and a_col_size[0] == b_row_size:
        # creating matrix to store data, no. of rows = no. of rows in a, no. of columns = no. of columns in b
        temp_matrix = [[0] * b_col_size[0] for i in range(a_row_size)]
        # loop through rows of first matrix --> columns of second matrix --> elements of each row in the
        # 	columns of second matrix
        for i in range(a_row_size):
            for j in range(b_col_size[0]):
                for k in range(b_row_size):
                    temp_matrix[i][j] += a[i][k] * b[k][j]
        return temp_matrix
    return None


'''
calculates and returns Euclidean distance between two vectors
if vectors are not compatible, returns None
'''
def euclidean_dist(a, b):
    powers = 0
    if len(a[0]) == len(b[0]):
        for i in range(len(a[0])):
            powers += math.pow(a[0][i] - b[0][i], 2)
        return math.sqrt(powers)
    return None


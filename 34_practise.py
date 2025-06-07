def diagonal_sum(matrix):
    primary = 0
    secondary = 0
    for i in range (len(matrix)):
        primary += matrix[i][i]
        secondary += matrix[i][len(matrix) -1 -i]
    return primary + secondary

diagonal_sum( [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]
)
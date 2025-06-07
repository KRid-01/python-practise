def sub_diagonals(matrix):
    primary = 0
    secondary = 0

    for i in range(len(matrix)):
        primary += matrix[i][i]
        secondary += matrix[i][len(matrix )-1  -i]

    return abs(primary - secondary)

    
print(sub_diagonals([
    [11, 2,  4],
    [ 4, 5,  6],
    [10, 8, -12]
]))
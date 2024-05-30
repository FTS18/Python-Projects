def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for i in range(size):
        minor = []
        for row in matrix[1:]:
            minor_row = row[:i] + row[i+1:]
            minor.append(minor_row)
        det += (-1) ** i * matrix[0][i] * determinant(minor)
    
    return det
matrix = [[1, 2, 4, 8],
          [4, 5, 6, 9],
          [3, 6, 6, 9],
          [7, 8, 9, 1]]

print("Determinant:", determinant(matrix))

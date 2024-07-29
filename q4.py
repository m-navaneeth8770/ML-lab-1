def get_matrix_input():
    print("Enter the matrix rows, one row at a time. Use space to separate values.")
    print("Type 'done' when finished entering rows.")
    
    matrix = []
    
    while True:
        row = input("Enter row: ")
        if row.lower() == 'done':
            break
        try:
            matrix.append([int(x) for x in row.split()])
        except ValueError:
            print("Invalid input. Please enter integers only.")
    
    return matrix

def transpose_matrix(matrix):
    if not matrix:
        return []
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
  
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("All rows must have the same number of columns.")
    
    transposed = [[0] * num_rows for _ in range(num_cols)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    print("Matrix Transpose Program")
    matrix = get_matrix_input()
    
    if matrix:  
        print("Original Matrix:")
        print_matrix(matrix)
        
        transposed = transpose_matrix(matrix)
        print("Transposed Matrix:")
        print_matrix(transposed)
    else:
        print("No matrix entered.")


main()

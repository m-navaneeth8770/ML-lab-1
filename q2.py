def input_matrix(rows, cols):
    
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            raise ValueError("Row length does not match the specified number of columns.")
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
  
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            sum = 0
            for k in range(cols_A):  
                sum += A[i][k] * B[k][j]
            result[i][j] = sum
    return result

def print_matrix(matrix):
    """Prints a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    try:
        
        rows_A = int(input("Enter the number of rows for matrix A: "))
        cols_A = int(input("Enter the number of columns for matrix A: "))
        A = input_matrix(rows_A, cols_A)
        
  
        rows_B = int(input("Enter the number of rows for matrix B: "))
        cols_B = int(input("Enter the number of columns for matrix B: "))
        B = input_matrix(rows_B, cols_B)
        
    
        if cols_A != rows_B:
            print("Error: The number of columns in matrix A must be equal to the number of rows in matrix B.")
            return
        
        
        result = multiply_matrices(A, B)
        
    
        print("Product of matrices A and B is:")
        print_matrix(result)
    
    except ValueError as e:
        print(f"Input error: {e}")


main()

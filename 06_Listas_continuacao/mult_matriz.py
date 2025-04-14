def multiply_matrix_by_scalar(matrix, scalar):
    resultado = []

    for linha in matrix:
        result_linha = []
        for elemento in linha: 
            result_linha.append(elemento * scalar)
        resultado.append(result_linha)
    return resultado 

def test():
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_01 = [[3, 6, 9], [12, 15, 18], [21, 24, 27]]
    assert multiply_matrix_by_scalar(matrix_1, 3) == result_01

matrix_02 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
result_02 = [[8, 12, 16], [20, 24, 28], [32, 36, 40]]
    assert multiply_matrix_by_scalar(matrix_02, 4) == result_02

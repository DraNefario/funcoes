def imprime_diagonal(matriz):
    diagonal = [matriz[i][i] for i in range(3)]
    return diagonal

matriz_guacamole = [
    [2,5,7],
    [54,67,3],
    [5,34,23]
]

diagonal = imprime_diagonal(matriz_guacamole)

print(diagonal)
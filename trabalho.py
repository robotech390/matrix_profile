def calculoDistancia(seq1, seq2):
    soma = 0  
    
    for a, b in zip(seq1, seq2):
        diferenca = a - b  
        diferenca_quadratica = diferenca ** 2  
        soma += diferenca_quadratica  

    euclidiana = soma ** 0.5  
    return euclidiana

def matrix_profile(lista, tamanho):
    n = len(lista)
    tamanhoMatrix = n - tamanho + 1
    matrix_prof = [float('inf')] * tamanhoMatrix  

    for i in range(tamanhoMatrix):
        subLinha = lista[i:i + tamanho]  

        for j in range(tamanhoMatrix):
            if i == j: 
                continue

            subColuna = lista[j:j + tamanho]  
            dist = calculoDistancia(subLinha, subColuna)  
            matrix_prof[i] = round(min(matrix_prof[i], dist), 2)
    return matrix_prof

lista = [0,1,3,2,9,1,14,15,1,2,2,10,7]  
tamanho = 4  

vizinhos = matrix_profile(lista, tamanho)
print("Vizinhos mais Proximos:", vizinhos)

# Função que busca o menor número em um array e o armazena
def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
# Analisa cada item da lista, se o atual for menor que o anterior, ele é armazenado como o menor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# Faz um novo array com a ordenação do menor para o maior
def ordenacao_por_selecao(arr):
    novo_arr = []
# Para cada item que for considerado o menor, ele é adicionado à nova lista e tirado da lista original
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordenacao_por_selecao([5, 3, 6, 2, 10, 1, 4, 7, 12, 8]))

# Função que busca o menor número em um array e o armazena
def busca_menor(arr):
    menor = arr[0] # O menor número é o primeiro na lista
    menor_indice = 0 # Guarda a posição do menor número encontrado
# Analisa cada item da lista, se o atual for menor que o anterior, ele é armazenado como o menor
    for i in range(1, len(arr)):
        if arr[i] < menor: # Se o número da posição i for menor que o menor número até então:
            menor = arr[i] # Este número passa a ser o menor
            menor_indice = i # A posição do menor número muda
    return menor_indice

# Faz um novo array com a ordenação do menor para o maior
def ordenacao_por_selecao(arr):
    novo_arr = [] # Cria uma nova lista para os itens ordenados
# Para cada item que for considerado o menor, ele é adicionado à nova lista e tirado da lista original
    for i in range(len(arr)):
        menor = busca_menor(arr) # Encontra e retorna o índice do menor elemento da lista "arr"
        novo_arr.append(arr.pop(menor)) # Remove o menor elemento da lista "arr" e o insere na lista nova
    return novo_arr


print(ordenacao_por_selecao([5, 3, 6, 2, 10, 1, 4, 7, 12, 8]))

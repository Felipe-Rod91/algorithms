# Função que faz a soma de elementos de um array utilizando a técnica DC (dividir para conquistar)
def soma(arr):
    if len(arr) < 2: # Se o tamanho do array for 1, retorna o próprio array. Se for 0, retorna zero
        return arr[0] if arr else 0
    else: # Se o tamanho for 2 ou maior, ele pega o primeiro elemento e soma com a soma de todos os outros juntos
        return arr[0] + soma(arr[1:])

# Função que ordena arrays mais eficientemente que a de ordenação por seleção
def quicksort(arr):
    if len(arr) < 2: # Se o tamanho total do array for menor que 2, retorna o próprio array
        return arr
    else: # Se for maior que 1, ele usa o primeiro elemento do array como pivô e verifica cada outro número se é maior ou menor
        pivo = arr[0]
# Se o número for menor que o pivô, ele vai para o array dos menores, antes do pivô
        lower = [i for i in arr[1:] if i <= pivo] 
# Se o número for maior que o pivô, ele vai para o array dos maiores, depois do pivô
        higher = [i for i in arr[1:] if i >= pivo] 
# Retorna a própria função quicksort feita na lista dos menores + pivô + quicksort dos maiores 
        return quicksort(lower) + [pivo] + quicksort(higher) 


list_1 = [4, 2, 1, 6, 5, 9, 7]
list_2 = [12, 14, 9, 7, 23, 21, 19, 10]
list_3 = list(range(55, 27, -1))
print(soma(list_1))
print(soma(list_2))
print(soma(list_3))
print(quicksort(list_1))
print(quicksort(list_2))
print(quicksort(list_3))

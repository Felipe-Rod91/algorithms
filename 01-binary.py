# Função de pesquisa binária, definindo o menor e maior item da lista ordenada
def binary_search(lst, item):
    tries = 1
    low = 0 
    high = len(lst) - 1

# Caso o número não esteja na lista, ele retorna esse valor
    if item not in lst:
        return f'O número {item} não está na lista.'
    
# Enquanto o menor e o maior não forem o mesmo, é definido um item intermediário
    while low <= high:
        tries += 1
        mid = (low + high) // 2
        choice = lst[mid]
# Se o intermediário for exatamente o da lista, retorna esse mesmo item
        if choice == item:
            break
# Se o chute for maior, ele redefine o maior como o intermediário -1
        if choice > item:
            high = mid - 1
# Se o chute for menor, ele redefine o menor como o intermediário + 1
        else:
            low = mid + 1
    return f'O algoritmo achou o número {item} em {tries} tentativas.'


my_list = list(range(0, 999))
print(binary_search(my_list, 1))
print(binary_search(my_list, 566))
print(binary_search(my_list, 342))

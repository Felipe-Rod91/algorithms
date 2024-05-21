from collections import deque

# Definição do grafo (exemplo)
graph = {
    'Amanda': ['Bob', 'Claire', 'Alice'],
    'Bob': ['Anuj', 'Peggy'],
    'Claire': ['Thom', 'Jonny'],
    'Alice': ['Peggy'],
    'Anuj': [],
    'Peggy': [],
    'Thom': [],
    'Jonny': []
    }

# Função exemplo para verificar se uma pessoa é vendedora
def seller(name):
    return name[-1] == 'm'  # Exemplo: pessoa cujo nome termina com 'm' é um vendedor

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []  # Usando conjunto para verificação

    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            if seller(person):
                print(f'{person} é vendedor.')
                return True
            else:
                search_queue += graph[person]
                verified.append(person)
    return False

# Chamando a função de busca
search('Amanda')

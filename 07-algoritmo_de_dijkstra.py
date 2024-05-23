# Tabela geral, e dentro dela estão as tabelas de início até A ou B, de A ao fim, de B ao fim ou até A, vértice final, 
# custos, pais e processados
graph = {} 
graph['start'] = {'a': 2, 'b': 6}
graph['a'] = {'end': 1} 
graph['b'] = {'a': 3, 'end': 5}
graph['end'] = {} 
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'end': infinity}
parents = {'a': 'start', 'b': 'start', 'end': None}
processed = []

# Função que acha o vértice de custo mínimo
def find_lowest_cost(costs):
    lowest_cost = float('inf')
    nodo_lowest_cost = None
    # Em cada vértice, se for o vértice de menor custo até o momento e não foi processado, atribua como o novo vértice de menor custo
    for nodo in costs: 
        cost = costs[nodo]
        if cost < lowest_cost and nodo not in processed: # 
            lowest_cost = cost # 
            nodo_lowest_cost = nodo
    return nodo_lowest_cost

# Execução do algoritmo de Dijkstra
# Encontra o custo mais baixo que ainda não foi processado
nodo = find_lowest_cost(costs)
# Caso todos os vértices tenham sido processados, o laço será finalizado
while nodo is not None:
    cost = costs[nodo]
    neighbors = graph[nodo]
    # Percorre todos os vizinhos deste vértice
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Caso seja mais barato chegar a um vizinho a partir deste vértice, atualiza o custo dele e este vértice se torna o novo pai
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = nodo
    # Marca o vértice como processado e encontra o próximo vértice a ser processado, então o algoritmo é repetido
    processed.append(nodo)
    nodo = find_lowest_cost(costs)

print(f'Custos: {costs}') # Mostra os custos ao vértice final
print(f'Pais: {parents}') # Mostra os pais de cada vértice

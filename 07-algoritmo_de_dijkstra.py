graph = {}
graph['start'] = {'a': 2, 'b': 6} # A tabela de início que vai até A ou B
graph['a'] = {'end': 1} # A tabela A que vai até o fim
graph['b'] = {'a': 3, 'end': 5} # A tabela B que vai até o fim ou até o vértice A
graph['end'] = {} # Vértice final, sem vizinhos

infinity = float('inf')
costs = {'a': 6, 'b': 2, 'end': infinity}

parents = {'a': 'start', 'b': 'start', 'end': None}

processed = []

print(graph)
print(costs)

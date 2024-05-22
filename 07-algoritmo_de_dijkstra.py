graph = {}
graph['start'] = {'a': 2, 'b': 6}
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

print(graph)

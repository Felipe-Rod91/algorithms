# Conjunto de todos os Estados em que precisamos espalhar as rádios
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# Conjuntos de todas as estações e em quais Estados elas tocam
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
# Conjunto final de estações
final_stations = set()
# Enquanto houverem Estados precisando de cobertura
while states_needed:
    # Estação que cobre o maior número de Estados não cobertos
    best_station = None
    # Conjunto de Estados cobertos por alguma estação
    states_covered = set()
    for station, states_for_station in stations.items():
        # Conjunto de intersecção entre os Estados não cobertos e os Estados que essa estação abrange
        covered = states_needed & states_for_station
        # Caso abranja, essa é a nova melhor estação, e os Estados cobertos por ela entram na lista de "estados_cobertos"
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    # Atualiza "estados_abranger", retirando os Estados que já são cobertos por alguma Estação, retirando-os do algoritmo
    states_needed -= states_covered
    # Depois do loop acabar, adiciona a "melhor_estação" à lista de estações
    final_stations.add(best_station)

print(final_stations)

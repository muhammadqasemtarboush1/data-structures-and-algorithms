from graph.graph import *

def business_trip(graph, cities):
    can = True
    cost = 0
    for i in range(len(cities) - 1):
        for city in graph.get_neighbors(cities[i]):
            if cities[i + 1] == city[0]:
                cost += city[1]
                break
            else:
                can = False
    if can == False:
        cost = 0

    return f'${cost}'

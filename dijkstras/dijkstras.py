# graph = dict()

# graph["start"] = {"a":6, "b":2}

# graph["a"] = {"fin":1}

# graph["b"] = {"fin":5, "a":3}
# // ssss
# graph["fin"] = {}

inf = float("inf")

graph = {"start":{"a":6, "b":2}, "a":{"fin":1}, "b":{"fin":5, "a":3}, "fin":{}}

costs = {"a": 6, "b":2, "fin": inf}

parent = {"a":"start", "b":"start", "fin":None}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
def find():
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n]> new_cost:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print("Cost from the start to each node:")
    print(costs)
    
if __name__ == "__main__":
    find()
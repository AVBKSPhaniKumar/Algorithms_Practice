


class create_graph:
    def __init__(self,data,costs,parents):
        self.graph = data
        self.costs = costs
        self.parents = parents
        self.processed = []



class dijkstras(create_graph):

    """
    it is used when the graph with weights are given to calculate the fastest path 
    or lowest cost path

    method 
    1. find a node with lowest cost
    2. find the neighbours of that node and update the costs and parents if the costs are less from this node
    3. do this for all nodes till we reach the finish
    """

    def get_lowest_cost_node(self):
        min_cost = float("inf")
        low_cost_node = None
        for node, cost in self.costs.items():
            if node not in self.processed and cost<min_cost:
                min_cost = cost
                low_cost_node = node
        #print("min_cost, low_cost_node >> ",min_cost, low_cost_node)
        
        return low_cost_node


    def get_shortest_path(self):
        node = self.get_lowest_cost_node()
        #print("req node >> ", node)
        while node is not None:
            #print("node is ", node)
            cost = self.costs[node]
            neighbours = self.graph[node]

            for n in neighbours:
                new_cost = cost+neighbours[n]
                if new_cost < self.costs[n]:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            
            self.processed.append(node)
            node = self.get_lowest_cost_node()
        
                



data = {}
data["start"] = {}
data["start"]["a"] = 5
data["start"]["b"] = 2

data["a"] = {}
data["a"]["finish"] = 3

data["b"] = {}
data["b"]["a"] = 1
data["b"]["finish"] = 5

data["finish"] = {}

costs = {}
parents = {}

for key,val in data["start"].items():
    costs[key]=val
    parents[key]="start"

costs["finish"]=float("inf")
parents["finish"]=None

input_data = dijkstras(data,costs,parents)
input_data.get_shortest_path()

print(input_data.costs)
print(input_data.parents)
print("shorted path length = ", input_data.costs["finish"])

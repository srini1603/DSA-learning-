# adjacent matrix ,adjacent list
# we only  going to use list since it is effient

class graph:
    def __init__(self):
        self.verties = {}

    def Add_vertixies(self,vertices):
        if vertices  not in self.verties:
            self.verties[vertices] = []
            return  True
        return False
    def Add_edges(self,v1,v2):
        if v1 in self.verties.keys() and v2 in self.verties.keys() and v1 != v2:
            self.verties[v1].append(v2)
            self.verties[v2].append(v1)
            return True
        return False

    def Remove_edge(self,v1,v2):
        if v1 in self.verties.keys() and v2 in self.verties.keys() and v1 != v2 and len(v1) != 0 and len(v2) != 0:
            if v2  in self.verties[v1]:
                self.verties[v1].remove(v2)
                self.verties[v2].remove(v1)
                return True
        return False

    def Remove_vertixies(self,vertice):
        if vertice in self.verties.keys():
            for other_vertice in self.verties.[vertice]:
                self.verties[other_vertice].remove(vertice)
            del self.verties[vertice]
            return True
        return False

    def PrintAdjacent(self):
        for k in self.verties:
            print(k, ':', self.verties[k])

my_graph = graph()
my_graph.Add_vertixies('A')
my_graph.Add_vertixies('B')
my_graph.Add_vertixies('C')
my_graph.Add_edges('A','B')
my_graph.Add_edges('A','C')
my_graph.PrintAdjacent()
my_graph.Remove_edge('A','C')
print()
my_graph.PrintAdjacent()
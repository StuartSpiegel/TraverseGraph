#Stuart Spiegel
#Program traverses graph structure

import namedtuple
Edge = namedtuple('Edge', 'start , end , cost')

#function acts like a constructor
def create_Edge(start, end, cost = 1):
    return Edge(start, end, cost)

#definition for graph 
class graph:
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )
#function joins together two sets of nodes
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs
#function for removing an edge from the list
    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

#function for adding an edge to the list
    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

#function for getting neighbour edge
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours
#function traverses the built graph structure
    def traverse(self):
        nerighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            print(edge)

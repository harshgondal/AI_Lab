class adjlist:
    def __init__(self):
        self.graph={}
        self.vertices_no=0
    def add_vertex(self,v):
        if v in self.graph:
            print("vertex already exists")
        else:
            self.vertices_no=self.vertices_no+1
            self.graph[v]=[]
    def add_edge(self,v1,v2,e):
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
         print("Vertex ", v2, " does not exist.")
        else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
            temp = [v2, e]
            self.graph[v1].append(temp)
    def print_graph(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(i, " -> ", j[0], " edge weight: ", j[1])
def main():
    obj=adjlist()
    obj.add_vertex(0)
    obj.add_vertex(1)
    obj.add_vertex(2)
    obj.add_vertex(3)
    obj.add_vertex(4)
    obj.add_vertex(5)
    obj.add_edge(0,1,6)
    obj.add_edge(1, 2, 7)
    obj.add_edge(2, 1, 4)
    obj.add_edge(2, 0, 5)
    obj.add_edge(3, 2, 10)
    obj.add_edge(4,5,1)
    obj.add_edge(5,4,3)
    # print(obj.graph)
    obj.print_graph()
if __name__=="__main__":
    main()

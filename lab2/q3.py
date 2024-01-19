class matrix:
    def __init__(self):
        self.adjmatrix=[]
        self.vertices_no=0
        self.vertices=[]
    def add_vertex(self,v):
        if v in self.vertices:
            print("vertex already exists")
        else:
            self.vertices_no=self.vertices_no+1
            self.vertices.append(v)
            if self.vertices_no >1:
                for vertex in self.adjmatrix:
                    vertex.append(0)
            temp=[]
            for i  in range(self.vertices_no):
                temp.append(0)
            self.adjmatrix.append(temp)
    def add_edge(self,v1,v2):
        # if v1 not in self.adjmatrix:
        #     print("Vertex ", v1, " does not exist.")
        # elif v2 not in self.adjmatrix:
        #     print("Vertex ", v2, " does not exist.")
        # else:
        i=self.vertices.index(v1)
        j=self.vertices.index(v2)
        self.adjmatrix[i][j]=1
        self.adjmatrix[j][i]=1
    # def print(self):
    #     for i in self.vertices_no:
    #         for j in self.vertices_no:
    #             if self.adj.matrix[i][j]!=0:
    #                 print(self.adjmatrix[i][j])
def main():
    ob=matrix()
    ob.add_vertex('a')
    ob.add_vertex('b')
    ob.add_vertex('c')
    ob.add_vertex('d')
    ob.add_vertex('e')
    ob.add_edge('a','b')
    ob.add_edge('a','c')
    ob.add_edge('a','e')
    # ob.add_edge('b','a')
    ob.add_edge('b','c')
    # ob.add_edge('c','a')
    # ob.add_edge('c','b')
    ob.add_edge('c','e')
    ob.add_edge('d','c')
    # ob.add_edge('e','a')
    # ob.add_edge('e','c')
    print(ob.adjmatrix)
if __name__=="__main__":
    main()
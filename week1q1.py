class graph:
    def __init__(self):
        self.list = {}

    def addnode(self, x):
        for node in self.list:
            if node == x:
                print("already exists")
                return
        self.list.update({x:[]})
    
    def addedge(self, a, b):
        f = 0
        for node in self.list:
            if node == a:
                f=1
                if b in self.list[node]:
                    print("already exists")
                    return
                else:
                    self.list[node].append(b)
                    return
        print("not found")
        return

    def display(self):
        for a in self.list:
            for b in self.list[a]:
                print(f"({a}->{b})", end = " ")
            print("")

class stack:
    def __init__(self):
        self.l = []
    def push(self,x):
        self.l.append(x)
    def pop(self):
        self.l.pop(-1)

def dfs(g):
    s = stack()
    visit = []
    for a in g.list:
        for b in g.list[a]:
            if b not in visit:
                visit.append(b)
                s.push(b)
        if a not in visit:
            visit.append(a)
            s.push(a)    

    for a in s.l[::-1]:
        print(a)


graph = graph()
graph.addnode(0)
graph.addnode(1)
graph.addnode(2)
graph.addnode(3)
graph.addnode(4)
graph.addnode(5)

graph.addedge(3,4)
graph.addedge(4,5)
graph.addedge(1,4)
graph.addedge(5,2)
graph.addedge(3,1)
graph.addedge(1,2)


dfs(graph)




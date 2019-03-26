# Python program to print DFS traversal from a 
# given given graph 
from collections import defaultdict 
  
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self, adjacencyMat): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list)
        self.N = len(adjacencyMat) # number of vertices

        # contruct graph
        self.contruct_graph(adjacencyMat)

        # save results
        self.parent_vertices = defaultdict(list)
        self.vertices_sequence = []
        self.tree_edges = []
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    # function to contruct graph from adjency matrix
    # using addEdge() function to help
    def contruct_graph(self, adjacencyMat):
        N = len(adjacencyMat)
        for i in range(N):
            for j in range(i, N):
                if adjacencyMat[i][j] == 1:
                    self.addEdge(i, j)
  
    # A function used by DFS 
    def DFS(self, v, visited, sequence, edges): 
        # Mark the current node as visited and print it 
        visited[v]= True
        sequence.append(v)
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i] == False:
                # Record edges of DFS tree
                edges.add((v, i))

                # Record parent vertices (p) to child (c)
                # recall vertex p is parent of vertex c if vertex c is traversed from p
                self.parent_vertices[v].append(i)

                # Recursive DFS
                self.DFS(i, visited, sequence, edges) 

    ####################################################
    ## DFS Tree Traverse
    ###################################################

    # The function to do DFS traversal.
    def traverse(self): 
  
        # Mark all the vertices as not visited 
        visited = [False]*(self.N)
  
        # Call the recursive helper function to print 
        # DFS traversal
        for v in range(self.N):
            sequence, edges = [], set()
            self.DFS(v, visited, sequence, edges)
            self.vertices_sequence.append(sequence[:])
            self.tree_edges.append(edges.copy())

    ####################################################
    ## DFS Cyclic detection
    ###################################################

    def isCyclicUtil(self, v, visited, recStack): 
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True

        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.N
        recStack = [False] * self.N 
        for node in range(self.N): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False

    def display_vertices_sequence(self):
        print("Visited vertices sequence in order:")
        arr = []
        for vertices in self.vertices_sequence:
            if len(vertices)>1:
                arr += vertices
        print(arr)
        print()

    def display_vertices(self):
        print("Vertices per components:")
        count = 1
        for vertices in self.vertices_sequence:
            if len(vertices)>1:
                print("- component {}: ".format(count), end=" ")
                print(vertices)
                count +=1
        print()

    def display_parents_vertex(self):
        print("Parent vertex:")
        for k, v in self.parent_vertices.items():
            print("- parent node: {}, has childs: {}".format(k, v))
        print()

    def display_tree_edges(self):
        print("Tree Edges per components:")
        count = 1
        for edges in self.tree_edges:
            if len(edges)>=1:
                print("- Component {}: ".format(count), end=" ")
                print(edges)
                count +=1
        print()

    def display_is_cyclic(self):
        if self.isCyclic() == 1: 
            print("Graph has a cycle\n")
        else: 
            print("Graph has no cycle\n")


if __name__ == '__main__':
    adjacencyMat = [
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 0]
    ]
    G = Graph(adjacencyMat)

    # Print Traversal result
    G.traverse() 
    print()
    G.display_vertices_sequence()
    G.display_vertices()
    G.display_parents_vertex()
    G.display_tree_edges()
    G.display_is_cyclic()
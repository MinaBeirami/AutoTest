# Python program to print all paths from a source to destination.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.validPaths = defaultdict(list)

        self.count=0

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def addToPaths(self,path):
        for el in range(0,path.__len__()):
            self.validPaths[self.count].append(path[el])
        self.count+=1

    def isItAValidPath(self,path):
        if1=0
        if2=0
        if3=0
        for i in range (0, path.__len__()):
            if path[i]==2:
                # print(self.validPaths[el])
                if1=1
            elif path[i]==6:
                # print(self.validPaths[el])
                if2=1
            elif path[i]==10:
                # print(self.validPaths[el])
                if3=1
        if (if1==1 and if2==1 and if3==0):
            print('mode1')
            return False
            # self.validPaths.pop(el)
        elif (if1==1 and if2==0 and if3==1):
            print('mode2')
            return False

            # self.validPaths.pop(el)
        elif (if1==0 and if2==1 and if3==0):
            print('mode3')
            return False

            # self.validPaths.pop(el)
        else:
            return True

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            if self.isItAValidPath(path)==True:
                self.addToPaths(path)
            # print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

# Create a graph given in the above diagram
    def retunValidPaths(self):
        print(self.validPaths)
        return self.validPaths

p= Graph(21)
p.addEdge(0, 1)
p.addEdge(1, 2)
p.addEdge(1, 5)
p.addEdge(2, 3)
p.addEdge(3, 4)
p.addEdge(4, 5)
p.addEdge(5, 6)
p.addEdge(5, 9)
p.addEdge(6, 7)
p.addEdge(7, 8)
p.addEdge(8, 9)
p.addEdge(9, 10)
p.addEdge(9, 13)
p.addEdge(10, 11)
p.addEdge(11, 12)
p.addEdge(12, 13)
p.addEdge(13, 14)
p.addEdge(13, 15)
p.addEdge(14, 20)
p.addEdge(15, 16)
p.addEdge(16, 17)
p.addEdge(16, 18)
p.addEdge(17, 20)
p.addEdge(18, 19)
p.addEdge(18, 20)
p.addEdge(19, 20)

s = 0
d = 20
print("Following are all different paths from %d to %d :" % (s, d))
p.printAllPaths(s, d)
p.retunValidPaths()
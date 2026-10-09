# Task 1 ----BFS
'''
class Graph:
    def __init__(self,V):
        self.V = V
        self.adj = [[]for i in range (V)]

    def addEdge(self,v,w):
        self.adj[v] = self.adj[v] +[w]
        self.adj[w] = self.adj[w] +[v]

    def BFS(self,s):
        visited = [False] * self.V

        queue = [0] * self.V
        front = 0
        rear = 0


        visited [s] = True
        queue[rear] = s
        rear =rear + 1

        while front < rear :
            s = queue[front]
            front = front + 1

            print(s,end=" ")

# To find neighbour vertices

            i=0

            while i < len(self.adj[s]):
                w = self.adj[s][i]               # w stored neighbour

                if not visited[w]:
                   visited[w] = True
                   queue[rear] = w
                   rear = rear + 1

                i = i + 1



g = Graph(5)

g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)

print("Breadth First Traversal")
g.BFS(2)


'''

# Task 2 ------- BFS from A to G

class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        if w not in self.adj:
            self.adj[w] = []

        self.adj[v] = self.adj[v] + [w]

    def BFS(self, start, goal):
        visited = []

        queue = [""] * len(self.adj)
        front = 0
        rear = 0

        visited = visited + [start]
        queue[rear] = start
        rear = rear + 1

        while front < rear:
            s = queue[front]
            front = front + 1

            print(s, end=" ")

            if s == goal:
                print("\nGoal found!")
                return

            i = 0
            while i < len(self.adj[s]):
                w = self.adj[s][i]

                if w not in visited:
                    visited = visited + [w]
                    queue[rear] = w
                    rear = rear + 1

                i = i + 1

        print("\nGoal not found!")


# Driver program
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('I', 'L')

print("BFS Traversal starting from A:")
g.BFS('A', 'G')



# Task 3 ------Priority Queue

'''
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self,item,priority):
        self.queue.append((priority,item))

    def delete(self):
        if len(self.queue) == 0 :
            print("Queue is empty")
            return

        highest = 0

        for i in range(1,len(self.queue)):
            if self.queue[i][0]<self.queue[highest][0]:
                 highest=i

        item = self.queue.pop(highest)
        print("Deleted: " , item[1])

pq = PriorityQueue()

pq.insert("A",3)
pq.insert("B",1)
pq.insert("C",2)


pq.delete()
pq.delete()
pq.delete()
'''


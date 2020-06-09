"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            raise IndexError('key is already in the set')

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        1. create a queue
        2. starting with starting node, enqueue it
        3. while there is items in queue, do the following
        4. dequeue the first item 
        5. if not visited
        6. list it in visted set
        7. get all negiboring vertices
        8. enqueue all negiboring vertices
        9. print the dequeued item


        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            q1 = q.dequeue()
            if q1 not in visited:
                visited.add(q1)
                for each in self.get_neighbors(q1):
                    q.enqueue(each)
                print(q1)
            
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        1. create a stack and visted set
        2. starting with starting node, push it
        3. while there is items in stack, do the following
        4. pop the first item 
        5. if not visited
        6. list it in visted set
        7. get all negiboring vertices
        8. push all negiboring vertices
        9. print the poped item
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            poped = s.pop()
            if poped not in visited:
                visited.add(poped)
                for each in self.get_neighbors(poped):
                    s.push(each)
                print(poped)
    
    def dft_helper(self, visited, vertex):
        
        visited.add(vertex)
        print(vertex)
        for each in self.get_neighbors(vertex):
            if each not in visited:
                self.dft_helper(visited, each)
    


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_helper(visited, starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
      
    
        while q.size() > 0:
            path = q.dequeue() 
            last  = path[-1]
            if last not in visited:
             
                visited.add(last)
                if last == destination_vertex:
                    return path
                else:
                    for each in self.get_neighbors(last):
                        new_path =  path + [each]
                        q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])
        while s.size() > 0:

            path = s.pop()
            last = path[-1]
            if last not in visited:
                visited.add(last)
                if last == destination_vertex:
                    return path
                else:
                    for each in self.get_neighbors(last):
                        new_path = path + [each]
                        s.push(new_path)
                    

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print('\n')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('\n')
    graph.dft_recursive(1)
    print('\n')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

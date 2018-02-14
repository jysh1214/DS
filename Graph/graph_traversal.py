from get_neighbor import nbs

class GT():
    def __init__(self, adj_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.visited = []

    def dfs(self, start):
        """Depth first search
        Parameters:
            start(int): Start vertex No..

        Returns:
            self.visited(list): Record the vertices have been visited.

        Attention:
            Small vertex No. has high priority.

        Raises:
            ValueError, TypeError
        """
        self.visited.append(start)

        nb = nbs(start, self.Adjacency_Matrix)

        m = len(nb)
        for i in range(m):
            if not (nb[i] in self.visited):
                self.dfs(nb[i])

        return self.visited

    def bfs(self, start):
        """Breadth first search
        Parameters:
            start(int): Start vertex No..

        Returns:
            self.visited(list): Record the vertices have been visited.

        Attention:
            Small vertex No. has high priority.

        Raises:
            ValueError, TypeError
        """
        self.visited.append(start)

        queue = [start]
        while len(queue) != 0:
        	nb = nbs(queue[0], self.Adjacency_Matrix)
        	queue.remove(queue[0])
        	for i in range(len(nb)):
        		if not (nb[i] in self.visited):
        			self.visited.append(nb[i])
        			queue.append(nb[i])

        return self.visited

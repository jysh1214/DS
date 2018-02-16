from get_imformation import GI

class GT():
    def __init__(self, adj_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.visited = []

    def dfs(self, start, block):
        """Depth first search
        Parameters:
            start(int): Start vertex No..

            block(list): Banned vertices list.
                         Input empty list([]) first generally.

        Returns:
            self.visited(list): Record the vertices have been visited.

        Attention:
            Small vertex No. has high priority.

        Raises:
            ValueError, TypeError
        """
        self.visited.append(start)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix)
        nb = gi.get_nb(start)

        m = len(nb)
        for i in range(m):
            if not ((nb[i] in self.visited) or (nb[i] in block)):
                self.dfs(nb[i], block)

        return self.visited

    def bfs(self, start):
        """Breadth first search
        Parameters:
            start(int): Start vertex number.

        Returns:
            self.visited(list): Record the vertices have been visited.

        Attention:
            Small vertex No. has high priority.

        Raises:
            ValueError, TypeError
        """
        self.visited.append(start)
        # from get_imformation
        gi = GI(self.Adjacency_Matrix)

        queue = [start]
        while len(queue) != 0:
        	nb = gi.get_nb(queue[0])
        	queue.remove(queue[0])
        	for i in range(len(nb)):
        		if not (nb[i] in self.visited):
        			self.visited.append(nb[i])
        			queue.append(nb[i])

        return self.visited

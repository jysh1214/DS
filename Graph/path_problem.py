from get_neighbor import nbs
from graph_traversal import GT

class PT():
    def __init__(self, adj_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.all_path_list = []

    def get_path(self, v_a, v_b, path):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_b(int): Destinated vertex No..

        Returns:
            path(list): A path from v_a to v_b.
                        Input empty list([]) first generally.

        Attention:
            Don't accept fork road.

        Raises:        
            ValueError, TypeError
        """
        path.append(v_a)

        if not self.check_path(v_a, v_b, []):
            return False

        if v_a == v_b:
            return path

        # from get_neighbor
        a_nb = nbs(v_a, self.Adjacency_Matrix)
        if v_b in a_nb:
            path.append(v_b)
            return path

        if (len(a_nb)>2) or (len(a_nb)==0): return False
        else:  
            if a_nb[0] != v_a:
                next = a_nb[0]
            else:
                next = a_nb[1]

            return self.get_path(next, v_b, path)

    def all_path(self, start, v_a, v_b, visited):
        """
        Parameters:
            start(int): Input data as same as v_a first.

            v_a(int): Start vertex No..

            v_b(int): Destinated vertex No..

            visited(list):
                Record visited vertices.
                Input empty list([]) first generally.

        Returns:
            all_path_list(list): All path from v_a to v_b.

        Attention:
            Could contain loop.

        Raises:
            ValueError, TypeError
        """
        visited.append(v_a)

        if v_a == v_b:
            a = []
            a = put_all(visited, a)
            self.all_path_list.append(a)
            # print(visited)
        
        else:
            # from get_neighbor
            a_nb = nbs(v_a, self.Adjacency_Matrix)
            for i in range(len(a_nb)):
                if (not(a_nb[i] in visited)) and self.check_path(a_nb[i], v_b, visited):
                    self.all_path(a_nb[i], a_nb[i], v_b, visited)
                    visited.remove(visited[-1]) ### backtracking ###

        return self.all_path_list

    def check_path(self, v_a, v_b, block): # done
        """
        Parameters:
            v_a(int): Vertex No..

            v_b(int): Vertex No..

            block(list): Banned vertices list.
                         Int. elements difinition.

            Returns:
                bool.: Return True, if exist a path from v_a to v_b.

            Raises:
                ValueError, TypeError
        """
        if v_a == v_b:
            return True

        # from graph_traversal
        gt = GT(self.Adjacency_Matrix)
        if v_b in gt.dfs(v_a, block):
            return True
        else:
            return False

def put_all(a, b):
    for i in a:
        b.append(i)
    return b

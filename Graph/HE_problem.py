from get_imformation import GI
from graph_traversal import GT

class HE():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix
        self.N = len(self.Adjacency_Matrix)

        self.hp_list = []

    def ec(self, start):
        pass

    def hc(self, start):
        """
        """
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        dest = gi.get_pre(start)

        hc_list = []
        for i in range(len(dest)):
            temp = self.hp(start, dest[i], [])
            for j in range(len(temp)):
                temp[j].append(start)
                
            hc_list = put_all(temp, hc_list)
            self.hp_list = []

        return hc_list

    def et(self, start):
        pass

    def hp(self, v_a, v_b, visited):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_b(int): Destination vertex No..

        Returns:
            Hamiltonian path from v_a to v_b.

        Raises:
            ValueError, TypeError
        """
        visited.append(v_a)

        if v_a == v_b:
            temp = []
            temp = put_all(visited, temp)
            self.hp_list.append(temp)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        re = gi.get_re(v_a)
        
        for i in range(len(re)):
            if re[i] in visited:
                continue

            # reach v_b too early
            if (re[i]==v_b) and (len(visited)+1<self.N):
                continue

            # maybe cut two set
            left = [i for i in range(self.N)]
            left = list(set(left)-set(visited)) 
            
            flag = True
            # from graph_traversal
            gt = GT(self.Adjacency_Matrix, self.Insidence_Matrix)
            dfs = gt.dfs(left[0], visited)
            if len(dfs) != len(left):
                flag = False

            if not flag:
                continue

            self.hp(re[i], v_b, visited)
            visited.remove(visited[-1]) ### backtracking ###

        return self.hp_list

def put_all(a, b):
    for i in a:
        b.append(i)
    return b

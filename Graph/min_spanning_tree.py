from get_imformation import GI
from disjoint_set import DS

class MST():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.Insidence_Matrix = ins_matrix

    def kruskal_algo(self):
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        E = [(i, gi.get_weight(i)) for i in range(len(self.Insidence_Matrix[0]))]

        # edges sorted by weight
        E = sorted(E, key = lambda x: x[1])
        for i in range(len(E)):
            E[i] = E[i][0]

        con_ver = []
        mst = []

        for i in range(len(E)):
            (v_a, v_b) = gi.edge_term(E[i])
            
            # from disjoint_set
            ds = DS(self.Insidence_Matrix, con_ver, mst, v_a, v_b)
            if ds.same_set(v_a, v_b):
                pass # the edge is choosen or could make circle
            else:
                mst.append(E[i])
                if not (v_a in con_ver):
                    con_ver.append(v_a)
                if not (v_b in con_ver): 
                    con_ver.append(v_b)

        return mst
 
def put_all(a, b):
    for i in a:
        b.append(i)
    return b

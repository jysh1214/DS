from get_imformation import GI

class MST():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.Insidence_Matrix = ins_matrix

    def kruskal_algo(self):
        E = [i for i in range(len(self.Insidence_Matrix[0]))]

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        # edges sorted by weight
        E = sorted(E, key = lambda x: gi.get_wieght(x))
        con_ver = []
        mst = []

        i = 0
        while len(con_ver) < self.N:
            (v_a, v_b) = gi.get_term(E[i])
            if (v_a in con_ver) and (v_b in con_ver):
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

from get_imformation import GI

class DM:
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix
        self.N = len(self.Adjacency_Matrix)
    
    ### Packing: Find Maximal ###

    def clique(self):
        """
        Returns:
            Maximal clique

        Attention:
            Maximal
        """
        pass

    def indp_set(self):
        """
        Returns:
            Maximal independent set.

        Attention:
            Maximal
        """
        pass

    ### Covering: Find Minimal ###

    def dominating_set(self):
        """
        Returns:
            Minimal dominating set.

        Attention:
            Minimal
        """
        dom_set = []
        vertex = [i for i in range(self.N)]

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)

        for offset in range(self.N):
            selected = []
            non_selected = []

            while len(selected)+len(non_selected) < self.N:
                for b in range(self.N):
                    i = (b+offset)%self.N
                    if not vertex[i] in non_selected:
                        selected.append(vertex[i])
                        nb = gi.get_nb(vertex[i])
                        non_selected = list(set(nb)|set(non_selected))

            temp = []
            temp = put_all(selected, temp)
            dom_set.append(temp)

        min_ = self.N
        min_set = 0
        for i in range(len(dom_set)):
            if len(dom_set[i]) < min_:
                min_set = i

        return dom_set[min_set]
                    
    def vertex_cover(self):
        """
        Returns:
            Minimal vertex cover set.

        Attention:
            Minimal
        """
        pass

    def edge_cover(self):
        """
        Returns:
            Minimal edge cover set.

        Attention:
            Minimal
        """
        pass

def put_all(a, b):
    for i in a:
        b.append(i)
    return b

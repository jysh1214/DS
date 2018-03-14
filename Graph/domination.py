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
        # from get_information
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)

        # check every vertex are connected with each orthers
        def complete(vertex):
            for k in range(len(temp_set)):
                if not gi.check_conn(vertex, temp_set[k]):
                    return False
            
            return True

        def clique_recursion(vertex):
            nb = gi.get_nb(vertex)
            for j in range(len(nb)):
                if (not nb[j] in temp_set) and complete(nb[j]):
                    temp_set.append(nb[j])
                    clique_recursion(nb[j])


        cliq_set = []
        used_vertex = []
        vertex = [i for i in range(self.N)]

        temp_set = [] # local var.

        for offset in range(self.N):
            for b in range(self.N):
                i = (b+offset)%self.N
                
                if vertex[i] in used_vertex:
                    continue

                temp_set.append(vertex[i])
                clique_recursion(vertex[i])
                used_vertex = list(set(temp_set)|set(used_vertex))

                temp = []
                temp = put_all(temp_set, temp)
                cliq_set.append(temp)

                temp_set = []

        max_ = 0
        max_clique = 0
        for i in range(len(cliq_set)):
            if len(cliq_set[i]) > max_:
                max_ = len(cliq_set[i])
                max_clique = i

        return cliq_set[max_clique]


    def indp_set(self):
        """
        Returns:
            Maximal independent set.

        Attention:
            Maximal
        """
        in_set = []
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
            in_set.append(temp)

        max_ = 0
        max_set = 0
        for i in range(len(in_set)):
            if len(in_set[i]) > max_:
                max_ = len(in_set[i])
                max_set = i

        return in_set[max_set]


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
                min_ = len(dom_set[i])
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

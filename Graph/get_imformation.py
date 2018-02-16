class GI():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.Insidence_Matrix = ins_matrix

    def get_nb(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All neighbors of the vertex. 

        Raises:
            ValueError, TypeError
        """
        nbs_list = []
        for i in range(len(self.Adjacency_Matrix)):
            if self.Adjacency_Matrix[vertex][i] != 0:
                nbs_list.append(i)

        return nbs_list

    def get_edge(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No..

            v_b(int): Vertex No..

        Returns:
            int.: Eage No. of two vertices.

        Attention:
            Two vertices must be adjacent.

        Raises:
            ValueError, TypeError
        """
        if (self.Adjacency_Matrix[v_a][v_b]==0) and\
           (self.Adjacency_Matrix[v_b][v_a]==0):
            return False

        for i in range(len(self.Insidence_Matrix[0])):
            if (self.Insidence_Matrix[v_a][i]==1) and\
               (self.Insidence_Matrix[v_b][i]==1):
               return i

    def get_weight(self, edge):
        """
        Parameters:
            edge(int): Edge No..

        Returns: Weight of the input edge.

        Raises:
            ValueError, TypeError
        """
        (v_a, v_b) = self.edge_term(edge)

        if self.Adjacency_Matrix[v_a][v_b]:
            return self.Adjacency_Matrix[v_a][v_b]
        else:
            return self.Adjacency_Matrix[v_b][v_a]

    def edge_term(self, edge):
        temp = []
        for i in range(len(self.Insidence_Matrix)):
            if self.Insidence_Matrix[i][edge] == 1:
                temp.append(self.Insidence_Matrix[i][edge])
            if len(temp) == 2: break
        return temp
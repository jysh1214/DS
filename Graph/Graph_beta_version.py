from graph_traversal import GT
from get_imformation import GI
from min_spanning_tree import MST
from path_problem import PT
from shortest_path_problem import SP
from HE_problem import HE

class Graph():
    def __init__(self, adj_matrix, ins_matrix, V, E, region, R):
        self.N = len(adj_matrix)

        for i in range(self.N):
            if len(adj_matrix[i]) != self.N:
                print('Input data error!')
                return False

        self.Adjacency_Matrix = adj_matrix

        self.Directed = False
        for i in range(self.N):
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] !=\
                   self.Adjacency_Matrix[j][i]:
                   self.Directed = True 

        total_in_degree = 0
        for i in range(self.N):
            in_degree = 0
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] != 0:
                    in_degree += 1
            total_in_degree += in_degree

        total_out_degree = 0
        for i in range(self.N):
            out_degree = 0
            for j in range(self.N):
                if self.Adjacency_Matrix[j][i] != 0:
                    out_degree += 1
            total_out_degree += out_degree

        if self.Directed:
            self.edges = total_in_degree + total_out_degree
        else:
            # total degree = total in degree = total out degree
            self.edges = int(total_in_degree/2)

        if ins_matrix != None:
            for i in range(self.N):
                if len(ins_matrix[i]) != self.edges:
                    print('Input incidence matrix error!')
                    return False

                else: self.Insidence_Matrix = ins_matrix

        else:
            ins_matrix = [[0 for i in range(self.edges)] for j in range(self.N)]
            e = 0
            while e < self.edges:
                for i in range(self.N):
                    for j in range(i, self.N):
                        if self.Adjacency_Matrix[i][j] != 0:
                            ins_matrix[i][e] = 1
                            ins_matrix[j][e] = 1
                            e += 1

        """
        if V == None:
            self.V = [i for i in range(self.N)]
        else: self.V = V
 
        if E == None:
            self.E = [i for i in range(len(self.Insidence_Matrix[0]))]
        else: self.E = E"""

    def get_degree(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

            vertex(str): Vertex name.

        Returns:
            self.degree[vertex](int): Degree of the input vertex.

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """   
        try:
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_degree()

    def in_degree(self, vertex):
        try:
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_in_degree()

    def out_degree(self, vertex):
        try:
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_out_degree()

    def get_nb(self, vertex):
        """
        Parameters:
            vertex(int): Vertex number.

            vertex(str): Will be changed to vertex number.

        Returns:
            nb(list): All neighbors of the vertex. 

        Raises:
            ValueError, TypeError
        """
        try: 
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_nb(vertex)

    def get_re(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All reachable vertices of the vertex. 

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """
        try: 
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_reachable(vertex)

    def get_pre(self, vertex):
        """
        Parameters:
            vertex(int): Vertex No..

        Returns:
            nbs_list(list): All predecessor vertices of the vertex. 

        Attention:
            Undirected graph difinition.

        Raises:
            ValueError, TypeError
        """
        try: 
            int(vertex)
        except:
            vertex = name_to_num(vertex, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_predecessor(vertex)

    def get_edge(self, v_a, v_b):
        """
        Parameters:
            v_a(int): Vertex No..

            v_a(str): Vertex name.

            v_b(int): Vertex No..

            v_b(str): Vertex name.

        Returns:
            int.: Eage No. of two vertices.

        Attention:
            Two vertices must be adjacent.

        Raises:
            ValueError, TypeError
        """
        try:
            int(v_a)
        except:
            v_a = name_to_num(v_a, self.V)

        try:
            int(v_b)
        except:
            v_b = name_to_num(v_b, self.V)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_edge(v_a, v_b)

    def get_head(self, edge):
        pass

    def get_tail(self, edge):
        pass

    def get_weight(self, edge):
        """
        Parameters:
            edge(int): Edge No..

            edge(str): Edge name.

        Returns: Weight of the input edge.

        Raises:
            ValueError, TypeError
        """
        try:
            int(edge)
        except:
            edge = name_to_num(edge, self.E)

        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        return gi.get_weight(edge)

    def check_con(self):
        # check connected
        # return False if exist component

        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]!=0) and (i!=j):
                    return False

        return True

    def check_compl(self):
        # if the graph is complete, return True

        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]==0) and (i!=j):
                    return False

        return True

    def check_isol(self):
        # if exit isolate node, return True

        if self.check_con: return False

        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]>=1) and (i!=j):
                    return False

        return True

    def check_path(self, v_a, v_b, block): # done
        """
        Parameters:
            v_a(int): Vertex No..

            v_a(str): Vertex name.

            v_b(int): Vertex No..

            v_b(str): Vertex name.

            block(list): Banned vertices list.
                         Int. elements difinition.

        Returns:
            bool.: Return True, if exist a path from v_a to v_b.

        Raises:
            ValueError, TypeError
        """

        try:
            int(v_a)
        except:
            v_a = name_to_num(v_a, self.V)

        try:
            int(v_b)
        except:
            v_b = name_to_num(v_b, self.V)

        # from path_problem
        p = PT(self.Adjacency_Matrix)

        return p.check_path(v_a, v_b, block)

    ### graph traversal ###

    def DFS(self, start, block):
        """Depth first search
        Parameters:
            start(int): Start vertex No..

            start(str): Start vertex name.

            block(int): Banned vertex No..

            block(str): Banned vertex name.

        Attention:
            Small vertex No. has high priority.

        Returns:
            dfs(list):
        """
        try:
            int(start)
        except:
            start = name_to_num(start)

        # from graph_traversal.py
        gt = GT(self.Adjacency_Matrix)

        return gt.dfs(start, block)

    def BFS(self, start):
        """Breadth first search
        Parameters:
            start(int): Start vertex number.

            start(str): Start vertex name.    

        Attention:
            Small vertex No. has high priority.

        Returns:
            bfs(list):
        """
        try:
            int(start)
        except:
            start = name_to_num(start)

        gt = GT(self.Adjacency_Matrix)

        return gt.bfs(start)

    ### shortest path problem ###

    def Dijkstra_algo(self, start):
        """
        Returns:
            dist(list): Start vertex to all the others vertices distance.

        Attention:
            Negative weight could make misjudgment.

        Raises:
            ValueError, TypeError
        """
        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.dijkstra_algo(start)

    def Bellman_Ford_algo(self, start):
        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.bellman_ford_algo(start)

    def Floyd_Warshall_algo(self):
        # from shortest_path_problem
        sp = SP(self.Adjacency_Matrix, self.Insidence_Matrix)
        return sp.floyd_warshall_algo()

    ### AOV problem ###

    def all_path(self,v_a, v_b, visited, block):
        """
        Parameters:
            v_a(int): Start vertex No..

            v_a(str): Start vertex name.

            v_b(int): Destinated vertex No..

            v_b(str): Destinated vertex name.

            visited(list):
                Record visited vertices.
                Input empty list([]) first generally.

            block(list): Banned vertices list.

        Returns:
            all_path_list(list): All path from v_a to v_b.

        Attention:
            Could contain loop.

        Raises:
            ValueError, TypeError
        """
        try:
            int(v_a)
        except:
            v_a = name_to_num(v_a, self.V)

        try:
            int(v_b)
        except:
            v_b = name_to_num(v_b, self.V)

        # from path_problem
        p = PT(self.Adjacency_Matrix, self.Insidence_Matrix)

        return p.all_path(v_a, v_b, visited, block)

    ### min spainning tree ###
    
    def Kruskal_algo(self):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.kruskal_algo()

    def Prims_algo(self, root):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.prims_algo(root)

    def EC(self, start):
        # return all Eulerian circuit
        # could start from any vertex
        """
        Returns:
            EC_set(list):

        Vars:
            self.N(int):

        Raises:
            ValueError, TypeError
        """
        try:
            int(start)
        except:
            start = name_to_num(start, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.ec(start)


    def HC(self, start): 
        # return all Hamiltonian cycle
        # could start from any vertex
        """
        Returns:
            HC_set(list):

        Vars:
            self.N(int):

        Raises:
            ValueError, TypeError
        """
        try:
            int(start)
        except:
            start = name_to_num(start, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.hc(start)

    def ET(self, v_a): 
        """
        Returns:
            Return all Eulerian trail(chain)

        Raises:
            ValueError, TypeError
        """

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.et(v_a)

    def HP(self, v_a, v_b): 
        # return all Hamiltonian path
        """
        Returns:
            HP_set(list): 

        Vars:
            self.N(int):

        Raises:
            ValueError, TypeError
        """
        try:
            int(v_a)
        except:
            v_a = name_to_num(v_a, self.V)

        # from HE_problem
        he = HE(self.Adjacency_Matrix, self.Insidence_Matrix)
        return he.hp(v_a, v_b)


def put_all(a, b):
    for i in a:
        b.append(i)

    return b

def name_to_num(name, chart):
    # input: name_str
    # output: number_int of name in chart

    for i in range(len(chart)):
        if chart[i] == name:
            return i

    return False

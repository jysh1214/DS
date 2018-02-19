from get_imformation import GI
from graph_traversal import GT
from path_problem import PT
from min_spanning_tree import MST
import numpy as np

class Graph():
    def __init__(self, adj_matrix, ins_matrix, V, E, region, R):
        """
        Parameters:
            adj_matrix(list):
                The adjacency matrix of the graph.

            ins_matrix(list):
                The incidence matrix of the graph.
                Auto creat if the graph is undirect.

            V(list): 
                Vertex name list.
                V = [Vertex_0 name, Vertex_1 name, ...], default 0~n if input None

            E(list): 
                Edge name list.
                E = [Edge_0 name, Edge_1 name, ...], default 0~m if input None

            region(list):
                A matrix record region surrounded by which edges.
                region = Region_0|Region_1 ...
                   Edge_0    1   |    0
                   Edge_1    1   |    1  
                       ...
                EX:
                region[a][x] = region[b][x] = region[c][x] = 1: 
                region_x surrounded by edge_a, b, c

                It's planar graph difinition.
                input None if none

            R(list):
                Region name list.
                R = [Region_0 name, Region_1 name, ...], input None if none

        Vars:
            degree(list): Degree of vertex list.

            edges(int): How many edges. 

        Raises:
            ValueError, TypeError

        """

        """
        ex: simple undirect G = (V, E), A = adjacency matrix, B = incidence matrix

            g = Graph(A, B, None, None, None, None)
        """
        
        self.N = len(adj_matrix)

        # check data length
        for i in range(self.N):
            if len(adj_matrix[i]) != self.N:
                print('Input adjacency matrix error!')
                return False

            else: self.Adjacency_Matrix = adj_matrix

        self.Directed = False
        for i in range(self.N):
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] !=\
                   self.Adjacency_Matrix[j][i]:
                   self.Directed = True 

        # undireted graph
        if not self.Directed: 
            degree = []
            for i in range(self.N):
                temp = 0
                for j in range(self.N):
                    if self.Adjacency_Matrix[i][j] != 0:
                        temp += 1
                degree.append(temp)

            self.degree = degree

            total_degree = 0
            for i in range(self.N):
                total_degree += self.degree[i]

            # 2*|E| = degree sum
            self.edges = int(total_degree/2)
            
        # digraph
        else:
            pass

        if ins_matrix != None:
            for i in range(self.N):
                if len(ins_matrix[i]) != self.edges:
                    print('Input incidence matrix error!')
                    return False

                else: self.Insidence_Matrix = ins_matrix

        elif not self.Directed: # auto create incidence matrix if undirected
            ins_matrix = [[0 for i in range(self.edges)] for j in range(self.N)]
            e = 0
            while e < self.edges:
                for i in range(self.N):
                    for j in range(i, self.N):
                        if self.Adjacency_Matrix[i][j] != 0:
                            ins_matrix[i][e] = 1
                            ins_matrix[j][e] = 1
                            e += 1

            self.Insidence_Matrix = ins_matrix

        if V == None:
            V = [i for i in range(self.N)]
        else:
            if len(V) == self.N:
                self.V = V
            else:
                print('Input V error!')
                return False

        if E == None:
            E = [i for i in range(len(self.Insidence_Matrix[0]))]
        else:
            if len(E) == len(self.Insidence_Matrix[0]):
                self.E = E
            else:
                print('Input E error!')
                return False              

        self.Region = region

        if self.Region == None:
            self.R = None
        else:
            self.R = R

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

        if not self.Direct:
            return self.degree[vertex]

    def get_isol(self):
        """
        Returns:
            isol(list): Isolated vertices.

        Raises:
            ValueError, TypeError
        """

        isol = []
        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]==0) and (i!=j):
                    isol.append([i])

        return isol

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

    ### Decision problem ###

    def check_con(self):
        """
        Vars:
            self.Adjacency_Matrix

        Returns:
            bool.:If the graph connected, return True.
        """

        dfs = self.DFS(0, [])
        if len(dfs) == self.N:
            return True
        else:
            return False
            
    def check_compl(self):
        # if the graph is complete, return True

        for i in range(self.N):
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]==0) and (i!=j):
                    return False

        return True        

    def check_isol(self): 
        # if exit isolate vertex, return True

        for i in range(self.N):
            flag = True
            for j in range(self.N):
                if (self.Adjacency_Matrix[i][j]!=0) and (i!=j):
                    flag = False
            if flag: return True

        return False

    def check_path(self, v_a, v_b, block):
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
            start(int): Start vertex number.

            start(str): Start vertex name.

        Vars:
            color(list): The color of vertex.

            time(list): The recovered time and finish time of vertex.

            parents(list): The parents of vertex.

        Attention:
            Small vertex No. has high priority.

        Returns:
            dfs(list):

        Raises:
            ValueError, TypeError
        """
        try:
            int(start)
        except:
            start = name_to_num(start, self.V)

        gt = GT(self.Adjacency_Matrix)

        return gt.dfs(start)

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

    ### min spainning tree ###
    
    def Kruskal_algo(self):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.kruskal_algo()

    def Prims_algo(self):
        # from min_spanning_tree
        mst = MST(self.Adjacency_Matrix, self.Insidence_Matrix)
        return mst.prims_algo()
        
    ### AOV problem ###

    def all_path(self, start, v_a, v_b, visited):
        """
        Parameters:
            start(int): Input data as same as v_a first.

            start(str): Input data as same as v_a first.

            v_a(int): Start vertex No..

            v_a(str): Start vertex name.

            v_b(int): Destinated vertex No..

            v_b(str): Destinated vertex name.

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
        try:
            int(start)
        except:
            start = name_to_num(start, self.V)

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

        return p.all_path(start, v_a, v_b, [])  
        
# the others function

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

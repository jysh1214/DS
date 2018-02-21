from get_imformation import GI

import math
import numpy as np

class SP():
    def __init__(self, adj_matrix, ins_matrix):
        self.Adjacency_Matrix = adj_matrix
        self.N = len(self.Adjacency_Matrix)
        self.Insidence_Matrix = ins_matrix

    def dijkstra_algo(self, start):
        """
        Returns:
            dist(list): Start vertex to all the others vertices distance.

        Raises:
            ValueError, TypeError
        """
        sv = [] # selected vertices
        dist = [math.inf for i in range(self.N)]
        dist[start] = 0

        select = start
        while len(sv) < self.N - 1:
            sv.append(select)
            # from get_imformation
            gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
            nb = gi.get_nb(select)
            for i in range(len(nb)):
                e = gi.get_edge(select, nb[i])
                w = gi.get_weight(e)
                if w + dist[select] < dist[nb[i]]:
                    dist[nb[i]] = w + dist[select]

            # choose next selected vertex
            temp = []
            for j in range(len(dist)):
                temp.append((j, dist[j]))
            # sorted by distance
            temp = sorted(temp, key = lambda x: x[1])

            for k in range(len(temp)):
                if not(k in sv):
                    select = k
                    break

        # last one vertex
        total = [i for i in range(self.N)]
        last = list(set(total)-set(sv))[0]
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        nb = gi.get_nb(last)
        for i in range(len(nb)):
            e = gi.get_edge(last, nb[i])
            w = gi.get_weight(e)
            if w + dist[nb[i]] < dist[last]:
                dist[last] = w + dist[nb[i]]

        return dist

    def bellman_ford_algo(self, start):
        """
        Returns:
            dist(list): Start vertex to all the others vertices distance.

        Raises:
            ValueError, TypeError
        """
        dist = [[math.inf for i in range(self.N)]]
        dist[0][start] = 0

        # bool. matrix show fixed distance vertex
        bool_matrix = np.matrix(self.Adjacency_Matrix)
        # matrix[x, y] = list[x][y]
        for i in range(self.N):
            for j in range(self.N):
                if self.Adjacency_Matrix[i][j] != 0:
                    bool_matrix[i, j] = 1
                else:
                    bool_matrix[i, j] = 0

        step = 1
        while step < self.N - 1:
            dist.append([math.inf for i in range(self.N)])
            dist[step][start] = 0
            arrival_list = []
            # collect vertices can arrice
            for k in range(len(bool_matrix)):
                if bool_matrix[start, k]:
                    arrival_list.append(k)

            for l in range(len(arrival_list)):
                n = arrival_list[l]
                # collect u: vertex can go to n
                u = []
                for t in range(self.N):
                    if self.Adjacency_Matrix[t][n] != 0:
                        u.append(t)

                # find min(dist[step-1][u]+weight(u, n))
                min_ = math.inf
                for r in range(len(u)):
                    # from get_information
                    gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
                    e = gi.get_edge(u[r], n)
                    if dist[step-1][u[r]] + gi.get_weight(e) < min_:
                        min_ = dist[step-1][u[r]] + gi.get_weight(e)

                dist[step][n] = min(dist[step-1][n], min_)

            step += 1
            bool_matrix *= bool_matrix
            # while end

        return dist[step-1]

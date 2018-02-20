from get_imformation import GI

import math

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
        s = []
        dist = [math.inf for i in range(self.N)]
        dist[start] = 0

        select = start
        while len(s) < self.N - 1:
            s.append(select)
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
                if not(k in s):
                    select = k
                    break

        # last one vertex
        total = [i for i in range(self.N)]
        last = list(set(total)-set(s))[0]
        # from get_imformation
        gi = GI(self.Adjacency_Matrix, self.Insidence_Matrix)
        nb = gi.get_nb(last)
        for i in range(len(nb)):
            e = gi.get_edge(last, nb[i])
            w = gi.get_weight(e)
            if w + dist[nb[i]] < dist[last]:
                dist[last] = w + dist[nb[i]]

        return dist

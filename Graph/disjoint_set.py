class DS():
    def __init__(ins_matrix, mst, v_a, v_b):
        self.Insidence_Matrix = ins_matrix
        self.set = []

        def get_edge(v_a, v_b):   
            for i in range(len(self.Insidence_Matrix[0])):
                if (self.Insidence_Matrix[v_a][i]==1) and\
                   (self.Insidence_Matrix[v_b][i]==1):
                   return i

        def conn(a, b):
            # which set 'a' belong
            for i in range(len(self.set)):
            	if v_a in self.set[i]:
            		a_set = i

            for j in range(len(a_set)):
                e = get_edge(a_set[j], b)
                    if e in mst:
                        return True

            return False

        def part(v):
            flag = False
            for i in range(self.set):
            	if conn(self.set[i][0], v):
                    self.set[i].append(v)
                    flag = True
            if not flag: # new partion
                self.set.append([v])

        part(v_a)
        part(v_b)

    def same_set(self, v_a, v_b):
        """
        Parameters:

        Returns:
            bool.:If v_a and v_b belong same set, return True.
        """
        for i in range(len(self.set)):
            if v_a in self.set[i]:
                if v_b in self.set[i]:
                    return True

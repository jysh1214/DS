def nbs(vertex, adj):
    """
    Parameters:
        vertex(int): Vertex No..

    Returns:
        nbs_list(list): All neighbors of the vertex. 

    Raises:
        ValueError, TypeError
    """
    nbs_list = []
    for i in range(len(adj)):
        if adj[vertex][i] != 0:
            nbs_list.append(i)

    return nbs_list

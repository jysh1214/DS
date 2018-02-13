def k(n):
    """
    Parameters:
        n(int): The numbers of vertices.

    Returns:
        k_adj(list): N vertices complete graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    k_adj = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        k_adj[i][i] = 0

    return k_adj

def kk(n, m):
    """
    Parameters:
        n(int): The numbers of vertices of A part.

        m(int): The numbers of vertices of B part.

    Returns:
        kk_adj(list): Kn,m graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    kk_adj = [[0 for i in range(n+m)] for j in range(n+m)]
    i = 0
    while i < n + m:
        if i < m:
            for j in range(n, n+m):
                kk_adj[i][j] = 1
        else:
            for j in range(0, n):
                kk_adj[i][j] = 1
        i += 1

    return kk_adj

def path(n):
    """
    Parameters:
        n(int): The numbers of vertices.

    Returns:
        path_adj(list): N vertices path graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    path_adj = [[0 for i in range(n)] for j in range(n)]
    path_adj[0][1] = 1     # first vertex
    path_adj[n-1][n-2] = 1 # last vertex

    for i in range(1, n-1):
        path_adj[i][i-1] = 1
        path_adj[i][i+1] = 1

    return path_adj

def cycle(n): 
    """
    Parameters:
        n(int): The numbers of vertices.

    Returns:
        cycle_adj(list): N vertex cycle graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    cycle_adj = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        cycle_adj[i][(i-1)%n] = 1
        cycle_adj[i][(i+1)%n] = 1

    return cycle_adj

def wheel(n):
    """
    Parameters:
        n(int): The numbers of vertices.

    Returns:
        path_adj(list): N vertices wheel graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    wheel_adj = cycle(n)
    for i in range(n):
        wheel_adj[i].append(1)
    temp = [1 for i in range(n+1)] # center vertex
    temp[n] = 0
    wheel_adj.append(temp)

    return wheel_adj

def star(n):
    """
    Parameters:
        n(int): The numbers of vertices.

    Returns:
        start_adj(list): N vertices start graph adjacency matrix.

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """
    start_adj = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        start_adj[i][n-1] = 1
        start_adj[n-1][i] = 1 # center vertex

    return start_adj

def grid(n, m): 
    """
    Parameters:
        n(int): How many vertex.

    Returns:
        path_adj(list): n*m grid graph adjacency matrix.

        EX: 3*4 grid
            0-3-6-9
            | | | |
            1-4-7-10
            | | | |
            2-5-8-11

    Attention:
        It's undirected simple graph.

    Raises:
        ValueError, TypeError
    """

    grid_adj = [[0 for i in range(n*m)] for j in range(n*m)]
    for i in range(n*m):
        if i <= (n*m) - n - 1:
            # not the last colunm
            grid_adj[i][i+n] = 1
            grid_adj[i+n][i] = 1

        if not (i%n):
            # first row
            grid_adj[i][i+1] = 1
            grid_adj[i+1][i] = 1

        elif (i%n) == n-1: 
            # bottum row
            grid_adj[i][i-1] = 1
            grid_adj[i-1][i] = 1

        else:
            grid_adj[i][i-1] = 1
            grid_adj[i-1][i] = 1
            grid_adj[i][i+1] = 1
            grid_adj[i+1][i] = 1

    return grid_adj

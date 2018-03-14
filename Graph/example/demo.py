# from Graph import Graph
from graph_test import Graph

adj = [[0,8,21,11,0,0,0],[8,0,0,0,6,0,0],[21,0,0,0,12,0,0],[11,0,0,0,13,5,0],
       [0,6,12,13,0,15,0],[0,0,0,5,15,0,9],[0,0,0,0,0,9,0]]
ins = [[1,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0],[0,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,1,0,0],
       [0,0,0,1,1,1,0,1,0],[0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,0,1]]

V = ['阿杜家','愛德華','田季發爺','沖繩高中','佛心公司','Qtime','黑穴']
E = ['奴隸街','沖繩大道','田季街21巷','鐵支路','厚德路','月工大道','工口路','召喚峽谷','母湯路']

g = Graph(adj, ins, V, E, None, None)

print('阿杜想去Qtime打咖，他可以走哪些路線呢？')
a = g.all_path(0, 5, [], [])

for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        print(V[a[i][j]],'->',end='')
        if not (j==len(a[i])-1):
            b = g.get_edge(a[i][j], a[i][j+1])
            print(E[b],'->',end='')
print()
print()
print('阿杜想去Qtime打咖，但他害怕田季發爺的詛咒，他可以走哪些路線呢？')
a = g.all_path(0, 5, [],[2])
for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        print(V[a[i][j]],'->',end='')
        if not (j==len(a[i])-1):
            b = g.get_edge(a[i][j], a[i][j+1])
            print(E[b],'->',end='')
print()
print()
print('請求出阿杜家到所有地點的最短距離:')
print("使用Dijkstra's algorithm:")
dist = g.Dijkstra_algo(0)
for i in range(len(dist)):
    print('到{0}: {1}km'.format(V[i], dist[i]))
print()
print("使用Bellman-Ford algorithm:")
dist = g.Bellman_Ford_algo(0)
for i in range(len(dist)):
    print('到{0}: {1}km'.format(V[i], dist[i]))
print()
print('找出所有點到點最短距離，使用Floyd-Warshall algorithm:')
dist_matrix = g.Floyd_Warshall_algo()
for i in range(len(dist_matrix)):
    print('從{0}'.format(V[i]))
    for j in range(len(dist_matrix)):
        print('    到{0}: {1}km'.format(V[j], dist_matrix[i][j]))
print()
print('阿杜心血來潮，想找出島上地圖的min spanning tree')
print("使用Kruskal's algorithm:")
mst = g.Kruskal_algo()
for i in range(len(mst)):
    mst[i] = E[mst[i]]
print(mst)
print()
print("使用Prim's algorithm(阿杜家做root):")
root = [0]
mst = g.Prims_algo(root)
for i in range(len(mst)):
    mst[i] = E[mst[i]]
print(mst)
print()
adj = [[0,8,21,11,0,0],[8,0,0,0,6,0],[21,0,0,0,12,0],[11,0,0,0,13,5],
       [0,6,12,13,0,15],[0,0,0,5,15,0]]
ins = [[1,1,1,0,0,0,0,0],[1,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[0,1,0,0,0,1,1,0],
       [0,0,0,1,1,1,0,1],[0,0,0,0,0,0,1,1]]

V = ['阿杜家','愛德華','田季發爺','沖繩高中','佛心公司','Qtime']
E = ['奴隸街','沖繩大道','田季街21巷','鐵支路','厚德路','月工大道','工口路','召喚峽谷']
g = Graph(adj, ins, V, E, None, None)

print('假如母湯路母湯過去')
print('請問阿杜家開始的Eulerian Tail為:')
et = g.ET(0)

for i in range(len(et)):
    print()
    for j in range(len(et[i])):
        if (j%2):
            print(E[et[i][j]],'->',end='')
        else:
            print(V[et[i][j]],'->',end='')
    print()

print()
print()

adj = [[0,8,21,11,0,0,0],[8,0,0,0,6,0,0],[21,0,0,7,12,0,0],[11,0,7,0,13,5,0],
       [0,6,12,13,0,15,0],[0,0,0,5,15,0,9],[0,0,0,0,0,9,0]]
ins = [[1,1,1,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,0,1],
       [0,1,0,0,0,1,1,0,0,1],[0,0,0,1,1,1,0,1,0,0],[0,0,0,0,0,0,1,1,1,0],
       [0,0,0,0,0,0,0,0,1,0]]

V = ['阿杜家','愛德華','田季發爺','沖繩高中','佛心公司','Qtime','黑穴']
E = ['奴隸街','沖繩大道','田季街21巷','鐵支路','厚德路','月工大道','工口路','召喚峽谷',
     '母湯路','田季街87巷']
g = Graph(adj, ins, V, E, None, None)
print('田季發爺和沖繩高中中間開了一條新路，叫田季街87巷(7km)')
print('請問阿杜家到黑穴的Hamiltonian Path為:')
ht = g.HP(0, 6)
for i in range(len(ht)):
    print()
    for j in range(len(ht[i])):
        print(V[ht[i][j]],'->',end='')
        if (j<len(ht[i])-1):
            b = g.get_edge(ht[i][j], ht[i][j+1])
            print(E[b],'->',end='')
    print()
print()
print()

adj = [[0,8,21,11,0,0,0],[8,0,0,0,6,0,0],[21,0,0,7,12,0,0],[11,0,7,0,13,5,16],
       [0,6,12,13,0,15,0],[0,0,0,5,15,0,9],[0,0,0,16,0,9,0]]
ins = [[1,1,1,0,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,0,1,0],
       [0,1,0,0,0,1,1,0,0,1,1],[0,0,0,1,1,1,0,1,0,0,0],[0,0,0,0,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,1,0,1]]

V = ['阿杜家','愛德華','田季發爺','沖繩高中','佛心公司','Qtime','黑穴']
E = ['奴隸街','沖繩大道','田季街21巷','鐵支路','厚德路','月工大道','工口路','召喚峽谷',
     '母湯路','田季街87巷','啊斯路']

g = Graph(adj, ins, V, E, None, None)
print('沖繩高中到黑穴開了一條新路，叫啊斯路(16km)')
print('請問阿杜家開始的Hamiltonian Cycle為:')
hc = g.HC(0)
for i in range(len(hc)):
    print()
    for j in range(len(hc[i])):
        print(V[hc[i][j]],'->',end='')
        if not (j==len(hc[i])-1):
            b = g.get_edge(hc[i][j], hc[i][j+1])
            print(E[b],'->',end='')
    print()
print()
print('阿杜想找出沖繩島的clique:')
cliq_set = g.clique()
for i in range(len(cliq_set)):
    cliq_set[i] = V[cliq_set[i]]
print(cliq_set)
print()
print('阿杜想找出沖繩島的independent set:')
indp = g.indp_set()
for i in range(len(indp)):
    indp[i] = V[indp[i]]
print(indp)
print()
print('阿杜想找出沖繩島的dominating set:')
ds = g.dominating_set()
for i in range(len(ds)):
    ds[i] = V[ds[i]]
print(ds)
print()

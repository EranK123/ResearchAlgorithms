import networkx as nx
import numpy as np
import networkx.algorithms.approximation.clique as cq

"""
Finds the $O(|V|/(log|V|)^2)$ apx of maximum clique/independent set
    in the worst case.
     A clique in an undirected graph G = (V, E) is a subset of the vertex set
    `C \subseteq V` such that for every two vertices in C there exists an edge
    connecting the two. This is equivalent to saying that the subgraph
    induced by C is complete (in some cases, the term clique may also refer
    to the subgraph).
"""

graph = nx.gnp_random_graph(np.random.randint(2, 20), np.random.random(), seed=None, directed=False)
print(graph)
print(list(cq.max_clique(graph)))
print("------------------------")
for i in nx.find_cliques(graph):
    print(i)

for i in range(20):
    p = np.random.random()
    n = np.random.randint(2, 20)
    graph = nx.gnp_random_graph(n, p, seed=None, directed=False)

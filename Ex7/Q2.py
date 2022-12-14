import math

import networkx as nx
import numpy as np
import networkx.algorithms.approximation.clique as cq
import matplotlib.pyplot as plt

"""
Finds the $O(|V|/(log|V|)^2)$ apx of maximum clique/independent set
    in the worst case.
     A clique in an undirected graph G = (V, E) is a subset of the vertex set
    `C \subseteq V` such that for every two vertices in C there exists an edge
    connecting the two. This is equivalent to saying that the subgraph
    induced by C is complete (in some cases, the term clique may also refer
    to the subgraph).
"""


def plot_approx():
    idx = 1
    values = {}
    max_clique = -1
    ns = set()
    for i in range(20):  # generate 20 random sized vertices
        ns.add(np.random.randint(2, 20))
    for p in range(10):  # run for 10 different probabilities
        prb = np.random.random()
        values[prb] = []
        for n in ns:  # for each size
            graph = nx.gnp_random_graph(n, prb, seed=None, directed=False)  # build a random gnp graph
            maximum_clique = list(cq.max_clique(graph))  # get the maxmimum clique the approx algo returns
            for clique in nx.find_cliques(graph):
                max_clique = max(max_clique, len(clique))  # get the exact maxmimal clique in the graph
            values[prb].append(len(maximum_clique) / max_clique)  # for each probability append the approximation ratio
    for prob in values.keys():  # plot the graph where the xis are the number of vertices, yis is the approximation ratio for each probability
        xis = list(k for k in ns)
        yis = values[prob]
        plt.xlabel("Size")
        plt.ylabel("Approximation")
        plt.title(f"p :{round(prob, 5)}", fontsize=10)
        plt.subplot(3, 5, idx)
        idx += 1
        plt.plot(xis, yis, 'r')
        th_approx = list(k / math.log2(k) ** 2 for k in ns)  # calc the theoretic approx
        print(f"Differences Approximation{np.array(values[prob]) - np.array(th_approx)}")
    plt.show()


"""
The approximation algo is better when the number of vertices gets bigger
"""
plot_approx()

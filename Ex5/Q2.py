import math
import sys
from typing import Callable

graph1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
graph2 = {0: [(0, 0), (1, 5), (2, math.inf), (3, math.inf)],
          1: [(0, 50), (1, 0), (2, 15), (3, 5)],
          2: [(0, 30), (1, math.inf), (2, 0), (3, 15)],
          3: [(0, 15), (1, math.inf), (2, 5), (3, 0)]
          }


def same_look(graph: dict):
    """
    this function gets a graph and if the graph is a dictionary it turns it to a matrix. in this way the algo can accepts two ways of input
    """
    if type(graph) is list:
        return graph
    rows = cols = len(graph.keys())
    i = j = 0
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    while i != rows:
        for adj in graph.values():
            for val in adj:
                mat[i][j] = val[1]
                j += 1
            i += 1
            j = 0
    return mat


class Output:
    def sum(self):
        """
         sums the length of shortest paths
        """
        sum = 0
        for i in self:
            sum += i
        return sum

    def dist_from_source(self):
        """
        find the distance of the shortest paths from source vertex to all other vertices
        """
        res = dict()
        for node in range(len(self)):
            res[node] = self[node]
        return res


def path_algo(algorithm: Callable, items: list, src, outputtype=Output):
    """
    >>> path_algo(algorithm=dijkstra, items=graph1, src=1, outputtype=Output.dist_from_source)
    {0: 4, 1: 0, 2: 8, 3: 15, 4: 22, 5: 12, 6: 12, 7: 11, 8: 10}
    >>> path_algo(algorithm=dijkstra, items=graph1, src=1, outputtype=Output.sum)
    94
    >>> path_algo(algorithm=floyd_warshall, items=graph1, src=1, outputtype=Output.dist_from_source)
    {0: 4, 1: 0, 2: 8, 3: 15, 4: 22, 5: 12, 6: 12, 7: 11, 8: 10}
    >>> path_algo(algorithm=floyd_warshall, items=graph1, src=1, outputtype=Output.sum)
    94
    >>> path_algo(algorithm=dijkstra, items=graph2, src=2, outputtype=Output.dist_from_source)
    {0: 30, 1: 35, 2: 0, 3: 15}
    >>> path_algo(algorithm=dijkstra, items=graph2, src=2, outputtype=Output.sum)
    80
    >>> path_algo(algorithm=floyd_warshall, items=graph2, src=2, outputtype=Output.dist_from_source)
    {0: 30, 1: 35, 2: 0, 3: 15}
    >>> path_algo(algorithm=floyd_warshall, items=graph2, src=2, outputtype=Output.sum)
    80
    """
    path = algorithm(same_look(items), src)
    return outputtype(path)


def minDistance(dist, sptSet, v_num):
    # Initialize minimum distance for next node
    min_index = 0
    min = 1e7

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(v_num):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def dijkstra(graph, src):
    v_num = len(graph[0])
    dist = [sys.maxsize] * v_num
    dist[src] = 0
    sptSet = [False] * v_num

    for cout in range(v_num):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # x is always equal to src in first iteration
        x = minDistance(dist, sptSet, v_num)

        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[x] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for y in range(v_num):
            if graph[x][y] > 0 and sptSet[y] == False and \
                    dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
    return dist


def floyd_warshall(graph, src):
    graph = change_to_inf(graph)
    v_num = len(graph[0])
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Adding vertices individually
    for k in range(v_num):
        for i in range(v_num):
            for j in range(v_num):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance[src]


def change_to_inf(graph):
    """
     if there is no path between two vertices, there will need to be inf in the place of the matrix for floyd_warshall to watk
    """
    v_num = len(graph[0])
    for i in range(v_num):
        for j in range(v_num):
            if graph[i][j] == 0 and i != j:
                graph[i][j] = math.inf
    return graph


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
    print(path_algo(algorithm=dijkstra, items=graph1, src=0, outputtype=Output.dist_from_source))
    print(path_algo(algorithm=dijkstra, items=graph1, src=0, outputtype=Output.sum))
    print(path_algo(algorithm=floyd_warshall, items=graph1, src=0, outputtype=Output.dist_from_source))
    print(path_algo(algorithm=floyd_warshall, items=graph1, src=0, outputtype=Output.sum))
    print(path_algo(algorithm=dijkstra, items=graph2, src=0, outputtype=Output.dist_from_source))
    print(path_algo(algorithm=dijkstra, items=graph2, src=0, outputtype=Output.sum))
    print(path_algo(algorithm=floyd_warshall, items=graph2, src=0, outputtype=Output.dist_from_source))
    print(path_algo(algorithm=floyd_warshall, items=graph2, src=0, outputtype=Output.sum))

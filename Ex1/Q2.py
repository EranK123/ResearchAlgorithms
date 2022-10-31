def breadth_first_search(start, end, neighbor_function):
    """
            >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function)
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
            >>> breadth_first_search(start=0, end=10, neighbor_function=two_neighbor_function)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            >>> breadth_first_search(start='5', end='8', neighbor_function=graph_neighbor)
            ['5', '3', '4', '8']
        """
    visited = {}
    queue = [start]
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        if m == end:
            return print_path(visited, start, end)  # return the path of all nodes
        neighbours = neighbor_function(m)  # get all the neighbors
        for neighbour in neighbours:
            if m not in queue:  # check which is not visited and update
                visited[neighbour] = m
                queue.append(neighbour)


# this function prints the path of the bfs search
def print_path(parent, s, e):
    path = [e]
    while path[-1] != s:
        path.append(parent[path[-1]])
    path.reverse()
    return path


# this function gets the neighbors of a 2d point
def four_neighbor_function(node) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


# this function gets the neighbors of a number point
def two_neighbor_function(node) -> list:
    x = node
    return [(x + 1), (x - 1)]


# neighbor function for a graph
def graph_neighbor(node) -> list:
    neighbors = []
    for x in graph[node]:
        neighbors.append(x)
    return neighbors


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
print(breadth_first_search(start=0, end=10, neighbor_function=two_neighbor_function))
print(breadth_first_search(start='5', end='8', neighbor_function=graph_neighbor))

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())

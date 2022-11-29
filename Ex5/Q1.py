import itertools


# ===================== Q1.a ================== #
def bounded_subsets(bound_set, val, mem=[]):
    """
     >>> for j in bounded_subsets([1, 2, 4], 1): print (j, end="")
     [][1]
     >>> for j in bounded_subsets([7,8,9,10], 20): print (j, end="")
     [7][8][9][10][7, 8][7, 9][7, 10][8, 9][8, 10][9, 10]
     >>> for j in bounded_subsets(range(5,15), 15): print (j, end="")
     [5][6][11][12][13][14][5, 6][5, 7][5, 8][5, 9][5, 10][6, 7][6, 8][6, 9]
    """
    for i in range(len(bound_set) + 1):
        for comb in itertools.combinations(bound_set, i):  # iterate over all the combinations
            if sum(comb) <= val:  # check if sum of the combination is lower than val
                if comb not in mem:  # check in mem so we dont check the same comb twice
                    mem.append(comb)
                    yield list(comb)  # will remember the last comb


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())

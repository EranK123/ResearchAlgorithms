def print_sorted(data):
    """
            >>> print_sorted({'c': 2, 'b': 1})
            {'b': 1, 'c': 2}
            >>> print_sorted({"a": 5, "c": 6, "b": 1})
            {'a': 5, 'b': 1, 'c': 6}

        """
    data_list = [(k, v) for k, v in data.items()]
    lst = len(data_list)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if data_list[i][1] > data_list[i + 1][1]:
                temp = data_list[i]
                data_list[i] = data_list[i + 1]
                data_list[i + 1] = temp
    return dict(data_list)


x = {"a": 5, "c": 6, "b": 1}
print(print_sorted(x))
print(print_sorted({'c': 2, 'b': 1}))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

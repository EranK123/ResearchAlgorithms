def lastcall(func, mem={}):
    """
    >>> f(5)
    '25'
    >>> f(5)
    'I already told you the answer is 25'
    >>> f1(3,2)
    '5'
    >>> f1(4,4)
    '8'
    >>> f1(x=3,y=2)
    'I already told you the answer is 5'
    >>> f1("ab", "c")
    'abc'
    >>> f1("def", "")
    'def'
    >>> f1("ab", "c")
    'I already told you the answer is abc'
    """
    if func not in mem.keys():  # if its a new function add it to the dict
        mem[func] = list()

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)  # get the value the function returns
        kwarg_values = []
        for value in kwargs.values():  # deals with kwargs
            kwarg_values.append(value)
        if tuple(kwarg_values) not in mem[func] and len(kwarg_values) != 0:  # check if kwargs values are in the dict # of the func
            mem[func].append(tuple(kwarg_values))
            return str(val)
        if args not in mem[func] and len(args) != 0:  # if its a new value we add it to mem and return
            mem[func].append(args)  # add it to the list of the function
            return str(val)
        return "I already told you the answer is " + str(val)

    return wrapper


@lastcall
def f(x):
    return x ** 2


@lastcall
def f1(x, y):
    return x + y


@lastcall
def f3(x):
    return x + x


print(f(x=4))
print(f(4))
print(f(10))
print(f(4))
print(f1(10, 15))
print(f1(x=10, y=15))
print(f3(9))
print(f3(3))
print(f3(9))

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())

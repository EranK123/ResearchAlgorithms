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
    >>> f1(3,2)
    'I already told you the answer is 5'
    """
    if func not in mem.keys():  # if its a new function add it to the dict
        mem[func] = list()

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)  # get the value the function returns
        if args not in mem[func]:
            mem[func].append(args)  # add it to the dict of the function
            return str(val)  # if its a new value return
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


print(f(4))
print(f(4))
print(f(10))
print(f(4))
print(f1(10, 15))
print(f1(10, 15))
print(f3(9))
print(f3(3))
print(f3(9))


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
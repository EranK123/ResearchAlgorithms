def safe_call(func, **kwargs):
    """
        >>> safe_call(f1,x=5,y=7.0,z=3)
        15.0
        >>> safe_call(f1,x=True,y=4.1,z=32)
        Traceback (most recent call last):
            ...
        Exception: Wrong Type
        >>> safe_call(f1,x=3,y=5,z=32)
        Traceback (most recent call last):
            ...
        Exception: Wrong Type
        >>> safe_call(f3,x=5,y=7.1)
        12.1
        >>> safe_call(f2, x="a", y="dwa", z="abc")
        'adwaabc'
        >>> safe_call(f2, x=2, y="dwa", z=2)
        Traceback (most recent call last):
            ...
        Exception: Wrong Type
    """
    check_ano(func, **kwargs)  # call to a function which will check if all the types are as they are
    return func(**kwargs)  # if everything is as it is we will return


def check_ano(func, **kwargs):
    annotations = func.__annotations__  # get the annotations of the attributes
    for x in annotations.keys():
        if (type(kwargs[x])) is not annotations[x]:  # check if they match
            raise Exception("Wrong Type")


def f1(x: int, y: float, z):
    return x + y + z


def f2(x, y: str, z: str):
    return x + y + z


def f3(x: int, y: float):
    return x + y


# running examples
print(safe_call(f1, x=5, y=2.0, z=3))
print(safe_call(f2, x="da", y="abc", z="3"))
print(safe_call(f3, x=3, y=2.1))

# if __name__ == "__main__":
#     import doctest
#
#     print(doctest.testmod())

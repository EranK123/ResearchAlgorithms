class List(list):
    def __init__(self, iter):
        super().__init__(item for item in iter)  # inherit all the list function using super and initiate the elements

    def __getitem__(self, items):  # [] operator
        """
        >>> mylist1[0]
        [[1, 2, 3, 33], [4, 5, 6, 66]]
        >>> mylist2[0,4]
        [32, 1231, [315, 11, 3]]
        >>> mylist3[2,1,2,0]
        18
        >>> mylist1[0,1,5]
        Traceback (most recent call last):
            ...
        Exception: Out Of Range
        """
        elem = self
        if type(items) == int:  # if its only one number we return just like a normal list
            return list.__getitem__(self, items)  # use the list getitem operator for ours
        for i in items:  # else go through each element until we reach the last
            try:
                elem = elem[i]
            except:
                raise Exception("Out Of Range")
        return elem


mylist1 = List([[[1, 2, 3, 33], [4, 5, 6, 66]],
                [[7, 8, 9, 99], [10, 11, 12, 122]],
                [[13, 14, 15, 155], [16, 17, 18, 188]]])

mylist2 = List([[3212, 31, 5, 2,[32, 1231,[315, 11,3]]], [0, 3, 1]])

mylist3 = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, [18, 90]]],
])
print(mylist1[0, 1, 3])
print(mylist2[0,4,2])
print(mylist3[2, 1, 2, 1])

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
import itertools


#
# class BoundedSubsets:
#     def __init__(self, bounded_set, val):
#         self.set = bounded_set
#         self.state = []
#         self.val = val
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # if sum(self.state) > self.val:
#         #     raise StopIteration
#
#         for i in range(len(self.set) + 1):
#             for comb in itertools.combinations(set(self.set), i):
#                 if sum(comb) <= self.val:
#                     res = self.state
#                     self.state = list(comb)
#                     return res
#                 else:
#                     raise StopIteration
#
# ===================== Q1.a ================== #
def bounded_subsets(bound_set, val, mem=[]):
    for i in range(len(bound_set) + 1):
        for comb in itertools.combinations(bound_set, i):
            if sum(comb) <= val:
                if comb not in mem:
                    mem.append(comb)
                    yield list(comb)


# for s in bounded_subsets([1, 2, 3], 4):
#     print(s)

# for s in bounded_subsets(range(50, 150), 103):
#     print(s)

# for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
#     print(s)


# ===================== Q1.b ================== #

# def ordered_bounded_subsets(bound_set, val, mem=[]):
#     var = None
#     for i in range(len(bound_set) + 1):
#         for j in range(0, len(bound_set) - i - 1):
#          var = [(comb1, comb2) for comb1 in itertools.combinations(bound_set, i) for comb2 in
#                 itertools.combinations(bound_set, j)]
#         print(var)

# for s in ordered_bounded_subsets([1, 2, 3], 4):
#     print(s)



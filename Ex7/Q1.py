import numpy as np
import time
import math
import random
import matplotlib.pyplot as plt


# import cvxpy as cp

def generate_linear_equations():
    k = np.random.randint(2, 15)
    coeffs = [*range(-10, 0), *range(1, 11)]
    rng = np.random.default_rng()
    return rng.choice(coeffs, size=(k, k)), rng.integers(-10, 11, k), k


def numpyu_sol():
    coeffs, variables, k = generate_linear_equations()
    solution = coeffs.dot(variables)

    symbols = 'abcdefgh'[:k]
    for row, sol in zip(coeffs, solution):
        lhs = ' '.join(f'{r:+}{s}' for r, s in zip(row, symbols)).lstrip('+')
        print(f'{lhs} = {sol}')
    print()
    for s, v in zip(symbols, variables):
        print(f'{s} = {v}')

def cvxpy_sol():
    pass


def time_calculation():
    t = {}
    for i in range(20):
        coeffs, variables, k = generate_linear_equations()
        t1 = time.time()
        solution = coeffs.dot(variables)
        t2 = time.time() - t1
        t[k*k] = t2
    return t


def plot(t : dict):
    xis = list(i for i in t.keys())
    yis = list(i for i in t.values())
    print(xis, yis)
    plt.plot(xis, yis,'r')
    plt.xlabel("Size")
    plt.ylabel("Time")
    plt.title("numpy Vs cvxpy")
    plt.show()

plot(time_calculation())


# numpyu_sol()

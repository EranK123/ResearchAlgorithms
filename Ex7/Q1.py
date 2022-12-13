import numpy as np
import time
import math
import random
import matplotlib.pyplot as plt
import cvxpy as cp


def generate_linear_equations():
    k = np.random.randint(2, 25)  # amount of variables
    mkd, rhs = [], []  # eqs for the mekadmim, rhs for what each equaions equals to
    for i in range(k):  # iterate k time for the amount of equations
        temp_eq = []
        for j in range(k):  # iterate another k times for each variable
            temp_eq.append(np.random.randint(-10, 10))
        mkd.append(temp_eq)
        rhs.append(np.random.randint(-100, 100))
    return mkd, rhs, k


def numpyu_sol(system_of_equations):
    mkd, rhs, k = system_of_equations
    solution = np.linalg.solve(mkd, rhs)  # gets mekadmim and the equals to each equations and solves it
    return solution


def cvxpy_sol(system_of_equations):
    mkd, rhs, k = system_of_equations
    x = cp.Variable(k)  # amount of variables
    constr = [np.array(mkd) @ x - np.array(rhs) == 0]  # equals to zero so we have system of linear equations
    obj = cp.Minimize(cp.sum(x))
    prb = cp.Problem(obj, constr)  # define the problem of the equations
    prb.solve()  # solve it
    return x.value


def times():
    d_numpy = {}
    d_cvxpy = {}
    for i in range(20):
        system = generate_linear_equations()
        t1 = time.time()
        numpyu_sol(system)
        t2 = time.time() - t1
        d_numpy[system[2] * system[2]] = t2
        t3 = time.time()
        cvxpy_sol(system)
        t4 = time.time() - t3
        d_cvxpy[system[2] * system[2]] = t4
    return d_numpy, d_cvxpy


def plot(d_numpy: dict, d_cvxpy: dict):
    """
    This function gets both of the dictionary of time and size of the system for each library and plots it
    """
    xis_numpy = list(i for i in d_numpy.keys())
    yis_numpy = list(i for i in d_numpy.values())
    xis_cvx = list(i for i in d_cvxpy.keys())
    yis_cvx = list(i for i in d_cvxpy.values())
    plt.plot(xis_numpy, yis_numpy, 'r', label="numpy")
    plt.plot(xis_cvx, yis_cvx, 'b', label="cvxpy")
    plt.legend()
    plt.xlabel("Size")
    plt.ylabel("Time")
    plt.title("numpy Vs cvxpy")
    plt.show()


d1, d2 = times()
plot(d1, d2)

"""
We can see numpy is much faster.
"""

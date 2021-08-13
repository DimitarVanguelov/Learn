
# Numpy Vecotrized, via Houstonwp
import timeit
setup='''
import numpy as np
q = np.array([0.001,0.002,0.003,0.003,0.004,0.004,0.005,0.007,0.009,0.011])
w = np.array([0.05,0.07,0.08,0.10,0.14,0.20,0.20,0.20,0.10,0.04])
P = 100
S = 25000
r = 0.02


def npv(q, w, P, S, r):
    decrements = np.cumprod(1-q-w)
    inforce = np.empty_like(decrements)
    inforce[:1] = 1
    inforce[1:] = decrements[:-1]
    ncf = inforce * P - inforce * q * S
    t = np.arange(1, np.size(q)+1)
    d = np.power(1/(1+r), t)
    return np.sum(ncf * d)
'''
benchmark = '''npv(q, w, P, S, r)'''

print(timeit.timeit(stmt=benchmark,setup=setup,number = 1000000))

# Python Accumulator, via Houstonwp
setuploop='''
q = [0.001,0.002,0.003,0.003,0.004,0.004,0.005,0.007,0.009,0.011]
w = [0.05,0.07,0.08,0.10,0.14,0.20,0.20,0.20,0.10,0.04]
P = 100
S = 25000
r = 0.02


def npv_loop(q, w, P, S, r):
    inforce = 1.0
    result = 0.0
    v = 1 / (1 + r)
    v_t = v
    for t in range(0,len(q)-1):
        result = result + inforce * (P-S*q[t]) * v_t
        inforce = inforce * (1 - (q[t] + w[t]))
        v_t = v_t * v
    return result

'''
benchmarkloop = '''npv_loop(q, w, P, S, r)'''

# Numba Accumulator, via EarthGoddessDude
setuploop='''
from numba import njit

q = [0.001,0.002,0.003,0.003,0.004,0.004,0.005,0.007,0.009,0.011]
w = [0.05,0.07,0.08,0.10,0.14,0.20,0.20,0.20,0.10,0.04]
P = 100
S = 25000
r = 0.02


@njit
def npv_numba(q, w, P, S, r):
    inforce = 1.0
    result = 0.0
    v = 1 / (1 + r)
    v_t = v
    for t in range(0,len(q)-1):
        result = result + inforce * (P-S*q[t]) * v_t
        inforce = inforce * (1 - (q[t] + w[t]))
        v_t = v_t * v
    return result

'''
benchmarknumba = '''npv_numba(q, w, P, S, r)'''


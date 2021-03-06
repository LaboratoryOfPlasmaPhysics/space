import numpy as np
import pandas as pd

def norm(u, v, w):
    return np.sqrt(u**2 + v**2 + w**2)

def resolve_poly1(a, b, epsilon=1e-7):

    if isinstance(a, np.ndarray) | isinstance(a, pd.Series):
        b = np.ones(len(a)) * b
        r = np.zeros(len(a))
        r[(abs(a) >= epsilon)] = -b[ (abs(a) >= epsilon)] / a[ (abs(a) >= epsilon)]

    else :
        if abs(a) >= epsilon :
            r=-b/a
        else :
            r=0
    return r

def resolve_poly2_real_roots(a, b, c, epsilon=1e-7):
    delta = b ** 2 - 4 * a * c
    if isinstance(delta, np.ndarray) | isinstance(delta, pd.Series):
        delta[delta < 0] = np.nan
        a = np.ones(len(delta)) * a
        b = np.ones(len(delta)) * b
        c = np.ones(len(delta)) * c
        r1 = np.zeros(len(delta))
        r2 = np.zeros(len(delta))
        r1[abs(a) >= epsilon] = (-b[abs(a) >= epsilon] + np.sqrt(delta[abs(a) >= epsilon])) / (2 * a[abs(a) >= epsilon])
        r2[abs(a) >= epsilon] = (-b[abs(a) >= epsilon] - np.sqrt(delta[abs(a) >= epsilon])) / (2 * a[abs(a) >= epsilon])
        r1[abs(a) <= epsilon ] = r2[(abs(a) <= epsilon)] = resolve_poly1(b[abs(a) <= epsilon ], c[abs(a) <= epsilon ] , epsilon=epsilon)

    else:
        if delta < 0:
            r1 = r2 = np.nan
        elif (abs(a) <= epsilon):
            r1 = r2 = resolve_poly1(b, c, epsilon=epsilon)
        else :
            r1 = (-b + np.sqrt(delta)) / (2 * a)
            r2 = (-b - np.sqrt(delta)) / (2 * a)


    return r1, r2

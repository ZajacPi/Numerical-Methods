import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction


from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2*x) + x**2 - 1
    #  return x**2-4

def dfun(x):
    return -2*np.exp(-2*x) + 2*x
    # return 2*x
def ddfun(x):
    return 4*np.exp(-2*x)+2
    # return 2

# def is_continuous(func, interval_start, interval_end, num_points=1000, epsilon=1e-6):
#     x_values = np.linspace(interval_start, interval_end, num_points)
#     y_values = func(x_values)

#     differences = np.abs(np.diff(y_values))

#     max_difference = np.max(differences)

#     return max_difference < epsilon
# print(is_continuous(fun, -10, 10))


def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    # PIERWSZE PODEJŚCIE
    # try:
    #     if f(a)*f(b) > 0:
    #         return None
    #     # if not is_continuous(f, a, b):
    #     #     return None
    #     num_iter = 0
    #     max_iter = iteration
    #     while (b - a) / 2 > epsilon and num_iter < max_iter:
    #         midpoint = (a + b) / 2
    #         # if f(midpoint) == 0:
    #         #     return (midpoint, num_iter)
    #         if np.abs(f(midpoint))< epsilon:
    #              return (midpoint, num_iter)

    #         elif f(midpoint) * f(a) < 0:
    #             b = midpoint
    #         else:
    #             a = midpoint
    #         num_iter += 1
    #         if  num_iter >= iteration:
    #             break
    #     return midpoint, num_iter 
    
    # except(ValueError, TypeError):
    #     return None
# print(bisection(0, 5, fun, epsilon=1e-5, iteration = 100))

    if a < b:
        t = a
        a = b
        b = t

    try:
        #rozpoczynam licznik iteracji
        i = 0
        midpoint = (a + b)/2
        res = f(midpoint)
        
        while abs(res) > epsilon:
            if res * f(a) > 0:
                a = midpoint

            else:
                b = midpoint
            midpoint = (a + b)/2
            res = f(midpoint)
            i+=1

            if i >= iteration:
                break

        return midpoint, i 
    

    except:
        return None
def difference_quotient(f: typing.Callable[[float], float],x: Union[int,float], h: Union[int,float]):
    '''Funkcja obliczająca iloaz różnicowy zadanej funkcji
    Parametry:
    
    f - funkcja dla której jest poszukiwane rozwiązanie
    x - argument funkcji la której jest 
    h - krok różnicy wykorzystywanej do wyliczenia ilorazu różnicowego
    
    return:
    diff - wartość ilorazu różnicowego
    
    '''
    try:
        diff = (f(x+h)-f(x))/h
        return diff
    except(ValueError, TypeError):
        return None

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    try:
        x = 1
        # funkcja na końcach przedziału przyjmuje przeciwne znaki
        if f(a)*f(b)>0:
            return None
      
        iter_count = 0
        while np.abs(f(x)) > epsilon and iter_count < iteration:
            x = x - (f(x) / difference_quotient(f, x, 0.00001))
            iter_count += 1
        #sprawdzam czy x jest wgl w przedziale
        if x<a or x>b:
            return None
        return x, iter_count
    
    except(ValueError, TypeError):
        return None

# kopiuję z poprzednich laboratoriów do wykonania zadania 5
def relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    if not isinstance(v,(int, float, List, np.ndarray)) or not isinstance(v_aprox,(int, float, List, np.ndarray)):
        return np.nan
    
    try:
        if np.array(v).all() == 0:
            raise ValueError
        return abs((np.array(v_aprox)-np.array(v))/np.array(v))
    except:
        return np.nan
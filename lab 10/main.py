##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple

def linear_least_squares(x:np.ndarray,y:np.ndarray)-> np.ndarray:
    """Funkcja do obliczania współczynników liniowej aproksymacji metodą najmniejszych kwadratów,
    
    Parameters:
    x(np.ndarray): wartość x punktu danych
    y(np.ndarray): wartość y punktu danych

    Results:
    np.ndarray: wektor współczynników aproksymacji. 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
  
    if len(x) != len(y) or len(x) < 2:
        return None

    n = len(x)

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x**2)

    denominator = n * sum_x_squared - (sum_x)**2

    if denominator == 0:
        return None

    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / n

    return np.array([a, b])




def chebyshev_nodes(n:int,interval:tuple)-> np.ndarray:
    """Funkcja tworząca wektor zawierający węzły czybyszewa w postaci wektora (n) dla zadanego przedziału i organizująca wynik posortowany od najmniejszego do największego węzła
    
    Parameters:
    n(int): ilość węzłów Czebyszewa. Wartość musi być większa od 0.
    interval (tuple): Przedział, na którym mają być wygenerowane węzły (początek, koniec).
     
    Results:
    np.ndarray: posortowany wektor węzłów Czybyszewa o rozmiarze (n). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
 
    if not(isinstance(n, int)) or not(isinstance(interval, tuple)) or n <= 0 or len(interval) != 2 or interval[0] >= interval[1]:
        return None
    
    cheb_nodes = 0.5 * (interval[0] + interval[1]) + 0.5 * (interval[1] - interval[0]) * np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))

    cheb_nodes = np.sort(cheb_nodes)

    return cheb_nodes

##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple

def chebyshev_nodes(n:int=10):
    """Funkcja tworząca wektor zawierający węzły czybyszewa w postaci wektora (n+1,)
    
    Parameters:
    n(int): numer ostaniego węzła Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(n,int) and n >0:
        return np.array([np.cos(i*np.pi/n) for i in range(0,n+1)])
    else:
        return None 
    
def L_inf(xr:Union[int, float, List, np.ndarray],x:Union[int, float, List, np.ndarray]):
    """Obliczenie normy  L nieskończonośćg. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach biblioteki numpy.
    
    Parameters:
    xr (Union[int, float, List, np.ndarray]): wartość dokładna w postaci wektora (n,)
    x (Union[int, float, List, np.ndarray]): wartość przybliżona w postaci wektora (n,1)
    
    Returns:
    Union[int, float, np.ndarray]: wartość normy L nieskończoność,
                                    NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(xr, List):
        xr = np.array(xr)
    if isinstance(x, List):
        x = np.array(x)

    if not (isinstance(x, int) or isinstance(x, float) or isinstance(x, np.ndarray)):
        return np.nan
    if not (isinstance(xr, int) or isinstance(xr, float) or isinstance(xr, np.ndarray)):
        return np.nan

    # poprawne rozmiary w przypadku wektorów/macierzy
    if isinstance(xr, np.ndarray) and isinstance(x, np.ndarray):
        if (len(xr.shape)!=1 or len(x.shape)!=1) or xr.shape != x.shape:
            return np.nan
        
    # liczba i wkektor jedno elementowy
    if isinstance(x, (int,float)) and isinstance(xr, np.ndarray):
        if xr.shape[0] > 1 or len(xr.shape) > 1:
            return np.nan
        
    if isinstance(xr, (int,float)) and isinstance(x, np.ndarray):
        if x.shape[0] > 1 or len(x.shape) > 1:
            return np.nan

    return np.max(np.abs(xr-x))

 
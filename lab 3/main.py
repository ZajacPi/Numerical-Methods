import numpy as np
import scipy
import pickle
import math
from typing import Union, List, Tuple


def p_diff(n: int, c: float) -> float:
    """Funkcja wylicza wartości wyrażeń P1 i P2 w zależności od n i c.
    Następnie zwraca wartość bezwzględną z ich różnicy.
    Szczegóły w Zadaniu 2.
    
    Parameters:
    n Union[int]: 
    c Union[int, float]: 
    
    Returns:
    diff float: różnica P1-P2
                NaN w przypadku błędnych danych wejściowych
    """
    if not(isinstance(n, int)) or not (isinstance(c, (int, float))):
        return np.NaN
  
    b = 2 ** n
    P1 = b - b + c
    P2 = b + c - b

    return np.abs(P1 - P2)

def exponential(x: Union[int, float], n: int) -> float:
    """Funkcja znajdująca przybliżenie funkcji exp(x).
    Do obliczania silni można użyć funkcji scipy.math.factorial(x)
    Szczegóły w Zadaniu 3.
    
    Parameters:
    x Union[int, float]: wykładnik funkcji ekspotencjalnej 
    n Union[int]: liczba wyrazów w ciągu
    
    Returns:
    exp_aprox float: aproksymowana wartość funkcji,
                     NaN w przypadku błędnych danych wejściowych
    """
    if not(isinstance(x, (float, int))) or not (isinstance(n, int)) or n<0:
        return np.NaN
    sum = 0
    for i in range(n):
        sum += ((1/scipy.special.factorial(i))  *  pow(x, i))
    return sum



def coskx1(k: int, x: Union[int, float]) -> float:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 1.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx float: aproksymowana wartość funkcji,
                 NaN w przypadku błędnych danych wejściowych
    """
    if not(isinstance(k, int)) or not (isinstance(x, (int, float))) or k<0:
        return np.NaN
    if k == 1:
        return np.cos(x)
    if k == 0:
        return 1
    return 2 * np.cos(x) * coskx1(k-1, x) - coskx1(k-2, x)
   
def coskx2(k: int, x: Union[int, float]) -> Tuple[float, float]:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 2.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx, sinkx float: aproksymowana wartość funkcji,
                        NaN w przypadku błędnych danych wejściowych
    """
    if not(isinstance(k, int)) or not (isinstance(x, (int, float))) or k<0:
        return np.NaN
    if k == 1:
        return (np.cos(x), np.sin(x))
    if k == 0:
        return (1, 0)
    
    # return np.cos(x) * coskx2(k-1, x) - np.sin(x) * sinkx(k-1, x)
    cosk_x, sin_kx = coskx2(k - 1, x)

    cos_kx = np.cos(x) * cosk_x - np.sin(x) * sin_kx
    sin_kx = np.sin(x) * cosk_x + np.cos(x) * sin_kx

    return (cos_kx, sin_kx)





import numpy as np
import scipy
import pickle

from typing import Union, List, Tuple


def absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu bezwzględnego. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu bezwzględnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    if not (isinstance(v, (int, float, list, np.ndarray))):
        return np.nan
    if not (isinstance(v_aprox, (int, float, list, np.ndarray))):
        return np.nan

    if isinstance(v, (list, np.ndarray)) and isinstance(v_aprox, (list, np.ndarray)):
        v = np.array(v)
        v_aprox = np.array(v_aprox)
        if v.shape != v_aprox.shape:
            return np.nan

        if isinstance(v, np.ndarray) and v.ndim == 2:  # czy to macierz???
            abs_error = np.zeros_like(v)
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    abs_error[i, j] = np.abs(v[i, j] - v_aprox[i, j])
        else:
            abs_error = np.abs(v - v_aprox)
    else:
        abs_error = np.abs(v - v_aprox)

    return abs_error



def relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu względnego.
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu względnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    if not isinstance(v, (int, float, list, np.ndarray)) or not isinstance(v_aprox, (int, float, list, np.ndarray)):
        return np.nan

    if isinstance(v, (list, np.ndarray)) and isinstance(v_aprox, (list, np.ndarray)):
        v = np.array(v)
        v_aprox = np.array(v_aprox)
        if v.shape != v_aprox.shape:
            return np.nan

        if isinstance(v, np.ndarray) and v.ndim == 2:  # Check if it's a matrix
            relative_err = np.zeros_like(v)
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    if v[i, j] != 0:
                        relative_err[i, j] = np.abs((v[i, j] - v_aprox[i, j]) / v[i, j])
                    else:
                        relative_err[i, j] = np.inf
        else:
            if v != 0:
                relative_err = np.abs((v - v_aprox) / v)
            else:
                relative_err = np.inf
    else:
        if v != 0:
            relative_err = np.abs((v - v_aprox) / v)
        else:
            relative_err = np.inf

    return relative_err
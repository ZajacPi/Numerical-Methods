import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple


def square_from_rectan(A: np.ndarray, b: np.ndarray):
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników na kwadratowy układ równań. Funkcja ma zwrócić nową macierz współczynników  i nowy wektor współczynników
    Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (n,n) i wektorem (n,)
             Jeżeli dane wejściowe niepoprawne funkcja zwraca None
     """
    try:
        # if A.shape[0] != b.shape[0]:
        #   return None
        sq_A = np.transpose(A) @ A
        sq_b = np.transpose(A) @ b
        return sq_A, sq_b
        
    except(ValueError, TypeError):
        return None

# # skopiowane z zadania domowego na lab5
def spare_matrix_Abt(m: int,n: int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,n), wektora b (m,)  i pomocniczego wektora t (m,) zawierających losowe wartości
    Parameters:
    m(int): ilość wierszy macierzy A
    n(int): ilość kolumn macierzy A
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,n) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        t = np.linspace(0, 1, m)
        # print(t)

        b = [np.cos(4*x) for x in t ]
        # print(b)
        A = np.vander(t, n)
        A_flipped = np.fliplr(A)
        # print(A_flipped)
        return A_flipped, b
    except(TypeError, ValueError):
        return None


#skopiowane z lab4
def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      x: wektor x (n,) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów
      """
    try:
        res_form = np.linalg.norm(b - A @ x)
        return res_form
  
    except(ValueError):
      return None
       
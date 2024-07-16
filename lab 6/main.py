import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple

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

def is_diagonaly_dominant(A: np.ndarray | sp.sparse._csc.csc_array):
    """Funkcja sprawdzająca czy podana macierz jest diagonalnie zdominowana
      Jeśli A jest innego typu, lub nie jest kwadratowa, funkcja powinna zwracać None
      
      Parameters:
      A: macierz A (m,m) podlegająca weryfikacji

      Results:
      (bool)- True jeśli macierz jest diagonalnie zdominowana, w przeciwnym wypadku False
      """
    if not isinstance(A, (np.ndarray, sp.sparse._csc.csc_array)):
      return None
    if isinstance(A, np.ndarray):
      if A.ndim != 2 or A.shape[0] != A.shape[1] or type(A.shape) != tuple:
        return None 
      diagonal = np.abs(A.diagonal())
      difference = np.sum(np.abs(A), axis=1) - 2 * diagonal
      return np.all(difference<=0)

    elif isinstance(A, sp.sparse._csc.csc_array):
      diagonal = np.abs(A.diagonal())
      difference = np.array(A.sum(axis=1)).flatten() - 2 * diagonal
      return np.all(difference <= 0)

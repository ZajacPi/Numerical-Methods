import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle
import random

# zad1
def polly_A(x: np.ndarray):
    """Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    Parameters:
    x: wektor pierwiastków
    Results:
    (np.ndarray): wektor współczynników
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(x, np.ndarray):
        return None
    else:
        return  P.polyfromroots(x)
        
def roots_20(a: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray): wektor współczynników i miejsc zerowych w danej pętli
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
"""
    if not isinstance(a, np.ndarray):
        return None
    # for i in range(20):
    # muszę zmienić typ int64 na float bo inaczej nie działa
    a = a.astype(np.float64)
    a += 1e-10 * np.random.uniform(0, 1, size=a.shape)
    # print(a)
    b = P.polyroots(a)
    # print(b)

    return a, b
        
# zad 2

def frob_a(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(wsp, np.ndarray) or wsp.ndim != 1:
        return None
    
    n = len(wsp) 
    #tworzę pustą macierz z zerami
    frob_matrix = np.zeros((n, n))

    #na dobrych miejscach daję jedynki
    for i in range(n - 1):
        frob_matrix[i, i + 1] = 1
    
    for i in range(n):
        frob_matrix[n-1, i] = wsp[i]

    eigenvalues = np.linalg.eigvals(frob_matrix)
    schur_values = scipy.linalg.schur(frob_matrix, output = 'complex')
    roots =P.polyroots(wsp)
    return frob_matrix, eigenvalues, schur_values, roots



    

# zad 4
def is_nonsingular(A: np.ndarray)->bool:
    """Funkcja sprawdzająca czy podana macierz jest niesingularna.
    
    Parameters:
    A (np.ndarray): macierz nxn do przetestowania 
    
    Results:
    (bool): jeżeli macierz A jest singularna funkcja zwraca False w przeciwnym przypadku zwraca True
    
    Jeżeli dane wejściowe są niepoprawne funkcja zwraca None
    """
    if not isinstance(A, np.ndarray):
        return None
    try:
        n = len(A)
        elem_len = len(A[0])
        for i in range(n-1):
            if len(A[i]) != elem_len:
                return None
            
        if A.shape[0] != A.shape[1]:
            return False
        
            
        det = np.linalg.det(A)

        if det == 0:
            return False

        return True
    except(ValueError, TypeError):
        return None
# a = np.array([31,  1, 89, 72, 73, 66, 79, 16, 17, 98], dtype=np.int64)
# roots_20(a)
# array([-1.05708445+0.j        , -0.68827767-0.62997666j...8j,  0.15336676-0.61881984j,
#         0.15336676+0.61881984j,  0.85599815-0.70751121j,
#         0.85599815+0.70751121j]))



# wsp = np.array([9, 7, 1, 8, 9, 8, 9, 1, 8, 8], dtype=np.int64)
# print(frob_a(wsp))
# result =(array([[0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
# E                    [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
# E                    [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
# E                    [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
# E                    [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
# E                    [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
# E                    [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
# E                    [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
# E                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
# E                    [9., 7., 1., 8., 9., 8., 9., 1., 8., 8.]]), 

#                       array([ 8.92320259+0.j        ,  0.78315902+0.59468731j,
# E                     0.78315902-0.59468731j,  0.49614863+0.89080845j,
# E                     0.49614863-0.89080845j, -0.29668032+0.95832671j,
# E                    -0.29668032-0.95832671j, -1.15431769+0.j        ,
# E                    -0.86706978+0.33428263j, -0.86706978-0.33428263j]), 
#                      
#                      array([[ 8.92320259e+00,  2.47223375e-08],
# E                    [-4.06171670e+00,  9.63959191e-02],
# E                    [-5.55691920e-01,  4.66498338e-01],
# E                    [ 3.91113466e+00,  1.23487493e-01],
# E                    [ 7.61186345e+00,  4.99303006e-01],
# E                    [ 5.53091877e-02,  3.36134804e-01],
# E                    [ 7.22329730e+00,  4.11221117e-01],
# E                    [ 9.99697179e+00, -5.99690596e-02],
# E                    [ 3.92450292e+00,  4.67898970e-01],
# E                    [-1.44184731e+01,  6.26045349e-02]]), 

#                       array([-1.27188076, -0.87040291, -0.87040291, -0.29254545, -0.29254545,
# E                     0.50629351,  0.50629351,  0.79259524,  0.79259524])), 
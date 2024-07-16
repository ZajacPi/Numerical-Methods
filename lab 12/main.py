import numpy as np
from typing import Union, Callable


def solve_euler(fun: Callable, t_span: np.array, y0: np.array):
    ''' 
    Funkcja umożliwiająca rozwiązanie układu równań różniczkowych z wykorzystaniem metody Eulera w przód.
    
    Parameters:
    fun: Prawa strona równania. Podana funkcja musi mieć postać fun(t, y). 
    Tutaj t jest skalarem i istnieją dwie opcje dla ndarray y: Może mieć kształt (n,); wtedy fun musi zwrócić array_like z kształtem (n,). 
    Alternatywnie może mieć kształt (n, k); wtedy fun musi zwrócić tablicę typu array_like z kształtem (n, k), tj. każda kolumna odpowiada jednej kolumnie w y. 
    t_span: wektor czasu dla którego ma zostać rozwiązane równanie
    y0: warunke początkowy równania o wymiarze (n,)
    Results:
    (np.array): macierz o wymiarze (n,m) zawierająca w wkolumnach kolejne rozwiązania fun w czasie t_span. W przypadku błędnych danych wejściowych powinna zwracać None

    '''
    
     
    if not(isinstance(fun, Callable) and isinstance(t_span, np.ndarray) and isinstance(y0, np.ndarray)):
        return None
    y = y0
    
    for i in range(0, y.shape[0] - 1):
        y[i + 1, :] = y[i, :] + fun(y[i, :], t_span[i]) * (t_span[i + 1] - t_span[i])
    return y
    


def arenstorf(t, x: np.array):
    '''     
    Parameters:
    t: czas
    x: wektor stanu 
    Results:
    (np.array): wektor pochodnych stanu
    '''
    try:
        if not(isinstance(t, int) or isinstance(t, float)):
            return None
        u = 0.012277471
        u_p = 1 - u
        D1 = np.power(np.power(x[0] + u ,2) + np.power(x[2],2),3/2)
        D2 = np.power(np.power(x[0] - u_p,2) + np.power(x[2],2),3/2)
        dx1 = x[1]
        dx2 = x[0] + 2 * x[3] - u_p * (x[0] + u) / D1 - u * (x[0] - u_p) / D2
        dx3 = x[3]
        dx4 = x[2] - 2 * x[1] - u_p * x[2] / D1 -  u * x[2] / D2
        return np.array([dx1, dx2, dx3, dx4])
    except(ValueError, TypeError):
        return None
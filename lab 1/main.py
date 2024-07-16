import math
import numpy as np
import scipy

#zad 1 py -3 -m  pip install pytest

print("zad 2")
def cylinder_area(r:float, h:float) -> float:
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """

    return (2 * math.pi * r**2) + (2*math.pi*r* h) if 0<h and 0<r  else math.nan


print("zad 3")
def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if (n <=0) or (type(n) is not int):
        return None
    else:
        if n <=2:
            fib = []
            for i in range(n):
                fib.append(1)
        
        else:
            fib = [1, 1]
            for i in range(2, n):
                fib.append(fib[i-2] + fib[i-1])
        #RESHAPE JAK W MATLABIE!!!! Ale tylko wtedy jak jest więcej elementów
            fib = np.reshape(fib, (1, n))       
        return fib
print(fib(4))

print("zad 4")
def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    # Wykonanie macierzy
    A = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    print(A)
    # Wyznacznik
    Mdet = scipy.linalg.det(A)
    print(Mdet)
    # Macierz odwrotna
    if Mdet != 0:
        Minv = scipy.linalg.inv(A)
    else:
        Minv = math.nan
    print(Minv)
    # Macierz transponowana
    Mt = np.transpose(A)
    print(Mt)

    return (Minv, Mt, Mdet)
matrix_calculations(4)


print("zad 6")
def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if (m <= 0) or (n <=0) or (type(n) is not int) or (type(m) is not int):
        return None
    else:
        empty_matrix = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                if i>j:
                    empty_matrix[i, j] = i
                else:
                    empty_matrix[i, j] = j

        print (empty_matrix)
        return empty_matrix
custom_matrix(4,7)

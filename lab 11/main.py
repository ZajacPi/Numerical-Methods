import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss


from typing import Union, List, Tuple

def rectangular_rule(func, a, b, n):
    """
    Metoda prostokątów do przybliżonego rozwiązania całki oznaczonej.

    :param func: Funkcja, której całkę oznaczoną chcemy przybliżyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podprzedziałów (większa liczba n daje dokładniejsze przybliżenie).
    :return: Przybliżona wartość całki oznaczonej.
    """
    try:
        h = (b-a)/n
        sum = 0
        while a<b:
            sum += func(a)
            a+=h
        return sum*h
    except(ValueError, TypeError):
        return None


def trapezoidal_rule(func, a, b, n):
    """
    Metoda trapezów do przybliżonego rozwiązania całki oznaczonej.

    :param func: Funkcja, której całkę oznaczoną chcemy przybliżyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podprzedziałów (większa liczba n daje dokładniejsze przybliżenie).
    :return: Przybliżona wartość całki oznaczonej.
    """
    try:
        h = (b-a)/n
        sum = 0
        while a<b:
            sum += h/2*(func(a+h)+func(a))
            a+=h
        return sum
    except(ValueError, TypeError):
        return None



def custom_integration(func, a, b, order):
    """
    Własna funkcja całkująca, wykorzystująca kwadraturę Gaussa-Legendre'a.

    :param func: Funkcja do zintegrowania.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param order: Rząd kwadratury.
    :return: Przybliżona wartość całki.
    """
    # Przeskalowanie przedziału do (a, b)
    # Obliczenie wartości funkcji w przeskalowanych punktach
    # Obliczenie całki przy użyciu kwadratury Gaussa-Legendre'a
    try:
       # Przeskalowanie przedziału do (a, b)
        scaled_points = 0.5 * (b - a) * leggauss(order)[0] + 0.5 * (b + a)
        
        # Obliczenie wartości funkcji w przeskalowanych punktach
        function_values = func(scaled_points)
        
        # Obliczenie całki przy użyciu kwadratury Gaussa-Legendre'a
        integral_approximation = 0.5 * (b - a) * np.dot(function_values, leggauss(order)[1])
        
        return integral_approximation
    except(ValueError, TypeError):
        return None



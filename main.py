import math
import numpy as np
import pandas as pd

def cylinder_area(r: float,h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0:
        return 2 * r * r * math.pi + 2 * r * h * math.pi
    else:
        return np.NaN

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    list = [0]
    a_adv, b_adv = 0, 1
    if n < 0 or not isinstance(n, int):
        return None
    elif n == 0:
        pass
    elif n == 1:
        list.append(1)
    else:
        for _ in range(0, n):
            a_adv, b_adv= b_adv, a_adv + b_adv
            list.append(a_adv) 
    return np.array(list)

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
    M = np.array([[a,1,-a],[0,1,1],[-a,a,1]])
    Mt = np.transpose(M)
    Mdet = np.linalg.det(M)
    if Mdet == 0:
        return np.NaN
    else:
        Minv = np.linalg.inv(M)
        return (Minv, Mt, Mdet)


def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    Matrix = np.zeros((m,n))
    
    for a in range(0,n):
        for b in range(0,m):
            if m > n:
                Matrix[b,a] = b
            else:
                Matrix[b,a] = a
    return Matrix
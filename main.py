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
    """
    powyzsza bardzo prosta funkcja, wykorzystuje pi z biblioteki math oraz dziala tylko i wylacznie w przypadku podania poprawnych wartosci w wywolaniu funkcji
    """

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
    if n < 0 or not isinstance(n, int): #sprawdzam czy wprowadzony zostal poprawny argument
        return None
    elif n == 0:
        pass
    elif n == 1: #ustalenie poszczegolnych warunkow przy podaniu jako argument 1 lub 0
        list.append(1)
    else:
        for _ in range(0, n): #wlasciwa funkcja ktora oblicza element ciagu fibonaciego oraz dodaje ja do listy
            a_adv, b_adv= b_adv, a_adv + b_adv
            list.append(a_adv) 
    return np.array(list) #zwracana jest wartosc jako przeksztalcona lista  w array

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
    Mdet = np.linalg.det(M) #wykorzystanie gotowych funkcji z biblioteki numpy
    if Mdet == 0: #sprawdzenie czy istnieje macierz odwrotna
        return np.NaN
    else:
        Minv = np.linalg.inv(M)
        return (Minv, Mt, Mdet) #zwrocenie otrzymanych wynikow w postaci krotki, mozna zapisac ja bez nawiasow


def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m is not int or n is not int:
        return None


    Matrix = np.zeros((m,n)) #stworzenie macierzy o zadanych rozmiarach, ktora zostanie uzupelniona   

    for a in range(0,n): #utworzone dwie petle ktore nastepnie wypelniaja odpowiednio kazdy element macierzy, ten sposob wymaga wykorzystania wiekszej mocy obliczeniowej poniewaz 
        for b in range(0,m): #funkcja w kazdej petli spradza warunek if
            if m > n:
                Matrix[b,a] = b + 1
            else:
                Matrix[b,a] = a + 1
    return Matrix
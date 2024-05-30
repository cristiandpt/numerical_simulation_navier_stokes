import sys
import numpy as np
import copy as cp
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import scipy.interpolate

def interpolar_splines_bicubicos(matriz):
    filas, columnas = matriz.shape

    # Doblar las filas y columnas
    nuevas_filas = 2 * filas
    nuevas_columnas = 2 * columnas

    # Coordenadas originales en el rango [0, 1]
    x_original = np.linspace(0, 1, columnas)
    y_original = np.linspace(0, 1, filas)

    # Coordenadas nuevas en el rango [0, 1]
    x_nuevo = np.linspace(0, 1, nuevas_columnas)
    y_nuevo = np.linspace(0, 1, nuevas_filas)

    # Crear spline bicubico
    spline = RectBivariateSpline(y_original, x_original, matriz, kx=3, ky=3)

    # Evaluar spline en las nuevas coordenadas
    matriz_interpolada = spline(y_nuevo, x_nuevo)

    return matriz_interpolada

def interpolar_bilineal(matriz):
    filas, columnas = matriz.shape

    # Doblar las filas y columnas
    nuevas_filas = 2 * filas
    nuevas_columnas = 2 * columnas

    # Coordenadas originales en el rango [0, 1]
    x_original = np.linspace(0, 1, columnas)
    y_original = np.linspace(0, 1, filas)

    # Coordenadas nuevas en el rango [0, 1]
    x_nuevo = np.linspace(0, 1, nuevas_columnas)
    y_nuevo = np.linspace(0, 1, nuevas_filas)

    # Crear interpolación bilineal
    interpolador = interp2d(x_original, y_original, matriz, kind='linear')

    # Evaluar interpolación en las nuevas coordenadas
    matriz_interpolada = interpolador(x_nuevo, y_nuevo)

    return matriz_interpolada

def interpolar_spline_orden_superior(matriz, order=5):
    filas, columnas = matriz.shape

    # Doblar las filas y columnas
    nuevas_filas = 2 * filas
    nuevas_columnas = 2 * columnas

    # Coordenadas originales en el rango [0, 1]
    x_original = np.linspace(0, 1, columnas)
    y_original = np.linspace(0, 1, filas)

    # Coordenadas nuevas en el rango [0, 1]
    x_nuevo = np.linspace(0, 1, nuevas_columnas)
    y_nuevo = np.linspace(0, 1, nuevas_filas)

    # Crear spline de orden superior
    spline = scipy.interpolate.RectBivariateSpline(y_original, x_original, matriz, kx=order, ky=order)

    # Evaluar spline en las nuevas coordenadas
    matriz_interpolada = spline(y_nuevo, x_nuevo)

    return matriz_interpolada
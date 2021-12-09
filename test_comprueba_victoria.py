from main import valido
import pytest

# valido(Tablero,Casilla)

Tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def Testvalido():
    assert valido(Tablero,10) == False , "Fallo en la funcion"
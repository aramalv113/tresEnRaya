from main import comprueba_victoria
import pytest

# comprueba_victoria(Tablero)

Tablero = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'O']

def Testcomprueba_victoria():
    assert comprueba_victoria(Tablero) == True , "Fallo en la funcion"
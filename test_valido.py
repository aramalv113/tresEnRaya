from main import valido
import pytest

# valido(Tablero,Casilla)

Tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

@pytest.mark.parametrize("Tablero,Jugadas,Resultado", ([Tablero,10,False],[Tablero,5,True],[Tablero,4,True],[Tablero,11,False],[Tablero,9,False]) )

def test_valido(Tablero,Jugadas,Resultado):
    assert valido(Tablero,Jugadas) == Resultado
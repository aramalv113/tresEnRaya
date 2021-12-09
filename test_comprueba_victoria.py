from main import comprueba_victoria
import pytest

# comprueba_victoria(Tablero)

# Tablero = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
@pytest.mark.parametrize("Tablero,Resultado", ([
['X', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],False],
[['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],True],
[['O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'],False]
) )

def test_comprueba_victoria(Tablero,Resultado):
    assert comprueba_victoria(Tablero) == Resultado
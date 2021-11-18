
import os
import random
from threading import Event

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def VerNumero(Dato):
    # Verificacion de si el objeto puede convertirse a numero
    try:
        int(Dato)
        return True
    except ValueError:
        return False

def Encabezado():
    # Encabezado de la aplicacion
    Clear()
    print("Juego de Tres en Raya")
    print("Los numeros del Tablero estan ordenados de izquierda a derecha.")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()

def Errores(Dato):
    # Impresion de errores
    print(Dato)
    print("- "*20)
    Event().wait(1) 

def Tablero_juego(Tablero):
    # Impresion del tablero en juego
    print("- "*20)
    print("Tablero de Juego")
    print("",Tablero[0],"|",Tablero[1],"|",Tablero[2])
    print("-----------")
    print("",Tablero[3],"|",Tablero[4],"|",Tablero[5])
    print("-----------")
    print("",Tablero[6],"|",Tablero[7],"|",Tablero[8])
    print("- "*20)
    print()

def comprueba_victoria(Tablero):
    # Revisar las lineas horizontales
    if (Tablero[0] == Tablero[1] == Tablero[2] != ' ') or (Tablero[3] == Tablero[4] == Tablero[5] != ' ') or (Tablero[6] == Tablero[7] == Tablero[8] != ' '):
        return False
    # Revisar las lineas verticales
    elif (Tablero[0] == Tablero[3] == Tablero[6] != ' ') or (Tablero[1] == Tablero[4] == Tablero[7] != ' ') or (Tablero[2] == Tablero[5] == Tablero[6] != ' '):
        return False
    # Revisar las lineas diagonales
    elif (Tablero[0] == Tablero[4] == Tablero[8] != ' ') or (Tablero[6] == Tablero[4] == Tablero[2] != ' '):
        return False
    else:
        return True

# Funciones de IA que aun no sabemos como mrd adaptarla a nuestro codigo

if __name__ == "__main__":

    # Variables
    # Guardardo del Tablero
    Tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Creacion Primer Jugador
    Jugador = "X"
    # Creacion de las jugadas
    Jugadas = 1
    # Variagle de Gamemode
    GamemodeSeleccionado = False
    # Creacion de IA
    Movimientos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:

        if not GamemodeSeleccionado:
            Clear()
            print("Selecciona el modo de juego")
            print("PvP -> Jugador vs Jugador", Jugador)
            print("PvE -> Jugador vs IA", Jugador)

            Gamemode = input("Selecciona si quieres PvP o PvE ")
            if Gamemode == 'pvp' or Gamemode == 'pve':
                GamemodeSeleccionado = True
            else:
                Errores('Solo Tenemos el modo de juego pvp y pve')

        if Gamemode == 'pvp':
            Encabezado()
            Tablero_juego(Tablero)
            print("Turno del jugador", Jugador)
            Casilla = input("Selecciona una casilla del (1-9) ")
            if VerNumero(Casilla):
                # La tabla es de 0 a 8 entonces se necesita restar 1 a la respuesta para un funcionamiento mas simple.
                Casilla = int(Casilla) - 1
                if Casilla >= 0 or Casilla <= 9:
                    if Tablero[Casilla] != " ":
                        Errores('Esa posicion ya esta en uso.')
                        continue
                    else:
                        Tablero[Casilla] = Jugador
                        Jugadas = Jugadas + 1
                else:
                    Errores('Posicion invalida')
                    continue

                if comprueba_victoria(Tablero):
                    if Jugador == "X":
                        Jugador = "O"
                    else:
                        Jugador = "X"
                else:
                    Clear()
                    Tablero_juego(Tablero)
                    print("Se termino el juego el ganador es", Jugador)
                    Event().wait(5) 
                    break
            
                if Jugadas >= 9:
                    Clear()
                    Tablero_juego(Tablero)
                    Errores("El juego termina en empate")
                    break
            else:
                Errores('Solo se Admiten numeros')

        elif Gamemode == 'pve':
            Encabezado()
            Tablero_juego(Tablero)
            print("Turno del jugador", Jugador)
            if Jugador == "O":
                Casilla = random.choice(Movimientos)
            else:
                Casilla = input("Selecciona una casilla del (1-9) ")
            if VerNumero(Casilla):
                # La tabla es de 0 a 8 entonces se necesita restar 1 a la respuesta para un funcionamiento mas simple.
                Casilla = int(Casilla) - 1
                if Casilla >= 0 or Casilla <= 9:
                    if Tablero[Casilla] != " ":
                        Errores('Esa posicion ya esta en uso.')
                        continue
                    else:
                        # Esto sirve para que la IA no repita casillas que ya estan en uso
                        Movimientos.remove(Casilla+1)
                        Tablero[Casilla] = Jugador
                        Jugadas = Jugadas + 1
                else:
                    Errores('Posicion invalida')
                    continue

                if comprueba_victoria(Tablero):
                    if Jugador == "X":
                        Jugador = "O"
                    else:
                        Jugador = "X"
                else:
                    Clear()
                    Tablero_juego(Tablero)
                    print("Se termino el juego el ganador es", Jugador)
                    Event().wait(5) 
                    break
            
                if Jugadas >= 9:
                    Clear()
                    Tablero_juego(Tablero)
                    Errores("El juego termina en empate")
                    break
            else:
                Errores('Solo se Admiten numeros')

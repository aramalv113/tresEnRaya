
import curses

CH_P1 = 'X'
CH_P2 = 'O'
X_STEP = 4
Y_STEP = 2
X_OFFSET = 1
Y_OFFSET = 4

def print_board(consola):
    #consola.addstr(0, 0, 'Tic Tac Toe')
    consola.hline(1, 0, '-', 50)
    #consola.addstr(2, 0, 'Usa flechas para moverte │ [F] Seleccionar │ [X] Salir')
    consola.addstr(Y_OFFSET    , X_OFFSET, '  │   │  ')
    consola.addstr(Y_OFFSET + 1, X_OFFSET, '──┼───┼──')
    consola.addstr(Y_OFFSET + 2, X_OFFSET, '  │   │  ')
    consola.addstr(Y_OFFSET + 3, X_OFFSET, '──┼───┼──')
    consola.addstr(Y_OFFSET + 4, X_OFFSET, '  │   │  ')

def print_players(consola, player_id):
    consola.addstr(Y_OFFSET + 6, 0, 'Player {}'.format(CH_P1),curses.A_BOLD if player_id == 0 else 0)
    consola.addstr(Y_OFFSET + 7, 0, 'Player {}'.format(CH_P2),curses.A_BOLD if player_id == 1 else 0)

def draw(y, x, consola, player_id):
    consola.addch(y, x, CH_P2 if player_id else CH_P1)

def check_victory(Tablero, y, x):
    if Tablero[0][x] == Tablero[1][x] == Tablero[2][x]:
        return True
    if Tablero[y][0] == Tablero[y][1] == Tablero[y][2]:
        return True
    if x == y and Tablero[0][0] == Tablero[1][1] == Tablero[2][2]:
        return True
    if x + y == 2 and Tablero[0][2] == Tablero[1][1] == Tablero[2][0]:
        return True
    return False

def main(consola):
    # Clear screen
    # consola.clear()

    print_board(consola)
    player_id = 0
    print_players(consola, player_id=player_id)

    x_pos = 1
    y_pos = 1
    board = [list('   ') for _ in range(3)]

    # This raises ZeroDivisionError when i == 10.
    while True:
        consola.move(Y_OFFSET + y_pos * Y_STEP, X_OFFSET + x_pos * X_STEP)

        c = consola.getch()
        if c == curses.KEY_UP:
            y_pos = max(0, y_pos - 1)
        elif c == curses.KEY_DOWN:
            y_pos = min(2, y_pos + 1)
        elif c == curses.KEY_LEFT:
            x_pos = max(0, x_pos - 1)
        elif c == curses.KEY_RIGHT:
            x_pos = min(2, x_pos + 1)
        elif c == ord('x') or c == ord('X'):
            break
        elif c == ord('f') or c == ord('F'):
            # Update
            y, x = consola.getyx()
            if consola.inch(y, x) != ( ord('f') or ord('F') ):
                continue

            draw(y, x, consola, player_id)
            board[y_pos][x_pos] = CH_P2 if player_id else CH_P1

            if check_victory(board, y_pos, x_pos):
                consola.addstr(Y_OFFSET + 9, 0, 'Player {} wins'.format(
                    CH_P2 if player_id else CH_P1))
                break

            # Switch player
            player_id = (player_id + 1) % 2
            print_players(consola, player_id)

    consola.refresh()
    consola.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
import jugador1
import time


def computadora(tablerojugador, tablerocomputadora, tablerovacio1, tablerovacio2):
    import random
    while 'O' in tablerocomputadora and 'O' in tablerojugador:
        try:
            x = random.randint(0,9)
            y = random.randint(0,9)
            if tablerocomputadora[x,y] == 'O':
                tablerocomputadora[x,y] = 'X'
                tablerovacio2[x,y] = 'X'
                print('La computadora ha TOCADO tu barco!\n')
                print('\U0001F92F')
                print()
                print(tablerocomputadora)
                time.sleep(5)
                continue
            elif tablerocomputadora[x,y] == ' ':
                tablerocomputadora[x,y] = '-'
                tablerovacio2[x,y] = '-'
                print('La computadora ha fallado!')
                print()
                print(tablerocomputadora)
                time.sleep(5)
                jugador1.jugador1(tablerojugador,tablerocomputadora,tablerovacio1,tablerovacio2)
            else:
                continue

        except:
            print('error')
            continue